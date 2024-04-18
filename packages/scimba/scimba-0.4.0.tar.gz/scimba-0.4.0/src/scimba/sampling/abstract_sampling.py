from abc import ABC, abstractmethod
from typing import Callable, Union

import torch as torch

from ..equations import domain as cdomain


class AbstractSampling(ABC):
    """
    Abstract Class for sampling.

    :param dim: the dimension of the object that we want sample
    :type dim: int
    :param domain: domain or bounds of the domain (square case) that we want sample
    :type domain: Union[torch.Tensor, list[list]]

    """

    def __init__(
        self,
        dim: int,
        domain: Union[torch.Tensor, list[list]] = [],
    ):
        self.dim = dim
        self.domain = domain

    @abstractmethod
    def sampling(
        self,
        n_points: int,
        mapping: Callable[[torch.Tensor], torch.Tensor] = cdomain.Id_domain,
        **kwargs,
    ) -> torch.Tensor:
        pass

    @abstractmethod
    def density(self, x: torch.Tensor) -> float:
        pass
