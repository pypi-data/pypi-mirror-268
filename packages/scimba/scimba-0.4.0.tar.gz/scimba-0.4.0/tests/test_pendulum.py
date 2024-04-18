from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import torch
from scimba.equations import ode_basic
from scimba.equations.pdes import AbstractODE
from scimba.pinns import pinn_t, training_t
from scimba.sampling import sampling_ode, sampling_parameters, uniform_sampling


def test_pendulum():
    ode = ode_basic.AmortizedPendulum()

    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )

    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )

    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "pendulum.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_t.Fourier_t(
        ode=ode, layer_sizes=tlayers, activation_type="sine", nb_features=2, std=0.4
    )
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

    assert True


def test_pendulum_adaptative():
    ode = ode_basic.AmortizedPendulum()
    t_usampler = sampling_ode.TSamplerProgressive(
        sampler=uniform_sampling.UniformSampling, ode=ode, M=10
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "pendulum_adaptive.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    network = pinn_t.RBFNet_t(ode=ode, nb_gaussian=2)
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
    assert True


class HamiltonianPendulum(AbstractODE):
    def __init__(self):
        super().__init__(
            nb_unknowns=2,
            time_domain=[0, 2.0],
            nb_parameters=2,
            parameter_domain=[[1.0, 1.25], [1.0, 1.25]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        c = 0.02
        lam, omega = self.get_parameters(mu)
        du0 = -c * lam * omega * 0.5
        return torch.cat(
            [
                0.5 * torch.ones_like(lam),
                du0 * torch.ones_like(lam),
            ],
            axis=1,
        )

    def residual(self, w, t, mu, **kwargs):
        c = 0.02

        lam, omega = self.get_parameters(mu)

        q, p = self.get_variables(w)
        q_t, p_t = self.get_variables(w, "w_t")

        return q_t - p, p_t + omega**2 * q + 2 * c * lam * omega * p

    def bc_add(self, t, mu, w):
        return torch.zeros_like(w)

    def bc_mul(self, t, mu):
        return 1.0

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        c = 0.02
        lam, omega = self.get_parameters(mu)
        arg = torch.sqrt(1 - c**2 * lam**2)
        return torch.cat(
            [
                0.5 * torch.exp(-c * lam * omega * t) * torch.cos(arg * omega * t),
                -0.5
                * (
                    omega
                    * torch.exp(-c * lam * omega * t)
                    * (
                        arg * torch.sin(arg * omega * t)
                        + c * lam * torch.cos(arg * omega * t)
                    )
                ),
            ],
            axis=1,
        )


def test_hamiltonian_pendulum():
    ode = HamiltonianPendulum()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "hamiltonian_pendulum.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_t.DisMLP_t(ode=ode, layer_sizes=tlayers, activation_type="sine")
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
    assert True


test_pendulum()
test_pendulum_adaptative()
test_hamiltonian_pendulum()
