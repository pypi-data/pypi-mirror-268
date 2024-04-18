from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_x as pinn_x
import scimba.pinns.training_x as training_x
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch
from scimba.equations import domain, pdes

PI = 3.14159265358979323846


class Poisson_2D(pdes.AbstractPDEx):
    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=1,
            parameter_domain=[[0.50000, 0.500001]],
        )

        self.first_derivative = True
        self.second_derivative = True

    def make_data(self, n_data):
        pass

    def bc_residual(self, w, x, mu, **kwargs):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = 72 * PI**2 * alpha * torch.sin(6 * PI * x1) * torch.sin(6 * PI * x2)
        return u_xx + u_yy + f

    def post_processing(self, x, mu, w):
        x1, x2 = x.get_coordinates()
        return x1 * (1 - x1) * x2 * (1 - x2) * w

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        alpha = self.get_parameters(mu)
        return alpha * torch.sin(6 * PI * x1) * torch.sin(6 * PI * x2)


def train_network(network, file_path, pde, epochs, sampler, new_training=True):
    if new_training:
        (
            Path.cwd()
            / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
            / file_path
        ).unlink(missing_ok=True)

    pinns = pinn_x.PINNx(network, pde)
    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(learning_rate=9.5e-3, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinns,
        losses=losses,
        optimizers=optimizers,
        sampler=sampler,
        file_name=file_path,
        batch_size=4000,
    )

    if new_training:
        trainer.train(epochs=epochs, n_collocation=100)


def test_fourier():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = Poisson_2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)
    tlayers = [3, 2]
    network2 = pinn_x.Fourier_x(
        pde=pde, std=1.0, nb_features=tlayers[0], layer_sizes=tlayers
    )
    train_network(network2, "nnfourier", pde, 5, sampler)


def test_multiscale():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = Poisson_2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)
    tlayers = [3, 2]

    network3 = pinn_x.MultiScale_Fourier_x(
        pde=pde, stds=[1.0, 10.0], nb_features=tlayers[0], layer_sizes=tlayers
    )
    train_network(network3, "nnmultiscale", pde, 5, sampler)


def test_siren():
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = Poisson_2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)
    tlayers = [10, 10]

    network4 = pinn_x.Siren_x(pde=pde, w=1.0, layer_sizes=tlayers)
    train_network(network4, "nnsiren", pde, 5, sampler)


test_fourier()
test_siren()
test_multiscale()
