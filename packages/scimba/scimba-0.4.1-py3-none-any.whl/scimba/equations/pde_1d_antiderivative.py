import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEx


class Antiderivative(AbstractPDEx):
    r"""
    .. math::

        \frac{du}{dx} = 2*pi*\mu*cos(2*pi*\mu*x)

        with u(0) = 0

    """

    def __init__(
        self,
        domain=SpaceDomain(1,SquareDomain(1, [[0.0, 1.0]])),
        p_domain=[[0.5, 1.0]],
    ):
        super().__init__(
            nb_unknowns=1,
            space_domain=domain,
            nb_parameters=1,
            parameter_domain=p_domain,
        )

        self.first_derivative = True

    def bc_residual(self, w, x, mu):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        u_x = self.get_variables(w, "w_x")
        alpha = self.get_parameters(mu)
        return u_x - 2 * torch.pi * alpha * torch.cos(2 * torch.pi * alpha * x)

    def post_processing(self, x, mu, w):
        u0 = 0.0
        return u0 + x * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, x, mu):
        alpha = self.get_parameters(mu)
        return torch.sin(2 * torch.pi * alpha * x)
