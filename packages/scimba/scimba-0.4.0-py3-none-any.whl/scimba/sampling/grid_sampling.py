from scipy.stats import qmc
import torch
from .abstract_sampling import AbstractSampling


class LatinHypercubeSampling(AbstractSampling):
    """
        Class for Latin Hypercube sampling of index of a tensor.
       
        :param dim: the dimension of the object that we want sample
        :type dim: int
        :param low_bound: lower bounds of the tensor in each direction
        :type low_bound: list
        :param high_bound: lower bounds of the tensor in each direction
        :type high_bound: list
    """
    def __init__(self, dim, low_bound, high_bound, seed=45):
        self.dim = dim
        self.low_bound = low_bound
        self.high_bound = high_bound
        self.sampler = qmc.LatinHypercube(d=dim, seed=seed)

    def sampling(self, n_points:int, **kwargs) -> torch.Tensor:
        """
            Sample "n_points" index 
       
            :param n_points: number of elements that we want
            :type n_points: int
            :return: the tensor containing the sampled elements
            :rtype: torch.Tensor
        """
        if n_points != 0:
            indices = self.sampler.integers(
                self.low_bound, u_bounds=self.high_bound, n=n_points
            )
        else:
            indices = self.sampler.integers(
                self.low_bound, u_bounds=self.high_bound, n=10
            )
        return indices

    def density(self, x: torch.Tensor)-> float:
        """
            compute the density of the law used for sampling at point x
       
            :param x: tensor of elements sampled
            :type x: torch.Tensor
            :return: the density value
            :rtype: float
        """  
        return 1.0
