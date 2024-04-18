import copy
from typing import Callable, List

import torch
from torch import nn
from torch.autograd import grad

from ..equations import pdes
from ..equations.domain import SpaceTensor
from ..nets import mlp, rbfnet, siren


def identity(x, mu, w):
    return w


class PINNx(nn.Module):
    def __init__(self, net, pde: pdes.AbstractPDEx, init_net_bool=False):
        super().__init__()
        self.net = net
        self.nb_unknowns = pde.nb_unknowns
        self.nb_parameters = pde.nb_parameters
        self.pde_dimension_x = pde.dimension_x
        self.init_net_bool = init_net_bool

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity

        if self.init_net_bool is True:
            self.net0 = copy.deepcopy(self.net)

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        return self.net.forward(x, mu)

    def get_w(self, data: SpaceTensor, mu: torch.Tensor) -> torch.Tensor:
        x = data.x
        if self.init_net_bool is True:
            w = self(x, mu) - self.net0.forward(x, mu)
        else:
            w = self(x, mu)
        wp = self.post_processing(data, mu, w)
        return wp

    def setup_w_dict(self, x: SpaceTensor, mu: torch.Tensor) -> dict:
        return {
            "w": self.get_w(x, mu),
            "w_x": None,
            "w_y": None,
            "w_xx": None,
            "w_yy": None,
            "labels": x.labels,
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
            w["w_mu1"] = first_derivatives.reshape(shape).T
        elif self.nb_parameters >= 2:
            for i in range(self.nb_parameters):
                w[f"w_mu{i + 1}"] = first_derivatives[i].reshape(shape).T

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
                w["w_xmu1"] = second_derivatives_xmu.reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_xmu{i + 1}"] = second_derivatives_xmu[i].reshape(shape).T
        elif self.pde_dimension_x == 2:
            if self.nb_parameters == 1:
                w["w_xmu1"] = second_derivatives_xmu.reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_xmu{i + 1}"] = second_derivatives_xmu[i].reshape(shape).T

            second_derivatives_ymu = torch.cat(
                [
                    grad(w["w_y"][:, i, None], mu, ones, create_graph=True)[0].T
                    for i in range(self.nb_unknowns)
                ],
                axis=-1,
            )

            if self.nb_parameters == 1:
                w["w_ymu1"] = second_derivatives_ymu.reshape(shape).T
            elif self.nb_parameters >= 2:
                for i in range(self.nb_parameters):
                    w[f"w_ymu{i + 1}"] = second_derivatives_ymu[i].reshape(shape).T

        else:
            raise NotImplementedError(
                "PDE dimension > 2 not implemented in PINNx.get_second_derivatives"
            )

    def get_first_derivatives_f(
        self,
        w: dict,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[[torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor],
        dim: str,
    ):
        """
        Compute the first derivatives of f(w) with respect to x.

        Args:
            w: dictionary containing the solution w
            x: tensor of batched space coordinates
            mu: tensor of batched parameters
            f: function f to be applied to w
            dim: "x" or "y", the dimension with respect to which the derivative is taken
        """
        possible_dims = ["x", "y"]
        assert (
            dim in possible_dims
        ), f"in get_first_derivatives_f, dim must be 'x' or 'y', got {dim}"

        x = data.x
        ones = torch.ones_like(w["w"][:, 0, None])

        first_derivatives = torch.cat(
            [
                grad(f(w, data, mu)[:, i, None], x, ones, create_graph=True)[0].T
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

    def get_second_derivatives_f(
        self,
        w: dict,
        data: SpaceTensor,
        mu: torch.Tensor,
        f: Callable[[torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor],
        dim: str,
    ):
        """
        Compute the second derivatives of f(w) with respect to x.

        Args:
            w: dictionary containing the solution w
            x: tensor of batched space coordinates
            mu: tensor of batched parameters
            f: function f to be applied to w
            dim: "x" or "y", the dimension with respect to which the derivative is taken
        """
        possible_dims = ["xx", "xy", "yy"]
        assert (
            dim in possible_dims
        ), f"in get_first_derivatives_f, dim must be 'x' or 'y', got {dim}"

        x = data.x
        ones = torch.ones_like(w["w"][:, 0, None])

        first_derivatives = torch.cat(
            [
                grad(f(w, data, mu)[:, i, None], x, ones, create_graph=True)[0].T
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

    def get_div_K_grad_w(
        self,
        w: dict,
        data: SpaceTensor,
        mu: torch.Tensor,
        anisotropy_matrix: Callable[
            [torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor
        ],
    ):
        """
        Compute the second derivatives of f(w) with respect to x.

        Args:
            w: dictionary containing the solution w
            x: tensor of batched space coordinates
            mu: tensor of batched parameters
            f: function f to be applied to w
        """
        assert self.pde_dimension_x == 2, "get_div_K_grad_w only implemented for 2D"

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

        w_x = first_derivatives[0].reshape(shape).T
        w_y = first_derivatives[1].reshape(shape).T

        grad_w = torch.cat([w_x, w_y], axis=1)

        K = anisotropy_matrix(w, data, mu).reshape((-1, 2, 2))
        K_grad_w = torch.einsum("bij,bj->bi", K, grad_w)
        K_grad_w_1 = K_grad_w[:, 0, None]
        K_grad_w_2 = K_grad_w[:, 1, None]

        second_derivatives_x = torch.cat(
            [
                grad(K_grad_w_1[:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        second_derivatives_y = torch.cat(
            [
                grad(K_grad_w_2[:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        div_K_grad_w_1 = second_derivatives_x[0].reshape(shape).T
        div_K_grad_w_2 = second_derivatives_y[1].reshape(shape).T

        w["div_K_grad_w"] = div_K_grad_w_1 + div_K_grad_w_2


class MLP_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        inputs = torch.cat([x, mu], axis=1)
        return self.net.forward(inputs)


class DisMLP_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        inputs = torch.cat([x, mu], axis=1)
        return self.net.forward(inputs)


class RBFNet_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.inputs_size = self.inputs_size = kwargs.get(
            "inputs_size", pde.dimension_x + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = rbfnet.RBFLayer(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        inputs = torch.cat([x, mu], axis=1)
        return self.net.forward(inputs)


class Fourier_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.bool_feature_mu = kwargs.get("feature_mu", False)
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.features_x = mlp.EnhancedFeatureNet(in_size=pde.dimension_x, **kwargs)
        self.inputs_size = kwargs.get(
            "inputs_size",
            pde.dimension_x + pde.nb_parameters + self.features_x.enhanced_dim,
        )
        if self.bool_feature_mu is True:
            self.features_mu = mlp.EnhancedFeatureNet(
                in_size=pde.nb_parameters, **kwargs
            )
            self.inputs_size = self.inputs_size + self.features_mu.enhanced_dim

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        features = self.features_x.forward(x)
        if self.bool_feature_mu:
            features = torch.cat([self.features_mu.forward(mu), features], axis=1)

        inputs = torch.cat([x, mu, features], axis=1)
        return self.net.forward(inputs)


class DisFourier_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.bool_feature_mu = kwargs.get("feature_mu", False)
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.features_x = mlp.EnhancedFeatureNet(in_size=pde.dimension_x, **kwargs)
        self.inputs_size = kwargs.get(
            "inputs_size",
            pde.dimension_x + pde.nb_parameters + self.features_x.enhanced_dim,
        )
        if self.bool_feature_mu is True:
            self.features_mu = mlp.EnhancedFeatureNet(
                in_size=pde.nb_parameters, **kwargs
            )
            self.inputs_size = self.inputs_size + self.features_mu.enhanced_dim

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        features = self.features_x.forward(x)
        if self.bool_feature_mu:
            features = torch.cat([self.features_mu.forward(mu), features], axis=1)

        inputs = torch.cat([x, mu, features], axis=1)
        return self.net.forward(inputs)


class ModFourier_x:
    pass


class HighwayFourier_x:
    pass


class MultiScale_Fourier_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, stds: List[float], **kwargs):
        super().__init__()
        self.pde = pde
        self.output_size = pde.nb_unknowns
        self.stds = stds
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.Ws = [
            torch.normal(0.0, std, size=(self.pde.dimension_x, self.nb_features))
            for std in self.stds
        ]
        self.mods = []
        for std in self.stds:
            self.mods.append(
                mlp.EnhancedFeatureNet(in_size=pde.dimension_x, std=std, **kwargs)
            )
        self.mods = nn.ModuleList(self.mods)

        self.nets = []
        for std in self.stds:
            self.nets.append(
                mlp.GenericMLP(
                    2 * self.nb_features + pde.nb_parameters,
                    out_size=self.outputs_size,
                    **kwargs,
                )
            )
        self.nets = nn.ModuleList(self.nets)

        self.last_layer = nn.Linear(
            len(self.stds) * self.outputs_size, self.output_size
        )

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        H = []
        for mod, net in zip(self.mods[0:], self.nets[0:]):
            H.append(net.forward(torch.cat([mod.forward(x), mu], axis=1)))
        H = torch.cat(H, axis=1)
        return self.last_layer.forward(H)


class Siren_x(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEx, **kwargs):
        super().__init__()
        self.in_size = pde.dimension_x + pde.nb_parameters
        self.out_size = pde.nb_unknowns

        self.net = siren.SirenNet(self.in_size, self.out_size, **kwargs)

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        y = torch.cat([x, mu], axis=1)
        return self.net.forward(y)


class DGM_x:
    pass
