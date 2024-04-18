import torch

from scimba.equations.pdes import AbstractPDExv

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"torch loaded; device is {device}")

torch.set_default_dtype(torch.double)
torch.set_default_device(device)

PI = 3.14159265358979323846


class Lap1D_xv(AbstractPDExv):
    r"""

    .. math::

        \nabla (\nabla \cdot u) + u = f

    """

    def __init__(self, x_domain, v_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=x_domain,
            velocity_domain=v_domain,
            nb_parameters=1,
            parameter_domain=[[0.75, 0.75 + 1e-4]],
        )

        self.first_derivative_x = True
        self.second_derivative_x = True
        self.first_derivative_v = True
        self.second_derivative_v = True

    def make_data(self, n_data):
        pass

    def bc_residual(self, w, x, v, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, v, mu, **kwargs):
        alpha = self.get_parameters(mu)
        x = x.get_coordinates()

        u_xx = self.get_variables(w, "w_xx")
        u_v1v1 = self.get_variables(w, "w_v1v1")

        f = 8 * PI**2 * alpha * torch.sin(2 * PI * x) * torch.sin(2 * PI * v)
        return u_xx + u_v1v1 + f

    def post_processing(self, x, v, mu, w):
        x = x.get_coordinates()
        return x * (1 - x) * v * (1 - v) * w

    def reference_solution(self, x, v, mu):
        alpha = self.get_parameters(mu)
        x = x.get_coordinates()
        return alpha * torch.sin(2 * PI * x) * torch.sin(2 * PI * v)
