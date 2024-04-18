import copy
from typing import Callable

import torch
from torch import nn
from torch.autograd import grad

from ..equations.domain import SpaceTensor
from ..nets import mlp, rbfnet


def identity_tx(t, x, mu, w):
    return w


class PINNtx(nn.Module):
    def __init__(self, net, pde, init_net_bool=False):
        super().__init__()
        self.net = net
        self.nb_unknowns = pde.nb_unknowns
        self.nb_parameters = pde.nb_parameters
        self.pde_dimension_x = pde.dimension_x
        self.init_net_bool = init_net_bool

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity_tx

        if self.init_net_bool:
            self.net0 = copy.deepcopy(self.net)

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        return self.net.forward(t, x, mu)

    def get_w(
        self, t: torch.Tensor, data: SpaceTensor, mu: torch.Tensor
    ) -> torch.Tensor:
        x = data.x
        if self.init_net_bool:
            w = self(t, x, mu) - self.net0.forward(0 * t, x, mu)  # put t at zeo
        else:
            w = self(t, x, mu)
        wp = self.post_processing(t, data, mu, w)
        return wp

    def setup_w_dict(
        self, t: torch.Tensor, data: SpaceTensor, mu: torch.Tensor
    ) -> dict:
        return {
            "w": self.get_w(t, data, mu),
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

        ones = torch.ones_like(w["w"][:, 0, None])
        x = data.x
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

    def get_first_derivatives_t(self, w: dict, t: torch.Tensor):
        ones = torch.ones_like(t)
        w["w_t"] = torch.cat(
            [
                grad(w["w"][:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_first_derivatives_x(self, w: dict, data: SpaceTensor):
        ones = torch.ones_like(w["w"][:, 0, None])
        x = data.x

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
        ones = torch.ones_like(w["w_x"][:, 0, None])
        x = data.x

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

    def get_first_derivatives_f_t(
        self,
        w: dict,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[
            [torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
        ],
    ):
        ones = torch.ones_like(t)

        w["f_w_t"] = torch.cat(
            [
                grad(f(w, t, data, mu)[:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_second_derivatives_f_t(
        self,
        w: dict,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[
            [torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
        ],
    ):
        ones = torch.ones_like(t)

        f_w_t = torch.cat(
            [
                grad(f(w, t, data, mu)[:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

        w["f_w_tt"] = torch.cat(
            [
                grad(f_w_t[:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_first_derivatives_f_x(
        self,
        w: dict,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[
            [torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
        ],
        dim: str,
    ):
        """
        Compute the first derivatives of f(w) with respect to x.

        Args:
            w: dictionary containing the solution w
            t: tensor of batched time coordinates
            x: tensor of batched space coordinates
            mu: tensor of batched parameters
            f: function f to be applied to w
            dim: "x" or "y", the dimension with respect to which the derivative is taken
        """
        possible_dims = ["x", "y"]
        assert (
            dim in possible_dims
        ), f"in get_first_derivatives_f, dim must be 'x' or 'y', got {dim}"

        ones = torch.ones_like(w["w"][:, 0, None])
        x = data.x

        first_derivatives = torch.cat(
            [
                grad(f(w, t, data, mu)[:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if dim == "x":
            if self.pde_dimension_x == 1:
                w["f_w_x"] = first_derivatives.reshape(shape).T
            elif self.pde_dimension_x == 2:
                w["f_w_x"] = first_derivatives[0].reshape(shape).T
        elif dim == "y":
            assert self.pde_dimension_x > 1, "dim == 'y' but pde_dimension_x < 2"
            w["f_w_y"] = first_derivatives[1].reshape(shape).T

    def get_second_derivatives_f_x(
        self,
        w: dict,
        t: torch.Tensor,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[
            [torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
        ],
        dim: str,
    ):
        """
        Compute the second derivatives of f(w) with respect to x.

        Args:
            w: dictionary containing the solution w
            t: tensor of batched time coordinates
            x: tensor of batched space coordinates
            mu: tensor of batched parameters
            f: function f to be applied to w
            dim: "x" or "y", the dimension with respect to which the derivative is taken
        """
        possible_dims = ["xx", "xy", "yy"]
        assert (
            dim in possible_dims
        ), f"in get_first_derivatives_f, dim must be 'x' or 'y', got {dim}"

        ones = torch.ones_like(w["w"][:, 0, None])
        x = data.x

        first_derivatives = torch.cat(
            [
                grad(f(w, t, data, mu)[:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if "x" in dim:
            if self.pde_dimension_x == 1:
                f_w_x = first_derivatives.reshape(shape).T
            elif self.pde_dimension_x == 2:
                f_w_x = first_derivatives[0].reshape(shape).T
        elif dim == "yy":
            assert self.pde_dimension_x > 1, "dim == 'yy' but pde_dimension_x < 2"
            f_w_y = first_derivatives[1].reshape(shape).T

        if "x" in dim:
            second_derivatives = torch.cat(
                [
                    grad(f_w_x[:, i, None], x, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            if self.pde_dimension_x == 1 and dim == "xx":
                w["f_w_xx"] = second_derivatives.reshape(shape).T
            elif self.pde_dimension_x == 2:
                if dim == "xx":
                    w["f_w_xx"] = second_derivatives[0].reshape(shape).T
                elif dim == "xy":
                    w["f_w_xy"] = second_derivatives[1].reshape(shape).T

        elif dim == "yy":
            second_derivatives = torch.cat(
                [
                    grad(f_w_y[:, i, None], x, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            w["f_w_yy"] = second_derivatives[1].reshape(shape).T


class MLP_tx(nn.Module):
    def __init__(self, pde, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, mu], axis=1)
        return self.net.forward(inputs)


class DisMLP_tx(nn.Module):
    def __init__(self, pde, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, mu], axis=1)
        return self.net.forward(inputs)


class RBFNet_tx(nn.Module):
    def __init__(self, pde, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = rbfnet.RBFLayer(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, mu], axis=1)
        return self.net.forward(inputs)


class Fourier_tx(nn.Module):
    def __init__(self, pde, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.list_type_features = kwargs.get(
            "list_type_features", {"x": True, "t": False, "tx": False, "mu": False}
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        de_inputs_size = 1 + pde.dimension_x + pde.nb_parameters
        if self.list_type_features["t"]:
            self.features_t = mlp.EnhancedFeatureNet(in_size=1, **kwargs)
            de_inputs_size = de_inputs_size + self.features_t.enhanced_dim
        if self.list_type_features["x"]:
            self.features_x = mlp.EnhancedFeatureNet(in_size=pde.dimension_x, **kwargs)
            de_inputs_size = de_inputs_size + self.features_x.enhanced_dim
        if self.list_type_features["tx"]:
            self.features_tx = mlp.EnhancedFeatureNet(
                in_size=1 + pde.dimension_x, **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_tx.enhanced_dim
        if self.list_type_features["mu"]:
            self.features_mu = mlp.EnhancedFeatureNet(
                in_size=pde.nb_parameters, **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_mu.enhanced_dim

        self.inputs_size = kwargs.get("inputs_size", de_inputs_size)
        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        full_features = torch.zeros((t.shape[0], 0))
        if self.list_type_features["t"]:
            features = self.features_t.forward(t)
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["x"]:
            features = self.features_x.forward(x)
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["tx"]:
            features = self.features_tx.forward(torch.cat([t, x], axis=1))
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["mu"]:
            features = self.features_mu.forward(mu)
            full_features = torch.cat([features, full_features], axis=1)

        inputs = torch.cat([t, x, mu, full_features], axis=1)
        return self.net.forward(inputs)
