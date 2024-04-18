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
        self.sdf = space_domain.large_domain.sdf

    def make_data(self, n_data):
        pass

    def bc_residual(self, w, x, mu, **kwargs):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = 1.0
        return u_xx + u_yy + f

    def post_processing(self, x, mu, w):
        # x1, x2 = x.get_coordinates()
        return self.sdf(x) * w

    def reference_solution(self, x, mu):
        return x.get_coordinates()


class Circle2(domain.SignedDistance):
    def __init__(self):
        super().__init__(dim=2)

    def sdf(self, x):
        x1, x2 = x.get_coordinates()
        ones = torch.ones_like(x1)
        res = (x1 - 0.5) ** 2 + (x2 - 0.5) ** 2 - ones
        return res


def test_adf():
    sdf = domain.PolygonalApproxSignedDistance(
        2,
        [[0.0, -0.5], [0.0, 0.5], [0.5, 0.5], [0.5, 0.0], [1.0, 0.0], [1.0, -0.5]],
        threshold=0.015,
    )
    bound_box = [[-1.0, 2.0], [-1.0, 2.0]]
    xdomain = domain.SpaceDomain(2, domain.SignedDistanceBasedDomain(2, bound_box, sdf))

    pde = Poisson_2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test_sdf.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)
    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(learning_rate=5e-2, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=5000,
    )

    trainer.train(epochs=2, n_collocation=5, n_data=0)


test_adf()
