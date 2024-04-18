import copy

import torch
from torch import nn
from torch.autograd import grad

from ..equations import pdes
from ..equations.domain import SpaceTensor
from ..nets import mlp, rbfnet
from ..sampling import sampling_pde_txv


def identity_xv(x, v, mu, w):
    return w


class PINNxv(nn.Module):
    def __init__(self, net, pde: pdes.AbstractPDExv, **kwargs):
        super().__init__()
        self.net = net
        self.nb_unknowns = pde.nb_unknowns
        self.nb_parameters = pde.nb_parameters
        self.pde_dimension_x = pde.dimension_x
        self.pde_dimension_v = pde.dimension_v
        self.init_net_bool = kwargs.get("init_net_bool", False)
        self.moment_sampler = kwargs.get(
            "moment_sampler", sampling_pde_txv.VSampler(pde)
        )

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity_xv

        if self.init_net_bool:
            self.net0 = copy.deepcopy(self.net)

    def forward(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        return self.net.forward(x, v, mu)

    def get_w(
        self, data: SpaceTensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        x = data.get_coordinates()
        if self.init_net_bool:
            w = self(x, v, mu) - self.net0.forward(x, v, mu)  ### put t at zeo

        else:
            w = self(x, v, mu)
        wp = self.post_processing(data, v, mu, w)
        return wp

    def get_moments(
        self, x: torch.Tensor, mu: torch.Tensor, index: list
    ) -> torch.Tensor:
        # todo
        pass

    def setup_w_dict(
        self, data: SpaceTensor, v: torch.Tensor, mu: torch.Tensor
    ) -> dict:
        return {
            "w": self.get_w(data, v, mu),
            "w_x": None,
            "w_y": None,
            "w_xx": None,
            "w_yy": None,
            "w_v1": None,
            "w_v2": None,
            "w_v1v1": None,
            "w_v2v2": None,
        }

    def get_first_derivatives_x(self, w: torch.Tensor, data: SpaceTensor):
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
                "PDE dimension > 2 not yet implemented in Trainer.get_first_derivatives"
            )

    def get_first_derivatives_v(self, w: torch.Tensor, v: torch.Tensor):
        ones = torch.ones_like(w["w"][:, 0, None])

        first_derivatives = torch.cat(
            [
                grad(w["w"][:, i, None], v, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, v.shape[0])

        if self.pde_dimension_v == 1:
            w["w_v1"] = first_derivatives.reshape(shape).T
        elif self.pde_dimension_v == 2:
            w["w_v1"] = first_derivatives[0].reshape(shape).T
            w["w_v2"] = first_derivatives[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 not yet implemented in Trainer.get_first_derivatives"
            )

    def get_second_derivatives_x(self, w: torch.Tensor, data: SpaceTensor):
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
                "PDE dimension > 2 not yet implemented in Trainer.get_second_derivatives"
            )

    def get_second_derivatives_v(self, w: torch.Tensor, v: torch.Tensor):
        ones = torch.ones_like(w["w_v1"][:, 0, None])

        second_derivatives_v1 = torch.cat(
            [
                grad(w["w_v1"][:, i, None], v, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, v.shape[0])

        if self.pde_dimension_v == 1:
            w["w_v1v1"] = second_derivatives_v1.reshape(shape).T
        elif self.pde_dimension_v == 2:
            w["w_v1v1"] = second_derivatives_v1[0].reshape(shape).T
            w["w_v1v2"] = second_derivatives_v1[1].reshape(shape).T

            second_derivatives_v2 = torch.cat(
                [
                    grad(w["w_v2"][:, i, None], v, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            w["w_v2v2"] = second_derivatives_v2[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 not yet implemented in Trainer.get_second_derivatives"
            )


class MLP_xv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDExv, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([x, v, mu], axis=1)
        return self.net.forward(inputs)


class DisMLP_xv(nn.Module):
    def __init__(self, pde, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([x, v, mu], axis=1)
        return self.net.forward(inputs)


class RBFNet_xv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDExv, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = rbfnet.RBFLayer(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([x, v, mu], axis=1)
        return self.net.forward(inputs)
