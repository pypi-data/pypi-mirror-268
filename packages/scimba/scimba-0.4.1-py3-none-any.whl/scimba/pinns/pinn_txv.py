import copy

import torch
from torch import nn
from torch.autograd import grad

from ..equations import pdes
from ..equations.domain import SpaceTensor
from ..nets import activation, mlp, rbfnet


def identity_txv(t, x, v, mu, w):
    return w


class PINNtxv(nn.Module):
    def __init__(self, net, pde: pdes.AbstractPDEtxv, **kwargs):
        super().__init__()
        self.net = net
        self.nb_unknowns = pde.nb_unknowns
        self.nb_parameters = pde.nb_parameters
        self.pde_dimension_x = pde.dimension_x
        self.pde_dimension_v = pde.dimension_v
        self.init_net_bool = kwargs.get("init_net_bool", False)

        try:
            self.post_processing = pde.post_processing
        except AttributeError:
            self.post_processing = identity_txv

        if self.init_net_bool:
            self.net0 = copy.deepcopy(self.net)

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        return self.net.forward(t, x, v, mu)

    def get_w(
        self, t: torch.Tensor, data: SpaceTensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        x = data.x
        if self.init_net_bool:
            w = self(t, x, v, mu) - self.net0.forward(t, x, v, mu)  ### put t at zeo
        else:
            w = self(t, x, v, mu)
        wp = self.post_processing(t, data, v, mu, w)
        return wp

    def get_moments(
        self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor, index: list
    ) -> torch.Tensor:
        # todo
        pass

    def setup_w_dict(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> dict:
        return {
            "w": self.get_w(t, x, v, mu),
            "w_t": None,
            "w_x": None,
            "w_y": None,
            "w_v1": None,
            "w_v2": None,
        }

    def get_first_derivatives(
        self, w: dict, t: torch.Tensor, data: SpaceTensor, v: torch.Tensor
    ):
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
        first_derivatives_x = torch.cat(
            [
                grad(w["w"][:, i, None], x, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_x == 1:
            w["w_x"] = first_derivatives_x.reshape(shape).T
        elif self.pde_dimension_x == 2:
            w["w_x"] = first_derivatives_x[0].reshape(shape).T
            w["w_y"] = first_derivatives_x[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 not yet implemented in Trainer.get_first_derivatives"
            )

        ones = torch.ones_like(w["w"][:, 0, None])
        first_derivatives_v = torch.cat(
            [
                grad(w["w"][:, i, None], v, ones, create_graph=True)[0].T
                for i in range(self.nb_unknowns)
            ],
            axis=-1,
        )

        shape = (self.nb_unknowns, x.shape[0])

        if self.pde_dimension_v == 1:
            w["w_v1"] = first_derivatives_v.reshape(shape).T
        elif self.pde_dimension_v == 2:
            w["w_v1"] = first_derivatives_v[0].reshape(shape).T
            w["w_v2"] = first_derivatives_v[1].reshape(shape).T
        else:
            raise NotImplementedError(
                "PDE dimension > 2 not yet implemented in Trainer.get_first_derivatives"
            )


class MLP_txv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEtxv, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, v, mu], axis=1)
        return self.net.forward(inputs)


class DisMLP_txv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEtxv, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, v, mu], axis=1)
        return self.net.forward(inputs)


class RBFNet_txv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEtxv, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get(
            "inputs_size", 1 + pde.dimension_x + pde.dimension_v + pde.nb_parameters
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        self.net = rbfnet.RBFLayer(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        inputs = torch.cat([t, x, v, mu], axis=1)
        return self.net.forward(inputs)


class Fourier_txv(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEtxv, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.list_type_features = kwargs.get(
            "list_type_features",
            {
                "x": True,
                "v": True,
                "xv": True,
                "t": False,
                "tx": False,
                "tv": False,
                "txv": False,
                "mu": False,
            },
        )
        self.std_features = kwargs.get(
            "std_features",
            {
                "x": 1.0,
                "v": 1.0,
                "xv": 0.0,
                "t": 0.0,
                "tx": 0.0,
                "tv": 0.0,
                "txv": 0.0,
                "mu": 0.0,
            },
        )
        self.outputs_size = kwargs.get("outputs_size", pde.nb_unknowns)

        de_inputs_size = 1 + pde.dimension_x + pde.dimension_v + pde.nb_parameters
        if self.list_type_features["t"]:
            self.features_t = mlp.EnhancedFeatureNet(
                in_size=1, std=self.std_features["t"], **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_t.enhanced_dim
        if self.list_type_features["x"]:
            self.features_x = mlp.EnhancedFeatureNet(
                in_size=pde.dimension_x, std=self.std_features["x"], **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_x.enhanced_dim
        if self.list_type_features["v"]:
            self.features_v = mlp.EnhancedFeatureNet(
                in_size=pde.dimension_v, std=self.std_features["v"], **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_v.enhanced_dim
        if self.list_type_features["tx"]:
            self.features_tx = mlp.EnhancedFeatureNet(
                in_size=1 + pde.dimension_x, std=self.std_features["tx"], **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_tx.enhanced_dim
        if self.list_type_features["tv"]:
            self.features_tv = mlp.EnhancedFeatureNet(
                in_size=1 + pde.dimension_v, std=self.std_features["tv"], **kwargs
            )
            de_inputs_size = de_inputs_size + self.features_tv.enhanced_dim
        if self.list_type_features["xv"]:
            self.features_xv = mlp.EnhancedFeatureNet(
                in_size=pde.dimension_x + pde.dimension_v,
                std=self.std_features["xv"],
                **kwargs,
            )
            de_inputs_size = de_inputs_size + self.features_xv.enhanced_dim
        if self.list_type_features["txv"]:
            self.features_txv = mlp.EnhancedFeatureNet(
                in_size=1 + pde.dimension_x + pde.dimension_v,
                std=self.std_features["txv"],
                **kwargs,
            )
            de_inputs_size = de_inputs_size + self.features_txv.enhanced_dim
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
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        full_features = torch.zeros((t.shape[0], 0))
        if self.list_type_features["t"]:
            features = self.features_t.forward(t)
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["x"]:
            features = self.features_x.forward(x)
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["v"]:
            features = self.features_v.forward(v)
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["tx"]:
            features = self.features_tx.forward(torch.cat([t, x], axis=1))
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["tv"]:
            features = self.features_tv.forward(torch.cat([t, v], axis=1))
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["xv"]:
            features = self.features_xv.forward(torch.cat([x, v], axis=1))
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["txv"]:
            features = self.features_txv.forward(torch.cat([t, x, v], axis=1))
            full_features = torch.cat([features, full_features], axis=1)
        if self.list_type_features["mu"]:
            features = self.features_mu.forward(mu)
            full_features = torch.cat([features, full_features], axis=1)

        inputs = torch.cat([t, x, v, mu, full_features], axis=1)
        return self.net.forward(inputs)


def Scalar_MlpXConstantGaussiansV(net, **kwargs):
    class Scalar_MlpXConstantGaussiansV(nn.Module):
        def __init__(self, pde: pdes.AbstractPDEtxv, nb_gaussians: int = 2, **kwargs):
            super().__init__()
            self.dim_x = pde.dimension_x
            self.dim_v = pde.dimension_v
            self.nb_gaussians = nb_gaussians
            self.gaussians = nn.ParameterList(
                [
                    activation.IsotropicRadial(in_size=self.dim_v, **kwargs)
                    for i in range(self.nb_gaussians)
                ]
            )

            self.weights = net(
                in_size=1 + self.dim_x + pde.nb_parameters,
                out_size=self.nb_gaussians,
                **kwargs,
            )

        def forward(
            self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
        ) -> torch.Tensor:
            w = self.weights.forward(torch.cat([t, x, mu], axis=1))
            gaussian_list = self.gaussians[0](v)
            for i in range(1, self.nb_gaussians):
                gaussian_list = torch.cat((gaussian_list, self.gaussians[i](v)), dim=1)
            res = torch.einsum("ij,ij->i", w, gaussian_list)
            return res[:, None]

    return Scalar_MlpXConstantGaussiansV(**kwargs)


class MultiScaleMlpConstantGaussiansV(nn.Module):
    def __init__(self, pde: pdes.AbstractPDEtxv, nb_gaussians: int = 2, **kwargs):
        super().__init__()
        self.dim_x = pde.dimension_x
        self.dim_v = pde.dimension_v
        self.nb_gaussians = nb_gaussians
        self.gaussians = nn.ParameterList(
            [
                activation.IsotropicRadial(in_size=self.dim_v, **kwargs)
                for i in range(self.nb_gaussians)
            ]
        )
        self.nb_features = kwargs.get("nb_features", 1)

        self.features_v = mlp.EnhancedFeatureNet(
            in_size=1 + pde.dimension_v + pde.dimension_x, **kwargs
        )
        inputs_size = (
            1
            + pde.dimension_x
            + pde.dimension_v
            + pde.nb_parameters
            + self.features_v.enhanced_dim
        )
        self.weights = mlp.GenericMLP(
            in_size=inputs_size, out_size=self.nb_gaussians, **kwargs
        )

    def forward(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        features = self.features_v.forward(torch.cat([t, x, v], axis=1))
        w = self.weights.forward(torch.cat([t, x, v, features, mu], axis=1))
        gaussian_list = self.gaussians[0](v)
        for i in range(1, self.nb_gaussians):
            gaussian_list = torch.cat((gaussian_list, self.gaussians[i](v)), dim=1)
        res = torch.einsum("ij,ij->i", w, gaussian_list)
        return res[:, None]
