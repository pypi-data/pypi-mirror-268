from typing import Callable, Union

import torch
import torch.distributions.uniform as uni

from ..equations import domain as cdomain
from ..equations.domain import SpaceTensor
from .abstract_sampling import AbstractSampling

## Different  uniform sampling class for different type of domain


class UniformSampling(AbstractSampling):
    """
        Class for uniform sampling on a box.

        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param domain: bounds of the domain that we want sample
        :type domain: list[list]
    """

    def __init__(self, dim: int, domain: list[list]):
        super().__init__(dim, domain)
        lower_bound = torch.tensor([self.domain[i][0] for i in range(0, self.dim)])
        upper_bound = torch.tensor([self.domain[i][1] for i in range(0, self.dim)])
        self.sampler = uni.Uniform(lower_bound, upper_bound)

    def sampling(self, n_points: int) -> torch.Tensor:
        """
            Sample "n_points" element in the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
        """
        data = self.sampler.sample((n_points,))
        return data

    def density(self, x: torch.Tensor) -> float:
        """
            compute the density of the law used for sampling at point x

            :param x: tensor of elements sampled
            :type x: torch.Tensor
            :return: the density value
            :rtype: float
        """
        return 1


class SphereUniformSampling(AbstractSampling):
    """
        Class for uniform sampling on a ball or on a sphere.

        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param domain: domain that we want sample
        :type domain: DiskBasedDomain
        :param surface: boolean to indicate if we sample the volume or the surface
        :type surface: bool
    """

    def __init__(
        self, dim: int, domain: cdomain.DiskBasedDomain, surface: bool = False
    ):
        super().__init__(dim, domain)
        if surface is False:
            self.sampler_r = uni.Uniform(0.0, self.domain.radius)
        else:
            self.sampler_r = uni.Uniform(self.domain.radius - 1e-5, self.domain.radius)

        self.sampler_theta = uni.Uniform(0.0, 2.0 * torch.pi)
        if self.domain.dim == 3:
            self.sampler_phi = uni.Uniform(0.0, torch.pi)

    def sampling(
        self,
        n_points: int,
        mapping: Callable[[torch.Tensor], torch.Tensor] = cdomain.Id_domain,
        compute_normals: bool = False,
    ) -> torch.Tensor:
        """
            Sample "n_points" element of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :param mapping: the mapping function
            :type mapping: Callable[[torch.Tensor], torch.Tensor]
            :param compute_normals: whether to compute the normals
            :type compute_normals: bool
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
        """
        r = torch.sqrt(self.sampler_r.sample((n_points,)))
        theta = self.sampler_theta.sample((n_points,))

        if self.domain.dim == 2:
            x = self.domain.center[0] + r * torch.cos(theta)
            y = self.domain.center[1] + r * torch.sin(theta)
            data = mapping(torch.cat([x[:, None], y[:, None]], axis=1))

        if self.domain.dim == 3:
            phi = self.sampler_theta.sample((n_points,))
            x = self.domain.center[0] + r * torch.cos(theta) * torch.sin(phi)
            y = self.domain.center[1] + r * torch.sin(theta) * torch.sin(phi)
            z = self.domain.center[2] + r * torch.cos(phi)
            data = mapping(torch.cat([x[:, None], y[:, None], z[:, None]], axis=1))

        if compute_normals:
            normals = self.domain.compute_normals(data, mapping)
            return data, normals
        else:
            return data

    def density(self, x: torch.Tensor) -> float:
        """
            Compute the density of the law used for sampling at point x

            :param x: tensor of elements sampled
            :type x: torch.Tensor
            :return: the density value
            :rtype: float
        """
        return 1


