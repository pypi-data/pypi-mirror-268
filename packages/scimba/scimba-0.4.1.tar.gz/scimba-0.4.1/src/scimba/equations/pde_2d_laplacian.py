import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEx


class Poisson2D(AbstractPDEx):
    r"""

    .. math::

        \frac{d^2u}{dx^2} + \frac{d^2u}{dy^2} + f = 0

    """

    def __init__(
        self, domain=SpaceDomain(2, SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    ):
        super().__init__(
            nb_unknowns=1,
            space_domain=domain,
            nb_parameters=1,
            parameter_domain=[[0.0, 1.0]],
        )

        self.first_derivative = True
        self.second_derivative = True

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = (
            8
            * torch.pi**2
            * alpha
            * torch.sin(2 * torch.pi * x1)
            * torch.sin(2 * torch.pi * x2)
        )
        return u_xx + u_yy + f

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        return alpha * torch.sin(2 * torch.pi * x1) * torch.sin(2 * torch.pi * x2)
