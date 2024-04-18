import torch

from .domain import SpaceDomain, SquareDomain
from .pdes import AbstractPDEtx


class HeatEquation(AbstractPDEtx):
    r"""
    Equation:

    .. math::

        \frac{du}{dt} - \alpha \frac{d^2u}{dx^2} =0

    sur :math:`x\in [0,2], t\in[,0.03], \alpha\in [0.4,0.7]`

    We learn :math:`u(t,x,\alpha)`

    parametric model :math:`u_{net} = u_0 + x(2-x)t \cdot u_{\theta}(t,x)`
    """

    def __init__(
        self,
        tdomain=[0, 0.03],
        xdomain=SpaceDomain(1, SquareDomain(1, [[0.0, 2.0]])),
        p_domain=[[0.4, 0.7]],
    ):
        super().__init__(
            nb_unknowns=1,
            time_domain=tdomain,
            space_domain=xdomain,
            nb_parameters=1,
            parameter_domain=p_domain,
        )

        self.first_derivative_t = True
        self.second_derivative_t = False
        self.first_derivative_x = True
        self.second_derivative_x = True
        self.t_min, self.t_max = self.time_domain

    def residual(self, w, t, x, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u_xx = self.get_variables(w, "w_xx")
        u_t = self.get_variables(w, "w_t")
        return u_t - alpha * u_xx

    def bc_residual(self, w, t, x, mu, **kwargs):
        u = self.get_variables(w)
        return u

    def initial_condition(self, x, mu, **kwargs):
        x = x.get_coordinates()

        t0 = 0.02
        alpha = self.get_parameters(mu)

        return (1.0 / ((4.0 * torch.pi * alpha * (t0)) ** 0.5)) * torch.exp(
            -((x - 1) ** 2.0) / (4 * alpha * t0)
        )

    def post_processing(self, t, x, mu, w):
        x_ = x.get_coordinates()
        return self.initial_condition(x, mu) + x_ * (2 - x_) * t * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, x, mu):
        x_ = x.get_coordinates()
        t0 = 0.02
        alpha = self.get_parameters(mu)
        return (1.0 / ((4.0 * torch.pi * alpha * (t + t0)) ** 0.5)) * torch.exp(
            -((x_ - 1) ** 2.0) / (4 * alpha * (t + t0))
        )
