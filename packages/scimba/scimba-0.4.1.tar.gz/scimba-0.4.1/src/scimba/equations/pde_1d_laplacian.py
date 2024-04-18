import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEx


class LaplacianOneParameter(AbstractPDEx):
    r"""

    .. math::

        \frac{d^2u}{dx^2} + \mu \sin{2\pi k x} = 0

    """

    def __init__(
        self,
        k=1,
        domain=SpaceDomain(1, SquareDomain(1, [[0.0, 1.0]])),
        p_domain=[[0.0, 1.0]],
    ):
        super().__init__(
            nb_unknowns=1,
            space_domain=domain,
            nb_parameters=1,
            parameter_domain=p_domain,
        )

        self.k = k

        self.first_derivative = True
        self.second_derivative = True

    def bc_residual(self, w, x, mu, **kwargs):
        u = self.get_variables(w)
        return u - 0.0

    def residual(self, w, x, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u_xx = self.get_variables(w, "w_xx")
        f = alpha * torch.sin(2 * self.k * torch.pi * x)
        return u_xx + f

    def post_processing(self, x, mu, w):
        return (x - self.x_min) * (self.x_max - x) * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, x, mu):
        alpha = self.get_parameters(mu)
        k0 = 2 * self.k * torch.pi
        return alpha / k0**2 * torch.sin(x * k0)


class LaplacianSine(AbstractPDEx):
    r"""

    .. math::

        \frac{d^2v}{dx^2} + \mu_0 \sin{2\pi k x} \\
                + \mu_1 \sin{2\pi (k+1) x} \\
                + \mu_2 \sin{2\pi (k+2) x} = 0

    """

    def __init__(
        self,
        k,
        domain=SquareDomain(1, [[0.0, 1.0]]),
        p_domain=[[0.0, 1.0], [0.0, 0.5], [0.0, 0.1]],
    ):
        super().__init__(
            nb_unknowns=1,
            space_domain=domain,
            nb_parameters=3,
            parameter_domain=p_domain,
        )

        self.k = k
        self.first_derivative = True
        self.second_derivative = True

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x = x.get_coordinates()
        a, b, c = self.get_parameters(mu)
        f = (
            a * torch.sin(2 * self.k * torch.pi * x)
            + b * torch.sin(2 * (self.k + 1) * torch.pi * x)
            + c * torch.sin(2 * (self.k + 2) * torch.pi * x)
        )
        u_xx = self.get_variables(w, "w_xx")
        return u_xx + f

    def post_processing(self, x, mu, w):
        x = x.get_coordinates()
        return x * (1.0 - x) * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, x, mu):
        x = x.get_coordinates()
        k0 = 2 * self.k * torch.pi
        k1 = 2 * (self.k + 1) * torch.pi
        k2 = 2 * (self.k + 2) * torch.pi
        a, b, c = self.get_parameters(mu)
        return (
            a / k0**2 * torch.sin(x * k0)
            + b / k1**2 * torch.sin(x * k1)
            + c / k2**2 * torch.sin(x * k2)
        )