class ParametricCurveSampling(AbstractSampling):
    """
        Class for uniform sampling on a parametric surface.

        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param domain: bounds of the domain that we want sample
        :type domain: list[list]
    """

    def __init__(self, dim: int, domain: cdomain.ParametricCurveBasedDomain):
        super().__init__(dim, domain)
        self.domain = domain
        lower_bound = torch.tensor(
            [
                self.domain.parametric_domain[i][0]
                for i in range(0, self.domain.dim_parameters)
            ]
        )
        upper_bound = torch.tensor(
            [
                self.domain.parametric_domain[i][1]
                for i in range(0, self.domain.dim_parameters)
            ]
        )
        self.sampler = uni.Uniform(lower_bound, upper_bound)

    def sampling(
        self,
        n_points: int,
        mapping: Callable[[torch.Tensor], torch.Tensor] = cdomain.Id_domain,
        compute_normals: bool = False,
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
            Sample "n_points" element in the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :param mapping: the mapping function
            :type mapping: Callable[[torch.Tensor], torch.Tensor]
            :param compute_normals: whether to compute the normals
            :type compute_normals: bool
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
        """
        data_param = self.sampler.sample((n_points,))
        data = mapping(self.domain.surface(data_param))

        if compute_normals:
            normals = self.domain.compute_normals(data_param, mapping)
            return data, normals
        else:
            return data

    def density(self, x: torch.Tensor) -> torch.Tensor:
        """
            Compute the density of the law used for sampling at point x

            :param x: tensor of elements sampled
            :type x: torch.Tensor
            :return: the density value for each x
            :rtype: torch.Tensor
        """
        return 1


class SquaredDistanceSampling(AbstractSampling):
    """
        Class for uniform sampling on a domain defined by a signed distance function.

        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param domain: domain that we want sample
        :type domain: SignedDistanceBasedDomain
        :param surface: boolean to indicate if we sample the volume or the surface
        :type surface: bool
    """

    def __init__(
        self, dim: int, domain: cdomain.SignedDistanceBasedDomain, surface: bool = False
    ):
        super().__init__(dim, domain)

        self.low_bound = torch.tensor(
            [self.domain.surrounding_domain.bound[i][0] for i in range(0, self.dim)]
        )
        self.high_bound = torch.tensor(
            [self.domain.surrounding_domain.bound[i][1] for i in range(0, self.dim)]
        )
        self.sampler = uni.Uniform(self.low_bound, self.high_bound)

        self.sd_function = domain.sdf
        self.surface = surface

        if self.surface:
            self.condition = self.domain.on_border
        else:
            self.condition = self.domain.is_inside

        print("Threshold of the sampling: ", self.domain.threshold)

    def keep(self, data:SpaceTensor) -> SpaceTensor:
        """
            Function which keep the point which are inside the domain

            :param data: elements sampled in the box
            :type data: SpaceTensor
            :return: the tensor containing the elements inside the domain
            :rtype: SpaceTensor
        """
        not_to_regenerate = self.condition(data)
        return data[not_to_regenerate[:, 0]]

    def generate_data(self, n_points:int) -> SpaceTensor:
        """
        general "n_points" element of the domain using the signed distance function

        :param n_points: number of elements that we want
        :type n_points: int
        :return: the SpaceTensor containing the sampled elements
        :rtype: SpaceTensor
        """
        if self.surface:
            # to generate more points than needed to keep only n_points
            area = torch.prod(self.high_bound - self.low_bound, 0)
            n_points_surrounding_domain = int(
                (100 * area / 0.01).numpy()
            )  # 100 points per 0.01 area
        else:
            n_points_surrounding_domain = n_points

        data = self.sampler.sample((n_points_surrounding_domain,))
        labels = torch.zeros(data.shape[0], dtype=int)
        data = SpaceTensor(data, labels)
        data = self.keep(data)
        count = n_points - data.shape[0]

        if count > 0:
            data_new = self.generate_data(count)
            data = data.cat(data_new)
        elif count < 0:
            data = data[:count]

        return data

    def sampling(
        self,
        n_points: int,
        mapping: Callable[[torch.Tensor], torch.Tensor] = cdomain.Id_domain,
        compute_normals: bool = False,
    ) -> SpaceTensor:
        """
            Sample "n_points" element of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :param mapping: the mapping function
            :type mapping: Callable[[torch.Tensor], torch.Tensor]
            :param compute_normals: whether to compute the normals
            :type compute_normals: bool
            :return: the SpaceTensor containing the sampled elements
            :rtype: SpaceTendor
        """
        data = mapping(self.generate_data(n_points))

        # Recalibrate points on the boundary by gradient descent
        # if self.surface:
        #     max_iter = 0
        #     while max_iter < 50: #self.sd_function(data).min()>eps():
        #         phi = self.sd_function(data)
        #         grad_phi = torch.autograd.grad(phi.sum(), data, create_graph=True)[0]
        #         data = data - phi[:,None]*grad_phi
        #         max_iter += 1

        if compute_normals:
            normals = self.domain.compute_normals(data, mapping)
            return data, normals
        else:
            return data

    def density(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute the density of the law used for sampling at point x

            :param x: tensor of elements sampled
            :type x: SpaceTensor
            :return: the density value for each x
            :rtype: torch.Tensor
        """
        return 1
