from abc import ABC, abstractmethod
from typing import Union
import torch as torch

import scimba.equations.domain as domain

class AbstractQuad(ABC):
    """
        Abstract Class for sampling.
       
        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param domain: domain or bounds of the domain (square case) that we want sample 
        :type domain: Union[torch.Tensor, list[list]]

    """
    def __init__(
        self,
        dim:int,
        order:int,
    ):
        self.dim = dim
        self.order =order


    @abstractmethod
    def get_quad(self, order, **kwargs) -> list[torch.Tensor]:
        pass


