import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEx


class SteadyTransport(AbstractPDEx):
    r"""

    .. math::

        \frac{dv}{dx} - \alpha v - \beta v^2 = 0

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            dimension_x=1,
            space_domain=SpaceDomain(1,SquareDomain(1, [[0.0, 1.0]])),
            nb_parameters=3,
            parameter_domain=[[0.5, 1], [0.5, 1], [0.1, 0.2]],
        )

        self.first_derivative = True

        self.x_min, self.x_max = self.space_domain.large_domain[0]

    def bc_condition(self, w, x, mu):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        u = self.get_variables(w)
        u_x = self.get_variables(w, "w_x")
        alpha, beta, _ = self.get_parameters(mu)
        return u_x - alpha * u - beta * u**2

    def post_processing(self, x, mu, w):
        alpha, beta, u0 = self.get_parameters(mu)
        return u0 + (x - self.xmin) * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, x, mu):
        alpha, beta, u0 = self.get_parameters(mu)
        return alpha * u0 / ((alpha + beta * u0) * torch.exp(-alpha * x) - beta * u0)
