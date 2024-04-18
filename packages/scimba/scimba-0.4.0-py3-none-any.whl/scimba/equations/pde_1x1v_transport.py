import numpy as np
import torch

from .domain import SpaceDomain, SpaceTensor, SquareDomain
from .pdes import AbstractPDEtxv


class ConstantInX(AbstractPDEtxv):
    r"""
    Advection equation class

    - Equation:

      .. math::

         \frac{df}{dt} + v \cdot \frac{df}{dx} = 0

    - Domain: :math:`x\in [0,1], t\in[0,0.1], v \in [-6,6]`
    - BC: periodic boundary condition in x
    - IC:

        .. math::

           f_0(x,v) = sin(2 \pi x) \cdot  1 / ( sqrt(2 \pi \sigma^2) ) \cdot exp(-v^2 / (2 \sigma^2) )

    - Reference solution: :math:`f_0(x-vt,v)`
    - We learn:  :math:`u_{\theta}(t,x,v)`
    - parametric model: :math:`f_{net} = f_0 + t \cdot u_{\theta}(t,x,v)`

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0.0, 0.2],
            space_domain=SpaceDomain(1, SquareDomain(1, [[0.0, 1.0]])),
            velocity_domain=SquareDomain(1, [[-6.0, 6.0]]),
            nb_parameters=0,
            parameter_domain=[],
            data_construction="sampled",
        )

        self.first_derivative_t = True
        self.first_derivative_x = True
        self.t_min, self.t_max = self.time_domain

    def residual(self, w, t, x, v, mu, **kwargs):
        u_t = self.get_variables(w, "w_t")
        u_x = self.get_variables(w, "w_x")
        return u_t + v * u_x

    def bc_residual(self, w, t, x, v, mu):
        # TODO: separate bc_residual for x and v
        return self.get_variables(w, "w")

    """
    In order to impose strongly the initial condition in the network,
    we define the functions bc_add and bc_mul.
    In order to desactivate this feature, comment the these two functions.
    see file PINN.py --> class PINN_txv for more details
    """

    def post_processing(self, t, x, v, mu, w):
        t0 = 0.0
        return self.reference_solution(t0, x, v, mu) + t * w

    def initial_condition(self, x, v, mu):
        x = x.get_coordinates()

        sigma = 1.0
        return (
            torch.sin(2 * torch.pi * x)
            * 1.0
            / (np.sqrt(2 * torch.pi * sigma**2))
            * torch.exp(-(v**2) / (2.0 * sigma**2))
        )

    def reference_solution(self, t, x, v, mu, a=None):
        shifted_x = SpaceTensor(x.x - v * t, x.labels)
        return self.initial_condition(shifted_x, v, mu)

    def make_data(self, n_data):
        pass  # TODO: make data from simulation
