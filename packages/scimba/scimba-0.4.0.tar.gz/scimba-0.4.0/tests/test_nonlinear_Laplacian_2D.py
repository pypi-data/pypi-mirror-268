from pathlib import Path

import scimba.equations.domain as domain
import scimba.equations.pdes as pdes
import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_x as pinn_x
import scimba.pinns.training_x as training_x
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch

PI = 3.14159265358979323846


class FactoredNonlinearPoissonDisk2D(pdes.AbstractPDEx):
    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=1,
            parameter_domain=[[0.5, 1]],
        )

        self.first_derivative = False
        self.second_derivative = True

        self.f_xx = lambda w, x, mu: self.get_variables(w) ** 2 / 2
        self.f_yy = lambda w, x, mu: self.get_variables(w) ** 2 / 2

    def make_data(self, n_data):
        pass

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        f = self.get_parameters(mu)

        u = self.get_variables(w, "w")
        f_u_xx = self.get_variables(w, "f_w_xx")
        f_u_yy = self.get_variables(w, "f_w_yy")

        x1_0, x2_0 = self.space_domain.large_domain.center

        boundary = 1 - (x1 - x1_0) ** 2 - (x2 - x2_0) ** 2
        rhs = (2 * f**2 - 0.5 * f) * boundary - f**2

        return f_u_xx + f_u_yy + u + rhs

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        x1_0, x2_0 = self.space_domain.large_domain.center
        f = self.get_parameters(mu)
        return 0.5 * f * (1 - (x1 - x1_0) ** 2 - (x2 - x2_0) ** 2)


def test_nonlinear_laplacian_disk():
    xdomain = domain.SpaceDomain(2, domain.DiskBasedDomain(2, [0.5, 0.5], 1.0))
    pde = FactoredNonlinearPoissonDisk2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)

    losses = pinn_losses.PinnLossesData(bc_loss_bool=True, w_res=1.0, w_bc=10.0)
    optimizers = training_tools.OptimizerData(learning_rate=5e-2, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=10, n_collocation=10, n_bc_collocation=5, n_data=5)


class NonlinearPoisson2D(pdes.AbstractPDEx):
    r"""

    .. math::

        \frac{d^2u}{dx^2} + \frac{d^2u}{dy^2} + f = 0

    """

    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True

        self.force_compute_1st_derivatives_in_residual = True

        def f_x(w, x, mu):
            x1, x2 = x.get_coordinates()
            u = self.get_variables(w)
            return x2 * u**3 / 6

        def f_y(w, x, mu):
            x1, x2 = x.get_coordinates()
            u = self.get_variables(w)
            return x1 * u**3 / 6

        self.f_x = f_x
        self.f_y = f_y

        self.f_xx = lambda w, x, mu: self.get_variables(w) ** 2 / 8
        self.f_xy = lambda w, x, mu: self.get_variables(w) ** 2 / 16
        self.f_yy = lambda w, x, mu: self.get_variables(w) ** 2 / 8

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)

        u = self.get_variables(w)
        u_x = self.get_variables(w, "w_x")
        f_u_x = self.get_variables(w, "f_w_x")
        f_u_y = self.get_variables(w, "f_w_y")
        f_u_xx = self.get_variables(w, "f_w_xx")
        f_u_xy = self.get_variables(w, "f_w_xy")
        f_u_yy = self.get_variables(w, "f_w_yy")

        sin_x = torch.sin(2 * PI * x1)
        cos_x = torch.cos(2 * PI * x1)

        sin_y = torch.sin(2 * PI * x2)
        cos_y = torch.cos(2 * PI * x2)

        term1 = (sin_x + 2 * PI * cos_x) * sin_y * alpha
        term2 = (
            -PI
            * alpha**3
            * (sin_x**2 * sin_y**2 * (cos_x * x2 * sin_y - x1 * sin_x * cos_y))
        )
        term3 = (
            PI**2
            * alpha**2
            * (
                cos_x**2 * sin_y**2
                + cos_x * sin_x * cos_y * sin_y
                - sin_x**2 * cos_y**2
            )
        )

        rhs = term1 + term2 + term3

        return f_u_xx + f_u_xy - f_u_yy - f_u_x + f_u_y + u_x + u - rhs

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        return alpha * torch.sin(2.0 * PI * x1) * torch.sin(2.0 * PI * x2)


def test_nonlinear_laplacian():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = NonlinearPoisson2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)

    losses = pinn_losses.PinnLossesData(bc_loss_bool=True, w_res=1.0, w_bc=10.0)
    optimizers = training_tools.OptimizerData(learning_rate=5e-2, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=10, n_collocation=10, n_bc_collocation=5, n_data=5)


