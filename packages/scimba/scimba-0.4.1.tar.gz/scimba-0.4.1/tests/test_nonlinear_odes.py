from pathlib import Path

import scimba.equations.nonlinear_ode_basic as nonlinear_ode_basic
import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_t as pinn_t
import scimba.pinns.training_t as training_t
import scimba.sampling.sampling_ode as sampling_ode
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.uniform_sampling as uniform_sampling
import torch
from scimba.equations.pdes import AbstractODE


class SimpleNonlinearFirstAndSecondOrderSystemFactored(AbstractODE):
    r"""
    .. math::

        diff(u(t)^2/2,t,2) + diff(u(t)*v(t),t,1)
        - v'(t) + α * u(t) =
        -(α*sin(t*α)*sin(t*β)-cos(t*α)*β*cos(t*β)-α^2*sin(t*α)^2+α^2*cos(t*α)^2-α*cos(t*α))
        diff(v(t)^2/2,t,2) + diff(β*t*u(t),t,1)
        + β * v(t) = -β*(β*sin(t*β)^2-sin(t*β)-β*cos(t*β)^2+t*α*sin(t*α)-cos(t*α))
        u(0)  = 1, v(0)  = 0
        u'(0) = 0, v'(0) = β

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=2,
            time_domain=[0.0, 1.0],
            nb_parameters=2,
            parameter_domain=[[0.5, 1.5], [0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

        def f_t(w: torch.Tensor, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
            u, v = self.get_variables(w)
            α, β = self.get_parameters(mu)
            return torch.cat((u * v, β * t * u), axis=1)

        def f_tt(w: torch.Tensor, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
            u, v = self.get_variables(w)
            return torch.cat((u**2 / 2, v**2 / 2), axis=1)

        self.f_t = f_t
        self.f_tt = f_tt

        self.force_compute_1st_derivatives_in_residual = True

    def initial_condition(self, mu, **kwargs):
        α, β = self.get_parameters(mu)
        return [
            torch.cat((torch.ones_like(α), torch.zeros_like(α)), axis=1),
            torch.cat((torch.zeros_like(α), β), axis=1),
        ]

    def residual(self, w, t, mu, **kwargs):
        α, β = self.get_parameters(mu)

        u, v = self.get_variables(w)
        u_t, v_t = self.get_variables(w, "w_t")
        f_u_t, f_v_t = self.get_variables(w, "f_w_t")
        f_u_tt, f_v_tt = self.get_variables(w, "f_w_tt")

        cos_α = torch.cos(t * α)
        cos_β = torch.cos(t * β)

        sin_α = torch.sin(t * α)
        sin_β = torch.sin(t * β)

        rhs_1 = (
            α * sin_α * sin_β
            - β * cos_β * (1 - cos_α)
            + α**2 * (cos_α**2 - sin_α**2)
            - α * cos_α
        )
        rhs_2 = β * (β * sin_β**2 - sin_β - β * cos_β**2 + t * α * sin_α - cos_α)

        eq_1 = f_u_tt + f_u_t - v_t + α * u + rhs_1
        eq_2 = f_v_tt + f_v_t + β * v + rhs_2

        return eq_1, eq_2

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        α, β = self.get_parameters(mu)
        return torch.cat((torch.cos(α * t), torch.sin(β * t)), axis=1)


def test_nonlinear_ode():
    ode = nonlinear_ode_basic.SimpleNonlinearFirstAndSecondOrderOde()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_t.MLP_t(ode=ode, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_t.PINNt(network, ode)

    losses = pinn_losses.PinnLossesData(init_loss_bool=True, w_res=1.0, w_init=10.0)
    optimizers = training_tools.OptimizerData(
        learning_rate=9e-3, decay=0.992, switch_to_LBFGS=True
    )
    trainer = training_t.TrainerPINNTime(
        ode=ode,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=5, n_collocation=20, n_init_collocation=20)


def test_nonlinear_ode_factored():
    ode = nonlinear_ode_basic.SimpleNonlinearFirstAndSecondOrderOdeFactored()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_t.MLP_t(ode=ode, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_t.PINNt(network, ode)

    losses = pinn_losses.PinnLossesData(init_loss_bool=True, w_res=1.0, w_init=10.0)
    optimizers = training_tools.OptimizerData(
        learning_rate=9e-3, decay=0.992, switch_to_LBFGS=True
    )
    trainer = training_t.TrainerPINNTime(
        ode=ode,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=5, n_collocation=20, n_init_collocation=20)


def test_nonlinear_system_factored():
    ode = SimpleNonlinearFirstAndSecondOrderSystemFactored()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_t.MLP_t(ode=ode, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_t.PINNt(network, ode)

    losses = pinn_losses.PinnLossesData(init_loss_bool=True, w_res=1.0, w_init=10.0)
    optimizers = training_tools.OptimizerData(
        learning_rate=9e-3, decay=0.992, switch_to_LBFGS=True
    )
    trainer = training_t.TrainerPINNTime(
        ode=ode,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=5, n_collocation=20, n_init_collocation=20)


if __name__ == "__main__":
    test_nonlinear_ode()
    test_nonlinear_ode_factored()
    test_nonlinear_system_factored()
