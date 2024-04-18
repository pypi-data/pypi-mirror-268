from pathlib import Path

import scimba.equations.domain as domain
import scimba.equations.pdes as pdes
import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_tx as pinn_tx
import scimba.pinns.training_tx as training_tx
import scimba.sampling.sampling_ode as sampling_ode
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch

PI = 3.14159265358979323846


# +
class LinearizedEuler(pdes.AbstractPDEtx):
    def __init__(
        self,
        tdomain=[0, 0.5],
        xdomain=domain.SquareDomain(1, [[0.0, 2.0]]),
        p_domain=[[]],
    ):
        super().__init__(
            nb_unknowns=2,
            time_domain=tdomain,
            space_domain=xdomain,
            nb_parameters=0,
            parameter_domain=p_domain,
        )

        self.first_derivative_t = True
        self.second_derivative_t = False
        self.first_derivative_x = True
        self.second_derivative_x = False
        self.t_min, self.t_max = self.time_domain

    def residual(self, w, t, x, mu, **kwargs):
        p_t, u_t = self.get_variables(w, "w_t")
        p_x, u_x = self.get_variables(w, "w_x")
        return u_t + p_x, p_t + u_x

    def bc_residual(self, w, t, x, mu, **kwargs):
        p, u = self.get_variables(w)
        return p, u

    def initial_condition(self, x, mu, **kwargs):
        x = x.get_coordinates()

        D = 0.02

        return torch.cat(
            (
                (1 / (4 * PI * D) ** 0.5) * torch.exp(-((x - 1) ** 2) / (4 * D)),
                torch.zeros_like(x),
            ),
            axis=1,
        )

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, x, mu):
        x = x.get_coordinates()

        D = 0.02
        coeff = 1 / (4 * PI * D) ** 0.5

        p_plus_u = coeff * torch.exp(-((x - t - 1) ** 2) / (4 * D))
        p_minus_u = coeff * torch.exp(-((x + t - 1) ** 2) / (4 * D))
        p = (p_plus_u + p_minus_u) / 2
        u = (p_plus_u - p_minus_u) / 2
        return torch.cat((p, u), axis=1)


def test_linearized_euler():
    xdomain = domain.SpaceDomain(1, domain.SquareDomain(1, [[-1.0, 3.0]]))
    pde = LinearizedEuler(tdomain=[0.0, 0.5], xdomain=xdomain)
    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=pde)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeTXCartesianSampler(t_sampler, x_sampler, mu_sampler)

    file_name = "linearized_euler.pth"
    (
        Path.cwd()
        / Path(training_tx.TrainerPINNSpaceTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [5, 3]
    network = pinn_tx.MLP_tx(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_tx.PINNtx(network, pde)

    losses = pinn_losses.PinnLossesData(
        bc_loss_bool=True, init_loss_bool=True, w_res=0.03, w_bc=1.0, w_init=1.0
    )
    optimizers = training_tools.OptimizerData(
        learning_rate=9e-3, decay=0.99, switch_to_LBFGS=True
    )
    trainer = training_tx.TrainerPINNSpaceTime(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=3000,
    )

    trainer.train(
        epochs=10,
        n_collocation=10,
        n_bc_collocation=5,
        n_init_collocation=5,
        n_data=0,
    )

    assert True


test_linearized_euler()
