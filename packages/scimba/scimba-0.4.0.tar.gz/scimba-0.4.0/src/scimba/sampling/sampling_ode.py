from typing import Union

import torch
from torch import nn

from scimba.equations.pdes import AbstractODE, AbstractPDEtx, AbstractPDEtxv

from ..pinns.pinn_losses import PinnLossesData
from .abstract_sampling import AbstractSampling
from .sampling_parameters import MuSampler


def TSampler(sampler: AbstractSampling, **kwargs):
    class t_sampler(sampler):
        """
        Class to sample the time domain with a given class of sampler.

        :param ode: pde or ode models
        :type ode: Union[AbstractODE,AbstractPDEtx,AbstractPDEtxv]
        """

        def __init__(self, ode: Union[AbstractODE, AbstractPDEtx, AbstractPDEtxv]):
            super(sampler, self).__init__(nn.Module())
            self.sampler = sampler(
                dim=1, domain=[[ode.time_domain[0], ode.time_domain[1]]]
            )
            self.coupling_training = False

        def sampling(self, n_points: int, **kwargs) -> torch.Tensor:
            """
            Sample "n_points" time of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
            """
            data = self.sampler.sampling(n_points)
            data.requires_grad_()
            return data

        def training_to_sampler(self, **kwargs):
            """
            function to obtain data for the trainer
            """
            pass

    return t_sampler(**kwargs)


def TSamplerProgressive(sampler, **kwargs):
    class t_sampler_progressive(sampler):
        """
        Class to progressively sample the time domain with a given class of sampler. We begin to sample a subdomain
        and increase to domain size when the residual is sufficiently small

        :param ode: pde or ode models
        :type ode: Union[AbstractODE,AbstractPDEtx,AbstractPDEtxv]
        :param M: number of time subdomain
        :type M: int, optional
        :param epsilon: the threshold for the error. When error is smaller we increase the subdomain
        :type epsilon: float, optional
        """

        def __init__(
            self,
            ode: Union[AbstractODE, AbstractPDEtx, AbstractPDEtxv],
            M: int = 1,
            epsilon: float = 0.005,
        ):
            super(sampler, self).__init__(nn.Module())
            self.M = M
            self.Deltat = (ode.time_domain[1] - ode.time_domain[0]) / self.M
            self.t0 = ode.time_domain[0]
            self.t1 = self.Deltat
            self.current_domain = 0
            self.sampler = sampler(dim=1, domain=[[self.t0, self.t1]])
            self.epsilon = epsilon
            self.coupling_training = True

        def sampling(self, n_points: int, **kwargs) -> torch.Tensor:
            """
            Sample "n_points" element of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
            """
            data = self.sampler.sampling(n_points)
            data.requires_grad_()
            return data

        def training_to_sampler(self, losses: PinnLossesData):
            """
            function to obtain data for the trainer. Here we obtain the value of the residual loss
            If the residual loss is smaller than the threshold we modify the sampler increasing the time domain.

            :param losses: the loss of the problem
            :type: PinnLossesData
            """
            if losses.residual_loss < self.epsilon and self.current_domain < self.M - 1:
                self.t1 = self.t1 + self.Deltat
                self.sampler = sampler(dim=1, domain=[[self.t0, self.t1]])
                self.current_domain = self.current_domain + 1

    return t_sampler_progressive(**kwargs)


# sample mu and t with the same basic sampler
def OdeFullSampler(sampler, **kwargs):
    class ode_full_sampler(sampler):
        """
        Class which create a Sampler for ODE sampling in the same time t and mu

        :param ode: the model
        :type ode: Union[AbstractODE,AbstractPDEtx,AbstractPDEtxv]
        """

        def __init__(self, ode):
            super(sampler, self).__init__(nn.Module())

            domain = [[ode.time_domain[0], ode.time_domain[1]]]
            domain = domain + [
                [ode.parameter_domain[i][0], ode.parameter_domain[i][1]]
                for i in range(0, ode.nb_parameters)
            ]

            self.sampler = sampler(dim=ode.nb_parameters + 1, domain=domain)
            self.coupling_training = False

        def sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
            """
            Sample "n_points" couple (t,mu) using one sampler given for the (mu,t) domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the list of tensor containing t samples and mu samples
            :rtype: list[torch.Tensor]
            """
            data = self.sampler.sampling(n_points)
            t = data[:, 0]
            mu = data[:, 1:]
            return t[:, None], mu

        def training_to_sampler(self, losses: PinnLossesData):
            pass

        def density(self, t: torch.Tensor, mu: torch.Tensor) -> float:
            """
            compute the density of the law used for sampling in the (mu,time) domain

            :param t: tensor of time sampled
            :type t: torch.Tensor
            :param mu: tensor of time sampled
            :type mu: torch.Tensor
            :return: the density value
            :rtype: float
            """
            return self.sampler.density(torch.cat([t, mu], axis=1))

    return ode_full_sampler(**kwargs)


# sample mu and t with different basic samplers
class OdeCartesianSampler:
    """
    Class which create a Sampler for ODE as a Cartesian product of time and parameters sampler

    :param t_sampler: the sampler for the time
    :type t_sampler: Union[TSampler,TSamplerProgressive]
    :param mu_sampler: the sampler for the spatial coordinates
    :type mu_sampler: MuSampler
    """

    def __init__(
        self, t_sampler: Union[TSampler, TSamplerProgressive], mu_sampler: MuSampler
    ):
        self.t_sampler = t_sampler
        self.mu_sampler = mu_sampler
        self.coupling_training = self.t_sampler.coupling_training

    def sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
        """
        Sample "n_points" couple (t,mu) using the t sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing t samples and mu samples
        :rtype: list[torch.Tensor]
        """
        data_t = self.t_sampler.sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_t, data_mu

    def training_to_sampler(self, losses: PinnLossesData):
        """
        call the function training to sampler of the time sampler
        """
        self.t_sampler.training_to_sampler(losses)

    def density(self, t: torch.Tensor, mu: torch.Tensor) -> float:
        """
        compute the density of the law used for sampling as a product of the time and mu densities

        :param t: tensor of time sampled
        :type t: torch.Tensor
        :param mu: tensor of parameters sampled
        :type mu: torch.Tensor
        :return: the density value
        :rtype: float
        """
        return self.t_sampler.density(t) * self.mu_sampler.density(mu)
