from typing import Union

import torch

from scimba.equations.pdes import AbstractPDEtxv, AbstractPDExv

from . import uniform_sampling
from .sampling_ode import TSampler
from .sampling_parameters import MuSampler
from .sampling_pde import XSampler


class VSampler:
    """
    Class to sample the velocity domain with uniform sampling. Depending to the domain type (contains in the PDE)
    we call the good uniform sampling and create the BC sampling lists

    :param model: the pde model
    :type model: Union[AbstractPDExv,AbstractPDEtxv]
    """

    def __init__(self, pde: Union[AbstractPDExv, AbstractPDEtxv]):
        self.dim_v = pde.dimension_v
        if pde.velocity_domain.type == "square_based":
            self.velocity_domain = [
                [pde.velocity_domain.bound[i][0], pde.velocity_domain.bound[i][1]]
                for i in range(0, pde.dimension_v)
            ]
            self.sampler = uniform_sampling.UniformSampling(
                pde.dimension_v, self.velocity_domain
            )

            self.list_sampler_bc = []
            for i in range(0, self.dim_v):
                domain = list(
                    (
                        [
                            pde.velocity_domain.bound[i][0],
                            pde.velocity_domain.bound[i][1],
                        ]
                        for i in range(0, pde.dimension_v)
                    )
                )
                domain[i][0] = pde.velocity_domain.bound[i][0]
                domain[i][1] = pde.velocity_domain.bound[i][0] + 0.000001
                self.list_sampler_bc.append(
                    uniform_sampling.UniformSampling(pde.dimension_v, domain)
                )

                domain2 = list(
                    (
                        [
                            pde.velocity_domain.bound[i][0],
                            pde.velocity_domain.bound[i][1],
                        ]
                        for i in range(0, pde.dimension_v)
                    )
                )
                domain2[i][0] = pde.velocity_domain.bound[i][1] - 0.000001
                domain2[i][1] = pde.velocity_domain.bound[i][1]
                self.list_sampler_bc.append(
                    uniform_sampling.UniformSampling(pde.dimension_v, domain2)
                )
            self.nb_bc = 2 * pde.dimension_v

        if pde.velocity_domain.type == "disk_based":
            self.sampler = uniform_sampling.SphereUniformSampling(
                pde.dimension_v, pde.velocity_domain, surface=True
            )
            self.list_sampler_bc = []
            self.nb_bc = 0

    def sampling(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" element in the spatial domain

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing the sampled elements
        :rtype: torch.Tensor
        """
        data = self.sampler.sampling(n_points)
        data.requires_grad_()
        return data

    def bc_sampling(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" element of the boundary of the domain

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing the sampled elements
        :rtype: torch.Tensor
        """
        if self.nb_bc > 0:
            nb_points_by_boundary = int(n_points / (2 * self.dim_v))
            data = self.list_sampler_bc[0].sampling(nb_points_by_boundary)
            for i in range(1, len(self.list_sampler_bc)):
                y = self.list_sampler_bc[i].sampling(nb_points_by_boundary)
                data = torch.cat([data, y], axis=0)
        else:
            data = self.sampler.sampling(n_points)

        data.requires_grad_()
        return data

    def density(self, x: torch.Tensor) -> float:
        """
        compute the density of the law used for sampling at point x

        :param x: tensor of elements sampled
        :type x: torch.Tensor
        :return: the density value
        :rtype: float
        """
        return 1.0


class PdeXVCartesianSampler:
    """
    Class whoch create a Sampler for spatial PDE as a Cartesian product of spatial, velocity and parameters sampler

    :param x_sampler: the sampler for the spatial coordinates
    :type x_sampler: XSampler
    :param v_sampler: the sampler for the velocity coordinates
    :type v_sampler: VSampler
    :param mu_sampler: the sampler for the spatial coordinates
    :type mu_sampler: MuSampler
    """

    def __init__(self, x_sampler: XSampler, v_sampler: VSampler, mu_sampler: MuSampler):
        self.x_sampler = x_sampler
        self.v_sampler = v_sampler
        self.mu_sampler = mu_sampler

    def sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
        """
        Sample "n_points" triplet (x,v,mu) using the x sampler, the v sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples, v samples and mu samples
        :rtype: list[torch.Tensor]
        """
        data_x = self.x_sampler.sampling(n_points)
        data_v = self.v_sampler.sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_x, data_v, data_mu

    def sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" saptial points using the v sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing v samples
        :rtype: torch.Tensor
        """
        data_x = self.x_sampler.sampling(n_points)
        return data_x

    def bc_sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" spatial points using the x bc sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_x = self.x_sampler.bc_sampling(n_points)
        return data_x

    def sampling_v(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" velocity points using the v sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_v = self.v_sampler.sampling(n_points)
        return data_v

    def bc_sampling_v(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" velocity points using the v bc sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_v = self.v_sampler.bc_sampling(n_points)
        return data_v

    def bc_sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
        """
        Sample "n_points" couple (x,v,mu) using the x boundary sampler, v boundary sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: list[torch.Tensor]
        """
        data_x = self.bc_sampling_x(n_points)
        data_v = self.bc_sampling_v(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_x, data_v, data_mu

    def density(self, x, v, mu) -> float:
        """
        compute the density of the law used for sampling as a product of the spatial, velocity and mu density

        :param x: tensor of space sampled
        :type x: torch.Tensor
        :param mu: tensor of parameters sampled
        :type mu: torch.Tensor
        :return: the density value
        :rtype: float
        """
        return (
            self.x_sampler.density(x)
            * self.v_sampler.density(v)
            * self.mu_sampler.density(mu)
        )


# TODO: add a_sampler if it is included in the eq
class PdeTXVCartesianSampler:
    """
    Class which create a Sampler for spatial PDE as a Cartesian product of
        time, spatial, velocity and parameters sampler

    :param t_sampler: the sampler for the time
    :type t_sampler: XSampler
    :param x_sampler: the sampler for the spatial coordinates
    :type x_sampler: XSampler
    :param v_sampler: the sampler for the velocity coordinates
    :type v_sampler: VSampler
    :param mu_sampler: the sampler for the spatial coordinates
    :type mu_sampler: MuSampler
    :param with_external_field: indicate if there is a external field to sample also
    :type with_external_field: boolean
    """

    def __init__(
        self,
        t_sampler: TSampler,
        x_sampler: XSampler,
        v_sampler: VSampler,
        mu_sampler: MuSampler,
    ):
        self.t_sampler = t_sampler
        self.x_sampler = x_sampler
        self.v_sampler = v_sampler
        self.mu_sampler = mu_sampler
        self.with_external_field = False

    def sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
        """
        Sample "n_points" group (t,x,v,mu) using the time sampler, the x sampler,
        the v sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing t samples, x samples, v samples and mu samples
        :rtype: list[torch.Tensor]
        """
        data_t = self.t_sampler.sampling(n_points)
        data_x = self.x_sampler.sampling(n_points)
        data_v = self.v_sampler.sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_t, data_x, data_v, data_mu

    def sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" saptial points using the v sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing v samples
        :rtype: torch.Tensor
        """
        data_x = self.x_sampler.sampling(n_points)
        return data_x

    def bc_sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" spatial points using the x bc sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_x = self.x_sampler.bc_sampling(n_points)
        return data_x

    def sampling_v(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" velocity points using the v sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_v = self.v_sampler.sampling(n_points)
        return data_v

    def bc_sampling_v(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" velocity points using the v bc sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data_v = self.v_sampler.bc_sampling(n_points)
        return data_v

    def bc_sampling(self, n_points: int, **kwargs) -> list[torch.Tensor]:
        """
        Sample "n_points" groupe (t,x,v,mu) using th time sampler, the x boundary sampler,
        the v boundary sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: list[torch.Tensor]
        """
        data_t = self.t_sampler.sampling(n_points)
        data_x = self.bc_sampling_x(n_points)
        data_v = self.bc_sampling_v(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_t, data_x, data_v, data_mu

    def density(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> float:
        """
        compute the density of the law used for sampling as a product of the time, spatial, velocity and mu density

        :param x: tensor of space sampled
        :type x: torch.Tensor
        :param mu: tensor of parameters sampled
        :type mu: torch.Tensor
        :return: the density value
        :rtype: float
        """
        return (
            self.t_sampler.density(t)
            * self.x_sampler.density(x)
            * self.v_sampler.density(v)
            * self.mu_sampler.density(mu)
        )
