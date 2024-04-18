import torch
from torch import nn
from torch.autograd import grad

from ..equations.domain import SpaceTensor
from ..sampling.data_sampling_pde_tx import (
    pde_loss_evaluation,
    pde_loss_evaluation_bc,
    pde_loss_evaluation_ini,
)


def identity_tx(t, x, mu, w):
    return w


class PINOtx(nn.Module):
    """
    Class spatial-temporal PINN which take type of Network and create the
    final model using the PDE parameters
    """

    def __init__(self, no_net, pde, **kwargs):
        super().__init__()

        self.ff = kwargs.get("ff", 0)  # number of fourier features
        self.ff_freq = kwargs.get("ff_freq", 30)
        self.ff_params = kwargs.get("ff_params", False)
        self.nb_unknowns = pde.nb_unknowns
        self.pde_dimension_x = pde.dimension_x
        self.dim = 1 + pde.dimension_x + pde.nb_parameters
        self.inputs_size = kwargs.get("inputs_size ", self.dim + self.ff)
        self.outputs_size = kwargs.get("outputs_size", self.nb_unknowns)

        self.no_net = no_net
        self.varying_sizes = no_net.varying_sizes

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity_tx

    def forward(
        self,
        t: torch.Tensor,
        x: torch.Tensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
        sample_ini: pde_loss_evaluation_ini,
    ) -> torch.Tensor:
        return self.no_net.forward(t, x, mu, sample, sample_bc, sample_ini)

    def get_w(
        self,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
        sample_ini: pde_loss_evaluation_ini,
    ) -> torch.Tensor:
        x = data.x
        w = self(t, x, mu, sample, sample_bc, sample_ini)
        return self.post_processing(t, data, mu, w)

    def setup_w_dict(
        self,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
        sample_ini: pde_loss_evaluation_ini,
    ) -> dict:
        return {
            "w": self.get_w(t, data, mu, sample, sample_bc, sample_ini),
            "w_t": None,
            "w_tt": None,
            "w_x": None,
            "w_y": None,
            "w_xx": None,
            "w_yy": None,
        }

    def get_first_derivatives(self, w: dict, t: torch.Tensor, data: SpaceTensor):
        ones = torch.ones_like(t)
        w["w_t"] = torch.cat(
            [
                grad(w["w"][:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

        x = data.x
        ones = torch.ones_like(w["w"][:, 0, None])
        first_derivatives = torch.cat(
            [
                grad(w["w"][:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_x == 1:
            w["w_x"] = first_derivatives.reshape(shape).T
        elif self.pde_dimension_x == 2:
            w["w_x"] = first_derivatives[0].reshape(shape).T
            w["w_y"] = first_derivatives[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 unavailable in PINNtx.get_first_derivatives"
            )

    def get_first_derivatives_x(self, w: dict, data: SpaceTensor):
        x = data.x
        ones = torch.ones_like(w["w"][:, 0, None])
        first_derivatives = torch.cat(
            [
                grad(w["w"][:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_x == 1:
            w["w_x"] = first_derivatives.reshape(shape).T
        elif self.pde_dimension_x == 2:
            w["w_x"] = first_derivatives[0].reshape(shape).T
            w["w_y"] = first_derivatives[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 unavailable in PINNtx.get_first_derivatives_x"
            )

    def get_second_derivatives_t(self, w: dict, t: torch.Tensor):
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

    def get_second_derivatives_x(self, w: dict, data: SpaceTensor):
        x = data.x
        ones = torch.ones_like(w["w_x"][:, 0, None])

        second_derivatives_x = torch.cat(
            [
                grad(w["w_x"][:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_x == 1:
            w["w_xx"] = second_derivatives_x.reshape(shape).T
        elif self.pde_dimension_x == 2:
            w["w_xx"] = second_derivatives_x[0].reshape(shape).T

            second_derivatives_y = torch.cat(
                [
                    grad(w["w_y"][:, i, None], x, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            w["w_yy"] = second_derivatives_y[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 unavailable in PINNtx.get_second_derivatives_x"
            )
