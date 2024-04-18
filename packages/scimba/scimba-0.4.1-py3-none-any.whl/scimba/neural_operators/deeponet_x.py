import torch

from ..equations import pdes
from ..largenets.pointnet import PointNet
from ..nets import mlp
from ..sampling.data_sampling_pde_x import (
    pde_loss_evaluation,
    pde_loss_evaluation_bc,
    pde_x_data,
)


def DeepONetSpace(net: torch.nn.Module, **kwargs):
    """
    Create a space-only DeepONet
    """

    class DeepONetSpace(net):
        def __init__(
            self,
            pde: pdes.AbstractPDEx,
            pde_sampler: pde_x_data,
            lat_size=5,
            **kwargs,
        ):
            super().__init__(pde)

            self.pde = pde
            self.pde_sampler = pde_sampler
            self.lat_size = lat_size

            self.dim_x = pde.dimension_x
            self.dim_f = pde_sampler.source.dim_f
            self.dim_f_bc = pde_sampler.boundary.dim_f
            self.dim = self.dim_x + pde.nb_parameters

            self.n_sensor = pde_sampler.n_sensor
            self.n_sensor_bc = pde_sampler.n_sensor_bc

            self.n_inputs = self.dim_f * self.n_sensor
            self.n_inputs_bc = self.dim_f_bc * self.n_sensor_bc
            self.n_outputs = pde.nb_unknowns

            self.encoder = kwargs.get("encoder_type", "MLP")
            self.decoder = kwargs.get("decoder_type", "linear")
            self.activation_type = kwargs.get("activation_type", "tanh")
            self.feature = kwargs.get("feature_type", "pointwise")
            self.layers_b = kwargs.get("layers_b", [20, 40, 40, 20])
            self.layers_t = kwargs.get("layers_t", [20, 40, 40, 20])

            self.varying_sizes = False
            self.activate_bc = self.dim_f_bc > 0

            if self.encoder == "PointNet":
                # Note: dim_u is the dimension of the source function f(x) on the
                # RHS of the equation. It is different from u the solution as used
                # in the original PointNet
                self.branch_net = PointNet(
                    self.dim_x,
                    self.dim_f,
                    self.lat_size * self.n_outputs,
                    activation_type="tanh",
                    width01=(10, 10),
                    depth01=(2, 2),
                    use_layer_normalization=False,
                    add_Tnet01=(False, False),
                )
                self.varying_sizes = True

                if self.activate_bc:
                    self.branch_net_bc = PointNet(
                        self.dim_x,
                        self.dim_f_bc,
                        self.lat_size * self.n_outputs,
                        activation_type="tanh",
                        width01=(10, 10),
                        depth01=(2, 2),
                        use_layer_normalization=False,
                        add_Tnet01=(False, False),
                    )

            elif self.encoder == "MLP":
                self.branch_net = mlp.GenericMLP(
                    self.n_inputs,
                    self.lat_size * self.n_outputs,
                    activation_type=self.activation_type,
                    layer_sizes=self.layers_b,
                )
                if self.activate_bc:
                    self.branch_net_bc = mlp.GenericMLP(
                        self.n_inputs_bc,
                        self.lat_size * self.n_outputs,
                        activation_type=self.activation_type,
                        layer_sizes=self.layers_b,
                    )
                self.varying_sizes = False

            # construction of the decoder,
            # which can be linear or nonlinear w.r.t. the latent variables
            if self.decoder == "linear":
                in_size = self.dim
                out_size = self.lat_size * (1 + self.activate_bc) * self.n_outputs
            else:
                in_size = (
                    self.n_outputs * self.lat_size * (1 + self.activate_bc) + self.dim
                )
                out_size = self.n_outputs

            self.trunk_net = net(
                pde,
                layer_sizes=self.layers_t,
                activation_type=self.activation_type,
                inputs_size=in_size,
                outputs_size=out_size,
            )

        def forward_encoder(
            self,
            x_sensor: torch.Tensor,
            x_sensor_bc: torch.Tensor,
            f_sensor: torch.Tensor,
            f_sensor_bc: torch.Tensor,
        ) -> torch.Tensor:
            if self.encoder == "PointNet":
                x = x_sensor.x.transpose(1, 2)
                f = f_sensor.transpose(1, 2)
                z = self.branch_net(x, f)
                if self.activate_bc:
                    x_bc = x_sensor_bc.x.transpose(1, 2)
                    f_bc = f_sensor_bc.transpose(1, 2)
                    z_bc = self.branch_net_bc(x_bc, f_bc)
                    z = torch.cat([z, z_bc], axis=1)
            else:
                z = self.branch_net(f_sensor)
                if self.activate_bc:
                    shape = (-1, 1, self.dim_f_bc * self.n_sensor_bc)
                    z_bc = self.branch_net_bc(f_sensor_bc.reshape(shape))
                    z = torch.cat([z, z_bc], axis=1)
            return z

        def forward_decoder(
            self, x: torch.Tensor, mu: torch.Tensor, z: torch.Tensor
        ) -> torch.Tensor:
            if self.decoder == "linear":
                trunk_res = self.trunk_net.forward(x, mu)
                shape = (-1, self.lat_size * (1 + self.activate_bc), self.n_outputs)
                z = z.reshape(shape)
                trunk_res = trunk_res.reshape(shape)
                return torch.sum(z * trunk_res, dim=1)
            else:
                shape = (-1, (1 + self.activate_bc) * self.n_outputs * self.lat_size)
                params = torch.cat([mu, z.reshape(shape)], axis=1)
                return self.trunk_net.forward(x, params)

        def forward(
            self,
            x: torch.Tensor,
            mu: torch.Tensor,
            sample: pde_loss_evaluation,
            sample_bc: pde_loss_evaluation_bc,
        ) -> torch.Tensor:
            # sample.x_sensor.size() [N_batches, dim_x, n_sensor]
            # sample.f_sensor.size() [N_batches, dim_f, n_sensor]
            # So the output tensor will have the size [N_batches, 1, n_sensor]
            # which need to be squeezed down to 2 dimensions before being passed
            # to the decoder
            z = self.forward_encoder(
                sample.x_sensor,
                sample_bc.x_sensor_bc,
                sample.f_sensor,
                sample_bc.f_sensor_bc,
            )

            return self.forward_decoder(x, mu, z)

    return DeepONetSpace(**kwargs)
