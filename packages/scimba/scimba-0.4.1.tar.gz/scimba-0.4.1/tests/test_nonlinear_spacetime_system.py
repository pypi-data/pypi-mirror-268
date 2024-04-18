from pathlib import Path

import scimba.pinns.pinn_tx as pinn_tx
import scimba.pinns.training_tx as training_tx
import torch
from scimba.equations import domain, pdes
from scimba.sampling import (
    sampling_ode,
    sampling_parameters,
    sampling_pde,
    uniform_sampling,
)

PI = 3.14159265358979323846


class NonlinearSystem(pdes.AbstractPDEtx):
    def __init__(
        self,
        tdomain=[0.0, 1.0],
        xdomain=domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]])),
        p_domain=[[0.5, 1.0], [0.5, 1.0]],
    ):
        super().__init__(
            nb_unknowns=2,
            time_domain=tdomain,
            space_domain=xdomain,
            nb_parameters=2,
            parameter_domain=p_domain,
        )

        self.first_derivative_t = True
        self.second_derivative_t = True
        self.first_derivative_x = True
        self.second_derivative_x = True

        self.t_min, self.t_max = self.time_domain

        def f_t(w, t, x, mu):
            u, v = self.get_variables(w)
            α, β = self.get_parameters(mu)
            return torch.cat([u**2 / (2 * α**2), v**2 / (2 * β**2)], axis=1)

        def f_x(w, t, x, mu):
            u, v = self.get_variables(w)
            α, β = self.get_parameters(mu)
            return torch.cat([u**2 / (2 * α**2 * PI), u * v / (2 * α * β * PI)], axis=1)

        def f_y(w, t, x, mu):
            u, v = self.get_variables(w)
            α, β = self.get_parameters(mu)
            return torch.cat([u * v / (2 * α * β * PI), v**2 / (2 * β**2 * PI)], axis=1)

        def f_tt(w, t, x, mu):
            x1, x2 = x.get_coordinates()
            α, β = self.get_parameters(mu)
            u, v = self.get_variables(w)
            return torch.cat([u * v / (α * β), u * v / (α * β)], axis=1)

        def f_xx(w, t, x, mu):
            x1, x2 = x.get_coordinates()
            α, β = self.get_parameters(mu)
            u, v = self.get_variables(w)
            return torch.cat([-x2 * u / (α * PI**2), -x2 * v / (β * PI**2)], axis=1)

        def f_xy(w, t, x, mu):
            u, v = self.get_variables(w)
            α, β = self.get_parameters(mu)
            return torch.cat([u**2 / (2 * α * PI) ** 2, v**2 / (2 * β * PI)], axis=1)

        def f_yy(w, t, x, mu):
            x1, x2 = x.get_coordinates()
            α, β = self.get_parameters(mu)
            u, v = self.get_variables(w)
            return torch.cat([x1 * v / (β * PI**2), x1 * u / (α * PI**2)], axis=1)

        self.f_t = f_t
        self.f_x = f_x
        self.f_y = f_y
        self.f_tt = f_tt
        self.f_xx = f_xx
        self.f_xy = f_xy
        self.f_yy = f_yy

    def residual(self, w, t, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        α, β = self.get_parameters(mu)

        u, v = self.get_variables(w)
        f_u_t, f_v_t = self.get_variables(w, "f_w_t")
        f_u_x, f_v_x = self.get_variables(w, "f_w_x")
        f_u_y, f_v_y = self.get_variables(w, "f_w_y")
        f_u_tt, f_v_tt = self.get_variables(w, "f_w_tt")
        f_u_xx, f_v_xx = self.get_variables(w, "f_w_xx")
        f_u_xy, f_v_xy = self.get_variables(w, "f_w_xy")
        f_u_yy, f_v_yy = self.get_variables(w, "f_w_yy")

        sin_x = torch.sin(PI * x1)
        cos_x = torch.cos(PI * x1)

        sin_y = torch.sin(PI * x2)
        cos_y = torch.cos(PI * x2)

        exp_t = torch.exp(t)
        exp_2t = torch.exp(2 * t)

        rhs_1 = (
            sin_x
            * sin_y
            * (
                exp_2t * α
                - exp_t * α
                - exp_t * sin_x * sin_y
                + 3 * sin_x * sin_y
                + exp_2t * cos_x * sin_y
                - 2 * exp_t * cos_x * sin_y
                + cos_x * sin_y
                + exp_2t * sin_x * cos_y
                - 2 * exp_t * sin_x * cos_y
                + sin_x * cos_y
                + exp_2t * cos_x * cos_y
                - 2 * exp_t * cos_x * cos_y
                + cos_x * cos_y
                + exp_2t * x2
                - exp_t * x2
                - exp_2t * x1
                + exp_t * x1
            )
            / exp_2t
        )

        rhs_2 = (
            sin_x
            * sin_y
            * (
                exp_2t * β
                - exp_t * β
                - exp_t * sin_x * sin_y
                + 3 * sin_x * sin_y
                + exp_2t * cos_x * sin_y
                - 2 * exp_t * cos_x * sin_y
                + cos_x * sin_y
                + exp_2t * sin_x * cos_y
                - 2 * exp_t * sin_x * cos_y
                + sin_x * cos_y
                + exp_2t * cos_x * cos_y
                - 2 * exp_t * cos_x * cos_y
                + cos_x * cos_y
                + exp_2t * x2
                - exp_t * x2
                - exp_2t * x1
                + exp_t * x1
            )
            / exp_2t
        )

        return (
            f_u_tt + f_u_t + f_u_xx + f_u_xy + f_u_yy + f_u_x + f_u_y + u - rhs_1,
            f_u_tt + f_u_t + f_v_xx + f_v_xy + f_v_yy + f_v_x + f_v_y + v - rhs_2,
        )

    def bc_residual(self, w, t, x, mu, **kwargs):
        u, v = self.get_variables(w)
        return u, v

    def initial_condition(self, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        α, β = self.get_parameters(mu)

        sin_x_sin_y = torch.sin(PI * x1) * torch.sin(PI * x2)

        return [
            torch.cat((0 * α, 0 * β), axis=1),
            torch.cat((α * sin_x_sin_y, β * sin_x_sin_y), axis=1),
        ]

    def reference_solution(self, t, x, mu):
        x1, x2 = x.get_coordinates()
        α, β = self.get_parameters(mu)
        return torch.cat(
            (
                α * torch.sin(PI * x1) * torch.sin(PI * x2) * (1 - torch.exp(-t)),
                β * torch.sin(PI * x1) * torch.sin(PI * x2) * (1 - torch.exp(-t)),
            ),
            axis=1,
        )


def test_nonlinear_system():
    pde = NonlinearSystem()
    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=pde)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeTXCartesianSampler(t_sampler, x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_tx.TrainerPINNSpaceTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_tx.MLP_tx(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_tx.PINNtx(network, pde)

    trainer = training_tx.TrainerPINNSpaceTime(
        pde=pde,
        network=pinn,
        sampler=sampler,
        file_name=file_name,
        learning_rate=9e-3,
        decay=0.99,
        bc_loss_bool=True,
        init_loss_bool=True,
        batch_size=3000,
        w_res=0.02,
        w_bc=1,
        w_init=1,
        w_data=0.5,
        switch_to_LBFGS=True,
    )

    trainer.train(
        epochs=2, n_collocation=10, n_bc_collocation=5, n_init_collocation=5, n_data=5
    )


test_nonlinear_system()
