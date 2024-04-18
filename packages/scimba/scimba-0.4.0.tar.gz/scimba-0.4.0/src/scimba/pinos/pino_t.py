import torch
from torch import nn
from torch.autograd import grad as grad

from scimba.sampling.data_sampling_ode import ode_loss_evaluation


def identity(t, mu, w):
    return w


class PINOt(nn.Module):

    """
    Create the class temporal PINO which take type of Network and create the
    final model using the ODE parameters
    """

    def __init__(self, no_net, ode, **kwargs):
        super().__init__()
        self.inputs_size = 1 + ode.nb_parameters

        self.nb_unknowns = ode.nb_unknowns
        self.nb_parameters = ode.nb_parameters
        self.outputs_size = kwargs.get("outputs_size", self.nb_unknowns)

        self.no_net = no_net
        self.varying_sizes = no_net.varying_sizes

        try:
            self.post_processing = ode.post_processing
        except AttributeError:
            self.post_processing = identity

    def forward(
        self, t: torch.Tensor, mu: torch.Tensor, sample: ode_loss_evaluation
    ) -> torch.Tensor:
        return self.no_net.forward(t, mu, sample)

    def get_w(
        self, t: torch.Tensor, mu: torch.Tensor, sample: ode_loss_evaluation
    ) -> torch.Tensor:
        w = self(t, mu, sample)
        return self.post_processing(sample.t_loss, sample.params, w)

    def setup_w_dict(
        self, t: torch.Tensor, mu: torch.Tensor, sample: ode_loss_evaluation
    ) -> dict:
        return {
            "w": self.get_w(t, mu, sample),
            "w_t": None,
            "w_tt": None,
        }

    def get_first_derivatives(self, w: dict, t: torch.Tensor):
        ones = torch.ones_like(t)
        w["w_t"] = torch.cat(
            [
                grad(w["w"][:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_first_derivatives_wrt_mu(self, w: dict, mu: torch.Tensor):
        ones = torch.ones_like(w["w"][:, 0, None])

        first_derivatives = torch.cat(
            [
                grad(w["w"][:, i, None], mu, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, mu.shape[0])

        if self.nb_parameters == 1:
            w["w_mu_1"] = first_derivatives.reshape(shape).T
        elif self.nb_parameters == 2:
            for i in range(self.nb_parameters):
                w[f"w_mu_{i + 1}"] = first_derivatives[i].reshape(shape).T

    def get_second_derivatives(self, w: dict, t: torch.Tensor):
        w["w_tt"] = torch.cat(
            [
                grad(
                    w["w_t"][:, i, None],
                    t,
                    torch.ones_like(t),
                    create_graph=True,
                )[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )
