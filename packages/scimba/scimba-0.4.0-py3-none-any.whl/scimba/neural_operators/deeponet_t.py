import scimba.largenets.pointnet as pointnet
import scimba.nets.mlp as mlp
import torch
from scimba.sampling.data_sampling_ode import ode_loss_evaluation
from torch import nn
from torch.autograd import grad as grad

# from scimba import nets, pinns


def DeepONetTime(net: nn.Module, **kwargs):
    class DeepONetTime(net):
        def __init__(self, ode, ode_sampler, lat_size=5, **kwargs):
            super().__init__(ode)

            self.n_sensor = ode_sampler.n_sensor
            self.n_outputs = ode.nb_unknowns
            self.lat_size = lat_size

            self.dim_t = 1
            self.dim_f = ode_sampler.source.dim_f

            self.encoder = kwargs.get("encoder_type", "MLP")
            self.decoder = kwargs.get("decoder_type", "linear")
            self.activation_type = kwargs.get("activation_type", "tanh")
            self.feature = kwargs.get("feature_type", "pointwise")
            self.layers_b = kwargs.get("layers_b", [20, 40, 40, 20])
            self.layers_t = kwargs.get("layers_t", [20, 40, 40, 20])

            self.varying_sizes = False

            # construction of the encoder:
            # inputs: the function at some points
            # outputs: the latent variables
            print("lat_size", self.lat_size)
            print("n_outputs", self.n_outputs)

            if self.encoder == "PointNet":
                # Note: dim_u is the dimension of the source function f(x) on the
                # RHS of the equation. It is different from u the solution as used
                # in the original PointNet
                self.branch_net = pointnet.PointNet(
                    self.dim_t,
                    self.dim_f,
                    self.lat_size * self.n_outputs,
                    activation_type="tanh",
                    width01=(20, 10),
                    depth01=(2, 2),
                    use_layer_normalization=False,
                    add_Tnet01=(False, False),
                )
                self.varying_sizes = True
            else:
                n_inputs = self.n_sensor * self.dim_f
                self.branch_net = mlp.GenericMLP(
                    n_inputs,
                    self.lat_size * self.n_outputs,
                    activation_type=self.activation_type,
                    layer_sizes=self.layers_b,
                )
                self.varying_sizes = False

            # construction of the decoder,
            # which can be linear or nonlinear w.r.t. the latent variables

            self.dim = (
                self.dim_t
                + ode.nb_parameters
                + ode_sampler.sampler_initial_condition.dim
            )

            if self.decoder == "linear":
                in_size = self.dim
                out_size = self.lat_size * self.n_outputs
            else:
                in_size = self.n_outputs * self.lat_size + self.dim
                out_size = self.n_outputs

            self.trunk_net = net(
                ode,
                layer_sizes=self.layers_t,
                activation_type=self.activation_type,
                inputs_size=in_size,
                outputs_size=out_size,
            )

        def forward_encoder(
            self, t_sensor: torch.Tensor, f_sensor: torch.Tensor
        ) -> torch.Tensor:
            if self.encoder == "PointNet":
                t = t_sensor.transpose(1, 2)
                f = f_sensor.transpose(1, 2)
                return self.branch_net(t, f)
            else:
                return self.branch_net(f_sensor)

        def forward_decoder(
            self,
            t: torch.Tensor,
            mu: torch.Tensor,
            w_initial: torch.Tensor,
            z: torch.Tensor,
        ) -> torch.Tensor:
            if self.decoder == "linear":
                params = torch.cat([mu, w_initial], axis=1)
                trunk_res = self.trunk_net.forward(t, params)
                new_shape = (-1, self.lat_size, self.n_outputs)
                z = z.reshape(new_shape)
                trunk_res = trunk_res.reshape(new_shape)
                return torch.sum(z * trunk_res, dim=1)

            else:
                params = torch.cat([mu, w_initial, z], axis=1)
                return self.trunk_net.forward(t, params)

        def forward(
            self, t: torch.Tensor, mu: torch.Tensor, sample: ode_loss_evaluation
        ) -> torch.Tensor:
            # vect.size() [N_batches, dim_t, n_sensor]
            # vecf.size() [N_batches, dim_f, n_sensor]
            # So the output tensor will have the size [N_batches, 1, n_sensor]
            # which need to be squeeze down to 2 dimensions before being passed
            # to the decoder
            z = self.forward_encoder(sample.t_sensor, sample.f_sensor)
            if self.lat_size > 1 or self.encoder != "PointNet":
                z = z.squeeze(1)
            return self.forward_decoder(t, mu, sample.w_initial, z)

    return DeepONetTime(**kwargs)
