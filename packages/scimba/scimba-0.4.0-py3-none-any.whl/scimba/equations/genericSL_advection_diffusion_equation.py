from abc import ABC, abstractmethod
from typing import Union

import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEtx


class AdvectionDiffusionData(ABC):
    """
        A class to describe advection diffusion problem for Semi Lagrangian
        method

        :param advection_is_constant: if the advection coefficient is constant in space or not
        :type advection_is_constant:  boolean
        :param diffusion_is_constant: if the diffusion coefficient is constant in space or not
        :type diffusion_is_constant: boolean
        :param has_advection: if the advection term is present or not
        :type has_advection: boolean
        :param has_diffusion: if the diffusion term is present or not
        :type has_diffusion: boolean
        :param nb_parameters: number of parameters 
        :type nb_parameters: int
        :param parameter_domain: the list of parameter domains
        :type parameter_domain: list[list]
    """
    def __init__(
        self,
        advection_is_constant:bool=True,
        diffusion_is_constant:bool=True,
        has_advection:bool=True,
        has_diffusion:bool=True,
        nb_parameters:int=1,
        parameter_domain:list[list]=[]
    ):
        self.advection_is_constant = advection_is_constant
        self.diffusion_is_constant = diffusion_is_constant
        self.has_advection = has_advection
        self.has_diffusion = has_diffusion
        self.nb_parameters = nb_parameters
        self.parameter_domain = parameter_domain

    @abstractmethod
    def a(self, t, x,mu):
        pass

    @abstractmethod
    def D(self, t, x,mu):
        pass

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_times(self, t: torch.Tensor) -> torch.Tensor:
        """
        Returns the time bach from the time tensor.

        :param time: the tensor of physical time
        :type time: torch.Tensor
        :return: the time tensor
        :rtype: torch.Tensor
        """
        return t[:, 0, None]
