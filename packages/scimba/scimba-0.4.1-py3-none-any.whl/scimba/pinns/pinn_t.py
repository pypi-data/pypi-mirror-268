from typing import Callable

import torch
from torch import nn
from torch.autograd import grad as grad

from ..equations import pdes
from ..nets import mlp, rbfnet

def identity(t, mu, w):
    return w


class PINNt(nn.Module):
    """
    class to transform a network with (t,mu) as input in temporal PINNs 

    :param net: the network
    :type in_size: nn.module
    :param ode: the ode solved by the Pinns
    :type ode: pdes.AbstractODE
    """

    def __init__(self, net: nn.Module, ode: pdes.AbstractODE):
        super().__init__()
        self.net = net
        self.nb_unknowns = ode.nb_unknowns
        self.nb_parameters = ode.nb_parameters

        try:
            self.post_processing = ode.post_processing
        except AttributeError:
            self.post_processing = identity

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs (t,mu).

        :param t: time sampled tensor
        :type t: torch.Tensor
        :param mu: parameters sampled tensor
        :type mu: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        return self.net.forward(t, mu)

    def get_w(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Compute the solution w(t,mu) applying the network and the post processing.

        :param t: time sampled tensor
        :type t: torch.Tensor
        :param mu: parameters sampled tensor
        :type mu: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        w = self(t, mu)
        wp = self.post_processing(t, mu, w)
        return wp

    def setup_w_dict(self, t: torch.Tensor, mu: torch.Tensor) -> dict:
        """
        Create a dictionary for w and it derivatives and compute w calling get_w

        :param t: time sampled tensor
        :type t: torch.Tensor
        :param mu: parameters sampled tensor
        :type mu: torch.Tensor
        :return: the dictionary of w and its derivatives at the sampled points
        :rtype: dict
        """
        return {
            "w": self.get_w(t, mu),
            "w_t": None,
            "w_tt": None,
        }

    def get_first_derivatives(self, w: dict, t: torch.Tensor):
        """
        compute the first time deriative of the variables and put in the dictionary

        :param w: the dictionary of the vaiables and its derivatives
        :type w: dict
        :param t: time sampled tensor
        :type t: torch.Tensor
        """
        ones = torch.ones_like(t)
        w["w_t"] = torch.cat(
            [
                grad(w["w"][:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_first_derivatives_wrt_mu(self, w: dict, mu: torch.Tensor):
        """
        compute the first mu deriative of the variables and put in the dictionary

        :param w: the dictionary of the vaiables and its derivatives
        :type w: dict
        :param t: time sampled tensor
        :type t: torch.Tensor
        """
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
        """
        compute the second time deriative of the variables and put in the dictionary

        :param w: the dictionary of the vaiables and its derivatives
        :type w: dict
        :param t: time sampled tensor
        :type t: torch.Tensor
        """
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

    def get_first_derivatives_f(
        self,
        w: dict,
        t: torch.Tensor,
        mu: torch.Tensor,
        f: Callable[[torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor],
    ):
        """
        compute the first time deriative of f(w) and put in the dictionary

        :param w: the dictionary of the vaiables and its derivatives
        :type w: dict
        :param t: time sampled tensor
        :type t: torch.Tensor
        :param mu: mu sampled tensor
        :type mu: torch.Tensor
        :param f: the function for conservative terms
        :type Callable[list(torch.Tensor, torch.Tensor, torch.Tensor), torch.Tensor]
        """
        ones = torch.ones_like(t)

        w["f_w_t"] = torch.cat(
            [
                grad(f(w, t, mu)[:, i, None], t, ones, create_graph=True)[0]
                for i in range(self.nb_unknowns)
            ],
            axis=1,
        )

    def get_second_derivatives_f(
        self,
        w: dict,
        t: torch.Tensor,
        mu: torch.Tensor,
        f: Callable[[torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor],
    ):
        """
        compute the second time deriative of f(w) and put in the dictionary

        :param w: the dictionary of the vaiables and its derivatives
        :type w: dict
        :param t: time sampled tensor
        :type t: torch.Tensor
        :param mu: mu sampled tensor
        :type mu: torch.Tensor
        :param f: the function for conservative terms
        :type Callable[list(torch.Tensor, torch.Tensor, torch.Tensor), torch.Tensor]
        """
        ones = torch.ones_like(t)

        f_w_t = torch.cat(
            [
                grad(f(w, t, mu)[:, i, None], t, ones, create_graph=True)[0]
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


class MLP_t(nn.Module):
    """Class which create a PINNs for ode based on MLP network
     The network is:
     $$
         MLP(t,x ;theta)
     $$

    -----
    Inputs Parameters:
    - ode (AbstractOde): the ode associated to the problem
    - kwargs for the optional parameters

    Optional Parameters
    - inputs_size (int): pby defaut it is 1 (time) + nb_parameters. However we can change it (useful for neural operator).
    - outputs_size (int): pby defaut nb_unknowns of the ODE. However we can change it (useful for neural operator).
    """

    def __init__(self, ode: pdes.AbstractODE, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get("inputs_size", 1 + ode.nb_parameters)
        self.outputs_size = kwargs.get("outputs_size", ode.nb_unknowns)

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Function: Forward of the MLP_t which concatenate t and mu and call the forward of the MLP associated
        -----
        Inputs Parameters:
            - t (tensor): sampled time point
            - mu (tensor): sampled ode parameters point
        """
        inputs = torch.cat([t, mu], axis=1)
        return self.net.forward(inputs)


class DisMLP_t(nn.Module):
    """Class which create a PINNs for ode based on discontinuous MLP network
     The network is:
     $$
         DMLP(t,x ;theta)
     $$

    -----
    Inputs Parameters:
    - ode (AbstractOde): the ode associated to the problem
    - kwargs for the optional parameters

    Optional Parameters
    - inputs_size (int): pby defaut it is 1 (time) + nb_parameters. However we can change it (useful for neural operator).
    - outputs_size (int): pby defaut nb_unknowns of the ODE. However we can change it (useful for neural operator).
    """

    def __init__(self, ode: pdes.AbstractODE, **kwargs):
        super().__init__()
        self.inputs_size = kwargs.get("inputs_size", 1 + ode.nb_parameters)
        self.outputs_size = kwargs.get("outputs_size", ode.nb_unknowns)

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Function: Forward of the discontinuous MLP_t which concatenate t and mu and call the forward of the discontinuous MLP associated
        -----
        Inputs Parameters:
            - t (tensor): sampled time point
            - mu (tensor): sampled ode parameters point
        """
        inputs = torch.cat([t, mu], axis=1)
        return self.net.forward(inputs)


class RBFNet_t(nn.Module):
    def __init__(self, ode: pdes.AbstractODE, **kwargs):
        """Class which create a PINNs for ode based on a radial basis network
         The network is:
         $$
             RBF(t,x ;theta)
         $$

        -----
        Inputs Parameters:
        - ode (AbstractOde): the ode associated to the problem
        - kwargs for the optional parameters

        Optional Parameters
        - inputs_size (int): pby defaut it is 1 (time) + nb_parameters. However we can change it (useful for neural operator).
        - outputs_size (int): pby defaut nb_unknowns of the ODE. However we can change it (useful for neural operator).
        """
        super().__init__()
        self.inputs_size = kwargs.get("inputs_size", 1 + ode.nb_parameters)
        self.outputs_size = kwargs.get("outputs_size", ode.nb_unknowns)

        self.net = rbfnet.RBFLayer(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Function: Forward of the RBF_t which concatenate t and mu and call the forward of the Radial basis network associated
        -----
        Inputs Parameters:
            - t (tensor): sampled time point
            - mu (tensor): sampled ode parameters point
        """
        inputs = torch.cat([t, mu], axis=1)
        return self.net.forward(inputs)


class Fourier_t(nn.Module):
    """Class which create a PINNs for ode based on MLP network enhanced with feature like Fourier
     The network is:
     $$
         MLP(t,x ;theta)
     $$

    -----
    Inputs Parameters:
    - ode (AbstractOde): the ode associated to the problem
    - kwargs for the optional parameters

    Optional Parameters:
    - nb_features (int): number of features added
    - type_feature (str): the name of feature (Fourier, Wavelet etc)
    - bool_feature_mu (bool): a boolean to decide if we compute feature on mu also
    - inputs_size (int): pby defaut it is 1 (time) + nb_parameters. However we can change it (useful for neural operator).
    - outputs_size (int): pby defaut nb_unknowns of the ODE. However we can change it (useful for neural operator).

    """

    def __init__(self, ode: pdes.AbstractODE, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.bool_feature_mu = kwargs.get("bool_feature_mu", False)
        self.outputs_size = kwargs.get("outputs_size", ode.nb_unknowns)

        self.features_t = mlp.EnhancedFeatureNet(in_size=1, **kwargs)
        self.inputs_size = (
            kwargs.get("inputs_size", 1 + ode.nb_parameters)
            + self.features_t.enhanced_dim
        )
        if self.bool_feature_mu:
            self.features_mu = mlp.EnhancedFeatureNet(
                in_size=ode.nb_parameters, **kwargs
            )
            self.inputs_size = self.inputs_size + self.features_mu.enhanced_dim

        self.net = mlp.GenericMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Function: Forward of the Fourier_t which:
            - create the Fourier feature in t
            - create (if the option is true) the Fourier feature in mu
            - concatenate t, mu and the Fourier feature and call the forward of the MLP

        In practice we can use other features than Fourier
        -----
        Inputs Parameters:
            - t (tensor): sampled time point
            - mu (tensor): sampled ode parameters point
        """
        features = self.features_t.forward(t)
        if self.bool_feature_mu:
            features = torch.cat([self.features_mu.forward(mu), features], axis=1)

        inputs = torch.cat([t, mu, features], axis=1)
        return self.net.forward(inputs)


class DisFourier_t(nn.Module):
    """Class which create a PINNs for ode based on discontinuous MLP network enhanced with feature like Fourier
     The network is:
     $$
         DMLP(t,x ;theta)
     $$

    -----
    Inputs Parameters:
    - ode (AbstractOde): the ode associated to the problem
    - kwargs for the optional parameters

    Optional Parameters:
    - nb_features (int): number of features added
    - type_feature (str): the name of feature (Fourier, Wavelet etc)
    - bool_feature_mu (bool): a boolean to decide if we compute feature on mu also
    - inputs_size (int): pby defaut it is 1 (time) + nb_parameters. However we can change it (useful for neural operator).
    - outputs_size (int): pby defaut nb_unknowns of the ODE. However we can change it (useful for neural operator).

    """

    def __init__(self, ode: pdes.AbstractODE, **kwargs):
        super().__init__()
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.bool_feature_mu = kwargs.get("bool_feature_mu", False)
        self.outputs_size = kwargs.get("outputs_size", ode.nb_unknowns)

        self.features_t = mlp.EnhancedFeatureNet(in_size=1, **kwargs)
        self.inputs_size = (
            kwargs.get("inputs_size", 1 + ode.nb_parameters)
            + self.features_t.enhanced_dim
        )
        if self.bool_feature_mu:
            self.features_mu = mlp.EnhancedFeatureNet(
                in_size=ode.nb_parameters, **kwargs
            )
            self.inputs_size = self.inputs_size + self.features_mu.enhanced_dim

        self.net = mlp.DiscontinuousMLP(
            in_size=self.inputs_size, out_size=self.outputs_size, **kwargs
        )

    def forward(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Function: Forward of the Fourier_t which:
            - create the Fourier feature in t
            - create (if the option is true) the Fourier feature in mu
            - concatenate t, mu and the Fourier feature and call the forward of the discontinuous MLP

        In practice we can use other features than Fourier
        -----
        Inputs Parameters:
            - t (tensor): sampled time point
            - mu (tensor): sampled ode parameters point
        """
        features = self.features_t.forward(t)
        if self.bool_feature_mu:
            features = torch.cat([self.features_mu.forward(mu), features], axis=1)

        inputs = torch.cat([t, mu, features], axis=1)
        return self.net.forward(inputs)
