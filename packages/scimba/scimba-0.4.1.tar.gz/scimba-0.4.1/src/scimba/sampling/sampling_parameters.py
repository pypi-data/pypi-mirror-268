from typing import Union

import torch as torch
from torch import nn

from scimba.equations.pdes import (
    AbstractODE,
    AbstractPDEtx,
    AbstractPDEtxv,
    AbstractPDEx,
    AbstractPDExv,
)

from .abstract_sampling import AbstractSampling

# Here we define a general class to sampler the parameters using a given sampler for box


def MuSampler(sampler: AbstractSampling, **kwargs):
    class MuSampler(sampler):
        """
        Class to sample the parameter space with a given class of sampler.

        :param model: pde or ode models
        :type model: Union[AbstractODE,AbstractPDEx,AbstractPDExv,AbstractPDEtx,AbstractPDEtxv]
        """

        def __init__(
            self,
            model: Union[
                AbstractODE, AbstractPDEx, AbstractPDExv, AbstractPDEtx, AbstractPDEtxv
            ],
        ):
            super(sampler, self).__init__(nn.Module())

            self.dim = model.nb_parameters
            domain = [
                [model.parameter_domain[i][0], model.parameter_domain[i][1]]
                for i in range(0, model.nb_parameters)
            ]
            self.sampler = sampler(self.dim, domain)

        def sampling(self, n_points: int, **kwargs) -> torch.Tensor:
            """
            Sample "n_points" parameters of the domain

            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
            """
            data = self.sampler.sampling(n_points)
            data.requires_grad_()
            return data

    return MuSampler(**kwargs)
