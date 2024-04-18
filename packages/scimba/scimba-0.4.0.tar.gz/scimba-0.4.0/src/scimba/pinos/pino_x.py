import torch
from torch import nn
from torch.autograd import grad

from ..equations import pdes
from ..equations.domain import SpaceTensor
from ..sampling.data_sampling_pde_x import (
    pde_loss_evaluation,
    pde_loss_evaluation_bc,
)


def identity(x, mu, w):
    return w


class PINOx(nn.Module):
    """
    create Class spatial PINO which take type of Network and create the final
    model using the PDE parameters
    """

    def __init__(self, no_net, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()

        self.init_net_bool = kwargs.get("init_net_bool", False)
        self.nb_unknowns = pde.nb_unknowns
        self.nb_parameters = pde.nb_parameters
        self.pde_dimension_x = pde.dimension_x
        self.dim = pde.dimension_x + pde.nb_parameters
        self.inputs_size = self.dim
        self.outputs_size = kwargs.get("outputs_size", self.nb_unknowns)

        self.no_net = no_net
        self.varying_sizes = no_net.varying_sizes

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity

    def forward(
        self,
        x: torch.Tensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
    ) -> torch.Tensor:
        return self.no_net.forward(x, mu, sample, sample_bc)

    def get_w(
        self,
        data: SpaceTensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
    ) -> torch.Tensor:
        x = data.x
        w = self(x, mu, sample, sample_bc)
        return self.post_processing(data, mu, w)

    def setup_w_dict(
        self,
        data: SpaceTensor,
        mu: torch.Tensor,
        sample: pde_loss_evaluation,
        sample_bc: pde_loss_evaluation_bc,
    ) -> dict:
        return {
            "w": self.get_w(data, mu, sample, sample_bc),
            "w_x": None,
            "w_y": None,
            "w_xx": None,
            "w_yy": None,
        }

    def get_first_derivatives(self, w: dict, data: SpaceTensor):
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
                "PDE dimension > 2 not implemented in PINNx.get_first_derivatives"
            )

    def get_second_derivatives(self, w: dict, data: SpaceTensor):
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
            w["w_xy"] = second_derivatives_x[1].reshape(shape).T

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
                "PDE dimension > 2 not implemented in PINNx.get_second_derivatives"
            )

    def get_first_derivatives_mu(self, w: dict, mu: torch.Tensor):
        ones = torch.ones_like(mu[:, 0, None])

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
        elif self.nb_parameters >= 2:
            for i in range(self.nb_parameters):
                w[f"w_mu_{i + 1}"] = first_derivatives[i].reshape(shape).T

    def get_second_derivatives_xmu(self, w: dict, data: SpaceTensor, mu: torch.Tensor):
        x = data.x
        ones = torch.ones_like(w["w_x"][:, 0, None])

        second_derivatives_xmu = torch.cat(
            [
                grad(w["w_x"][:, i, None], mu, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_x == 1:
            if self.nb_parameters == 1:
                w["w_x_mu1"] = second_derivatives_xmu.reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_x_mu{i + 1}"] = second_derivatives_xmu[i].reshape(shape).T

        elif self.pde_dimension_x == 2:
            if self.nb_parameters == 1:
                w["w_x_mu1"] = second_derivatives_xmu.reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_x_mu{i + 1}"] = second_derivatives_xmu[i].reshape(shape).T

            second_derivatives_ymu = torch.cat(
                [
                    grad(w["w_y"][:, i, None], mu, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            if self.nb_parameters == 1:
                w["w_y_mu1"] = second_derivatives_ymu[1].reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_x_mu{i + 1}"] = second_derivatives_ymu[1][i].reshape(shape).T

        else:
            raise NotImplementedError(
                "PDE dimension > 2 not implemented in PINNx.get_second_derivatives"
            )