class NonlinearDivGrad2D(pdes.AbstractPDEx):
    r"""

    .. math::

        div(K grad u) + 10 * u = f

    """

    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True

        def anisotropy_matrix(w, x, mu):
            u = self.get_variables(w)
            x1, x2 = x.get_coordinates()
            alpha = self.get_parameters(mu)

            return torch.cat((u**2, -(x1 + 1) * u, -alpha * u, u**2), axis=1)

        self.anisotropy_matrix = anisotropy_matrix

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        α = self.get_parameters(mu)

        u = self.get_variables(w)
        div_K_grad_u = self.get_variables(w, "div_K_grad_w")

        sin_x = torch.sin(PI * x1)
        cos_x = torch.cos(PI * x1)

        sin_y = torch.sin(PI * x2)
        cos_y = torch.cos(PI * x2)

        rhs = (
            -sin_x
            * sin_y
            * α
            * (
                2 * PI**2 * sin_x**2 * sin_y**2 * α**2
                - 2 * PI**2 * cos_x**2 * sin_y**2 * α**2
                - 2 * PI**2 * sin_x**2 * cos_y**2 * α**2
                + 2 * PI**2 * cos_x * cos_y * α**2
                + PI * sin_x * cos_y * α
                + 2 * PI**2 * x1 * cos_x * cos_y * α
                + 2 * PI**2 * cos_x * cos_y * α
                - 10
            )
        )

        return div_K_grad_u + 10 * u - rhs

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        return alpha * torch.sin(PI * x1) * torch.sin(PI * x2)

    def post_processing(self, x, mu, w):
        x1, x2 = x.get_coordinates()
        return x1 * (1 - x1) * x2 * (1 - x2) * w


def test_nonlinear_div_grad():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = NonlinearDivGrad2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)

    losses = pinn_losses.PinnLossesData(bc_loss_bool=True, w_res=1.0, w_bc=10.0)
    optimizers = training_tools.OptimizerData(learning_rate=1e-2, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=10, n_collocation=10)


class Nonlinear2DSystem(pdes.AbstractPDEx):
    r"""

    .. math::

        TODO

    """

    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=2,
            space_domain=space_domain,
            nb_parameters=2,
            parameter_domain=[[0.5, 1.0], [0.5, 1.0]],
        )

        self.first_derivative = True
        self.second_derivative = True

        def f_x(w, x, mu):
            u, v = self.get_variables(w)
            return torch.cat([u**2 / (2 * PI), u * v / (2 * PI)], axis=1)

        def f_y(w, x, mu):
            u, v = self.get_variables(w)
            return torch.cat([u * v / (2 * PI), v**2 / (2 * PI)], axis=1)

        def f_xx(w, x, mu):
            x1, x2 = x.get_coordinates()
            alpha, beta = self.get_parameters(mu)
            u, v = self.get_variables(w)
            return torch.cat(
                [-x2 * u / (alpha * PI**2), -x2 * v / (beta * PI**2)], axis=1
            )

        def f_xy(w, x, mu):
            u, v = self.get_variables(w)
            return torch.cat([u**2 / (4 * PI**2), v**2 / (4 * PI**2)], axis=1)

        def f_yy(w, x, mu):
            x1, x2 = x.get_coordinates()
            alpha, beta = self.get_parameters(mu)
            u, v = self.get_variables(w)
            return torch.cat(
                [x1 * v / (beta * PI**2), x1 * u / (alpha * PI**2)], axis=1
            )

        self.f_x = f_x
        self.f_y = f_y
        self.f_xx = f_xx
        self.f_xy = f_xy
        self.f_yy = f_yy

    def bc_residual(self, w, x, mu, **kwargs):
        u, v = self.get_variables(w)
        return u, v

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        alpha, beta = self.get_parameters(mu)

        u, v = self.get_variables(w)
        f_u_x, f_v_x = self.get_variables(w, "f_w_x")
        f_u_y, f_v_y = self.get_variables(w, "f_w_y")
        f_u_xx, f_v_xx = self.get_variables(w, "f_w_xx")
        f_u_xy, f_v_xy = self.get_variables(w, "f_w_xy")
        f_u_yy, f_v_yy = self.get_variables(w, "f_w_yy")

        sin_x = torch.sin(PI * x1)
        cos_x = torch.cos(PI * x1)

        sin_y = torch.sin(PI * x2)
        cos_y = torch.cos(PI * x2)

        rhs_1 = (
            sin_x
            * sin_y
            * (
                sin_x * cos_y * alpha * beta
                + cos_x * sin_y * alpha**2
                + cos_x * cos_y * alpha**2
                + alpha
                + x2
                - x1
            )
        )

        rhs_2 = (
            sin_x
            * sin_y
            * (
                sin_x * cos_y * beta**2
                + cos_x * cos_y * beta**2
                + cos_x * sin_y * alpha * beta
                + beta
                + x2
                - x1
            )
        )

        return (
            f_u_xx + f_u_xy + f_u_yy + f_u_x + f_u_y + u - rhs_1,
            f_v_xx + f_v_xy + f_v_yy + f_v_x + f_v_y + v - rhs_2,
        )

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        alpha, beta = self.get_parameters(mu)
        return torch.cat(
            (
                alpha * torch.sin(PI * x1) * torch.sin(PI * x2),
                beta * torch.sin(PI * x1) * torch.sin(PI * x2),
            ),
            axis=1,
        )


def test_nonlinear_system():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = Nonlinear2DSystem(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)

    losses = pinn_losses.PinnLossesData(bc_loss_bool=True, w_res=1.0, w_bc=5.0)
    optimizers = training_tools.OptimizerData(learning_rate=5e-2, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=3, n_collocation=10, n_bc_collocation=5)

    # trainer.plot(2)
    # trainer.plot_derivative_mu(n_visu=2)
    # trainer.plot_derivative_xmu(n_visu=2)


test_nonlinear_laplacian_disk()
test_nonlinear_laplacian()
test_nonlinear_div_grad()
test_nonlinear_system()
