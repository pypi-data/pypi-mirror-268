
from typing import Callable, Union
import torch

from ..equations.domain import SpaceTensor
from ..equations.pdes import (
    AbstractPDEtx,
    AbstractPDEtxv,
    AbstractPDEx,
    AbstractPDExv,
)
from . import uniform_sampling
from .sampling_parameters import MuSampler

#### This file contains basic Samplers for the spatial domain and basic Samplers for space and space time PDE


class XSampler:
    """
        Class to sample the spatial domain with uniform sampling. Depending to the domain type (contains in the PDE)
        we call the good uniform sampling and create the BC sampling lists

        :param model: the pde model
        :type model: Union[AbstractPDEx,AbstractPDExv,AbstractPDEtx,AbstractPDEtxv]
    """

    def __init__(
        self, pde: Union[AbstractPDEx, AbstractPDExv, AbstractPDEtx, AbstractPDEtxv]
    ):
        self.pde = pde
        self.dim = pde.dimension_x
        self.list_bc_sampler = []
        self.list_bc_holes_sampler = []
        self.list_bc_subdomains_sampler = []

        # Construct the sampler for the large domain (Square, Disk or SDF)
        if pde.space_domain.large_domain.type == "square_based":
            self.domain = [
                [
                    pde.space_domain.large_domain.bound[i][0],
                    pde.space_domain.large_domain.bound[i][1],
                ]
                for i in range(self.dim)
            ]
            self.sampler = uniform_sampling.UniformSampling(self.dim, self.domain)
            if pde.space_domain.full_bc_domain:
                all_bounds = [
                    [
                        pde.space_domain.large_domain.bound[i][0],
                        pde.space_domain.large_domain.bound[i][1],
                    ]
                    for i in range(self.dim)
                ]
                for i in range(self.dim):  # go through each dimension
                    left_domain = all_bounds.copy()
                    left_domain[i][1] = all_bounds[i][0] + 1e-5
                    self.list_bc_sampler.append(
                        uniform_sampling.UniformSampling(self.dim, left_domain)
                    )
                    right_domain = all_bounds.copy()
                    right_domain[i][0] = all_bounds[i][1] - 1e-5
                    self.list_bc_sampler.append(
                        uniform_sampling.UniformSampling(self.dim, right_domain)
                    )

        if self.pde.space_domain.large_domain.type == "disk_based":
            self.sampler = uniform_sampling.SphereUniformSampling(
                self.dim, pde.space_domain.large_domain
            )
            if pde.space_domain.full_bc_domain:
                self.list_bc_sampler.append(
                    uniform_sampling.SphereUniformSampling(
                        self.dim, pde.space_domain.large_domain, surface=True
                    )
                )

        if self.pde.space_domain.large_domain.type == "sd_based":
            self.sampler = uniform_sampling.SquaredDistanceSampling(
                self.dim, pde.space_domain.large_domain
            )
            if pde.space_domain.full_bc_domain:
                self.list_bc_sampler.append(
                    uniform_sampling.SquaredDistanceSampling(
                        self.dim, pde.space_domain.large_domain, surface=True
                    )
                )

        # Construct the list of sampler for the boundary if there is subdomain
        if not self.pde.space_domain.full_bc_domain:
            for bc_subdomain in self.pde.space_domain.large_domain.list_bc_subdomains:
                self.list_bc_sampler.append(
                    uniform_sampling.ParametricCurveSampling(self.dim, bc_subdomain)
                )

            #  Construct the list of sampler for the boundary of the holes
            for hole in self.pde.space_domain.list_holes:
                for bc_subdomain in hole.list_bc_subdomains:
                    self.list_bc_holes_sampler.append(
                        uniform_sampling.ParametricCurveSampling(self.dim, bc_subdomain)
                    )

        # Construct the list of sampler for the  subdomains
        for subdomain in self.pde.space_domain.list_subdomains:
            for bc_subdomain in subdomain.list_bc_subdomains:
                self.list_bc_subdomains_sampler.append(
                    uniform_sampling.ParametricCurveSampling(self.dim, bc_subdomain)
                )

    def keep(self, condition:Callable[[torch.Tensor], torch.Tensor], data:SpaceTensor) -> SpaceTensor:
        """
            Function which keep the point which are inside the domain

            :param data: elements sampled in the box
            :type data: SpaceTensor
            :return: the tensor containing the elements inside the domain
            :rtype: SpaceTensor
        """
        not_to_regenerate = condition(data)
        return data[not_to_regenerate[:, 0]]

    def sampling(self, n_points: int, **kwargs) -> SpaceTensor:
        """
            Sample "n_points" element in the spatial domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: SpaceTensor
        """

        ## We sample point in the large domain
        if self.pde.space_domain.large_domain.type != "square_based":
            mapping = self.pde.space_domain.large_domain.mapping
            data = self.sampler.sampling(n_points, mapping)
        else:
            data = self.sampler.sampling(n_points)

        if self.pde.space_domain.large_domain.type != "sd_based":
            labels = torch.zeros(n_points, dtype=int)
            data = SpaceTensor(data, labels)

        ## We keep point which are not in the hole
        for hole in self.pde.space_domain.list_holes:
            data = self.keep(hole.is_outside, data)

        count = n_points - data.shape[0]

        if count > 0:
            data_new = self.sampling(count)
            data = data.cat(data_new)
        elif count < 0:
            data = data[:count]

        data.x.requires_grad_()

        for i, subdomain in enumerate(self.pde.space_domain.list_subdomains):
            condition = subdomain.is_inside(data)
            data.labels[condition[:, 0]] = i + 1  ### 0 is big domain

        return data

    def bc_sampling(self, n_points: int, **kwargs) -> torch.Tensor:
        """
            Sample "n_points" element of the boundary of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
        """
        nb_bc_external = len(self.list_bc_sampler)

        nb_bc_hole = 0
        for hole in self.pde.space_domain.list_holes:
            nb_bc_hole += len(hole.list_bc_subdomains)

        # nb_bc_hole = len(self.pde.space_domain.list_holes)

        nb_subdomains = 0
        for subdomain in self.pde.space_domain.list_subdomains:
            nb_subdomains += len(subdomain.list_bc_subdomains)

        # nb_subdomains = len(self.pde.space_domain.list_subdomains)

        nb_bc = nb_bc_external + nb_bc_hole + nb_subdomains
        nb_points_by_boundary = [n_points // nb_bc] * nb_bc
        for i in range(n_points % nb_bc):
            nb_points_by_boundary[i] += 1

        data = torch.zeros((n_points, self.dim))
        labels = torch.zeros(n_points, dtype=int)

        if self.pde.compute_normals:
            normals = torch.zeros((n_points, self.dim))

        ### boundary of the large domain
        j = 0
        for i in range(nb_bc_external):
            nb_boundary = nb_points_by_boundary[i]
            if self.pde.space_domain.large_domain.type != "square_based":
                result = self.list_bc_sampler[i].sampling(
                    nb_boundary,
                    mapping=self.pde.space_domain.large_domain.mapping,
                    compute_normals=self.pde.compute_normals,
                )
                if self.pde.compute_normals:
                    data[j : j + nb_boundary], normals[j : j + nb_boundary] = result
                else:
                    data[j : j + nb_boundary] = result
            else:
                data[j : j + nb_boundary] = self.list_bc_sampler[i].sampling(
                    nb_boundary
                )
                if self.pde.compute_normals:
                    normals[j : j + nb_boundary] = (
                        self.pde.space_domain.large_domain.compute_normals(
                            data[j : j + nb_boundary], i
                        )
                    )

            labels[j : j + nb_boundary] = i
            j += nb_boundary

        for i in range(nb_bc_hole):
            nb_boundary = nb_points_by_boundary[i + nb_bc_external]

            # no mapping is applied here since the hole should not be deformed
            result = self.list_bc_holes_sampler[i].sampling(
                nb_boundary,
                mapping=self.pde.space_domain.list_holes[i].mapping,
                compute_normals=self.pde.compute_normals,
            )
            if self.pde.compute_normals:
                data[j : j + nb_boundary], normals[j : j + nb_boundary] = result
                normals[j : j + nb_boundary] = -normals[j : j + nb_boundary]
            else:
                data[j : j + nb_boundary] = result

            labels[j : j + nb_boundary] = nb_bc_external + i
            j += nb_boundary

        for i in range(nb_subdomains):
            nb_boundary = nb_points_by_boundary[i + nb_bc_hole]

            # no mapping is applied here since the hole should not be deformed
            result = self.list_bc_subdomains_sampler[i].sampling(
                nb_boundary,
                mapping=self.pde.space_domain.list_subdomains[i].mapping,
                compute_normals=self.pde.compute_normals,
            )
            if self.pde.compute_normals:
                data[j : j + nb_boundary], normals[j : j + nb_boundary] = result
                normals[j : j + nb_boundary] = -normals[j : j + nb_boundary]
            else:
                data[j : j + nb_boundary] = result

            labels[j : j + nb_boundary] = nb_bc_external + nb_bc_hole + i
            j += nb_boundary

        data.requires_grad_()

        if self.pde.compute_normals:
            data = SpaceTensor(data, labels, boundary=True, n=normals)
        else:
            data = SpaceTensor(data, labels)

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


class PdeXCartesianSampler:
    """
    Class whoch create a Sampler for spatial PDE as a Cartesian product of spatial and parameters sampler

    :param x_sampler: the sampler for the spatial coordinates
    :type x_sampler: XSampler
    :param mu_sampler: the sampler for the spatial coordinates
    :type mu_sampler: MuSampler
    """

    def __init__(self, x_sampler: XSampler, mu_sampler: MuSampler):
        self.x_sampler = x_sampler
        self.mu_sampler = mu_sampler

    def sampling(self, n_points: int, **kwargs) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Sample "n_points" couple (x,mu) using the x sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: tuple[torch.Tensor]
        """
        data_x = self.x_sampler.sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_x, data_mu

    def sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" spatial points using the x sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        data = self.x_sampler.sampling(n_points)
        return data

    def bc_sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" spatial points at the boundary using the x sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples at the boundary
        :rtype: torch.Tensor
        """
        data = self.x_sampler.bc_sampling(n_points)
        return data

    def bc_sampling(self, n_points: int, **kwargs) -> tuple[torch.Tensor, torch.Tensor]:
        """
        Sample "n_points" couple (x,mu) using the x boundary sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: tuple[torch.Tensor]
        """
        data_x = self.x_sampler.bc_sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_x, data_mu

    def density(self, x: torch.Tensor, mu: torch.Tensor) -> float:
        """
        compute the density of the law used for sampling as a product of the spatial and mu density

        :param x: tensor of space sampled
        :type x: torch.Tensor
        :param mu: tensor of parameters sampled
        :type mu: torch.Tensor
        :return: the density value
        :rtype: float
        """
        return self.x_sampler.density(x) * self.mu_sampler.density(mu)


class PdeTXCartesianSampler:
    """
    Class which create a Sampler for space time PDE as a Cartesian product of spatial,time and parameters sampler

    :param t_sampler: the sampler for the time
    :type t_sampler: TSampler
    :param x_sampler: the sampler for the spatial coordinates
    :type x_sampler: XSampler
    :param mu_sampler: the sampler for the spatial coordinates
    :type mu_sampler: MuSampler
    """

    def __init__(self, t_sampler, x_sampler, mu_sampler):
        self.t_sampler = t_sampler
        self.x_sampler = x_sampler
        self.mu_sampler = mu_sampler

    def sampling(
        self, n_points: int, **kwargs
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Sample "n_points" triplet (t,x,mu) using the time sampler, x sampler, the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: tuple[torch.Tensor]
        """
        data_t = self.t_sampler.sampling(n_points)
        data_x = self.x_sampler.sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_t, data_x, data_mu

    def sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" spatial points using the x sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the tensor containing x samples
        :rtype: torch.Tensor
        """
        return self.x_sampler.sampling(n_points)

    def bc_sampling_x(self, n_points: int, **kwargs) -> torch.Tensor:
        """
        Sample "n_points" couple (x,mu) using the x boundary sampler and the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: torch.Tensor
        """
        data = self.x_sampler.bc_sampling(n_points)
        return data

    def bc_sampling(
        self, n_points: int, **kwargs
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        """
        Sample "n_points" triplet (t,x,mu) using the time sampler, x bc sampler, the mu sampler

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the list of tensor containing x samples and mu samples
        :rtype: tuple[torch.Tensor]
        """
        data_t = self.t_sampler.sampling(n_points)
        data_x = self.x_sampler.bc_sampling(n_points)
        data_mu = self.mu_sampler.sampling(n_points)
        return data_t, data_x, data_mu

    def density(self, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor) -> float:
        """
        compute the density of the law used for sampling as a product of the time, spatial and mu densities

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
            * self.mu_sampler.density(mu)
        )
