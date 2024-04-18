from pathlib import Path

import scimba.equations.domain as domain
import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_x as pinn_x
import scimba.pinns.training_x as training_x
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch
from scimba.equations import pdes

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"torch loaded; device is {device}")

PI = 3.14159265358979323846

torch.set_default_dtype(torch.double)
torch.set_default_device(device)


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
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = 1.0
        return u_xx + u_yy + f

    def reference_solution(self, x, mu):
        x1, x2 = x.get_coordinates()
        return 0.0 * x1


def disk_to_potato(x):
    x1, x2 = (x[:, i, None] for i in range(2))
    x = x1 - 0.5 * x2**2 + 0.3 * torch.sin(x2)
    y = x2 + 0.1 * x + 0.12 * torch.cos(x)
    return torch.cat((x, y), axis=1)


def Jacobian_disk_to_potato(x):
    x1, x2 = (x[:, i, None] for i in range(2))
    raise ValueError("Jacobian_disk_to_potato is not implemented")
    return 0, 0, 0, 0


def test_laplacian2D_domainhole():
    # domain creation
    xdomain = domain.DiskBasedDomain(
        2, [0.0, 0.0], 1.0, mapping=disk_to_potato, Jacobian=Jacobian_disk_to_potato
    )
    fulldomain = domain.SpaceDomain(2, xdomain)

    def f(t):
        return torch.cat([torch.cos(2.0 * PI * t), torch.sin(2.0 * PI * t)], axis=1)

    bc1 = domain.ParametricCurveBasedDomain(2, [[0.0, 0.5]], f)
    bc2 = domain.ParametricCurveBasedDomain(2, [[0.5, 1.0]], f)

    fulldomain.add_bc_subdomain(bc1)
    fulldomain.add_bc_subdomain(bc2)

    # Hole and its signed distance function (sdf)
    class Hole(domain.SignedDistance):
        def __init__(self):
            super().__init__(dim=2)

        def sdf(self, x):
            x1, x2 = x.get_coordinates()
            center = [-0.2, -0.2]
            radius = 0.2
            return (x1 - center[0]) ** 2 + (x2 - center[1]) ** 2 - radius**2

    # parametric curve that describes the hole
    def bchole(t):
        center = [-0.2, -0.2]
        radius = 0.2
        return torch.cat(
            [
                center[0] - radius * torch.cos(2 * PI * t),
                center[1] - radius * torch.sin(2 * PI * t),
            ],
            axis=1,
        )

    # Inclusion subdomain and its signed distance function (sdf)
    class Inclusion(domain.SignedDistance):
        def __init__(self):
            super().__init__(dim=2)

        def sdf(self, x):
            x1, x2 = x.get_coordinates()
            center = [0.2, 0.2]
            radius = 0.2
            return (x1 - center[0]) ** 2 + (x2 - center[1]) ** 2 - radius**2

    # parametric curve that describes the inclusion
    def bcinclusion(t):
        center = [0.2, 0.2]
        radius = 0.2
        return torch.cat(
            [
                center[0] - radius * torch.cos(2 * PI * t),
                center[1] - radius * torch.sin(2 * PI * t),
            ],
            axis=1,
        )

    sdf = Hole()
    hole = domain.SignedDistanceBasedDomain(2, [[0.0, 1.0], [0.0, 1.0]], sdf)
    bc_hole = domain.ParametricCurveBasedDomain(2, [[0.0, 1.0]], bchole)
    hole.add_bc_subdomain(bc_hole)

    sdf = Inclusion()
    inc = domain.SignedDistanceBasedDomain(2, [[0.0, 1.0], [0.0, 1.0]], sdf)
    bc_inc = domain.ParametricCurveBasedDomain(2, [[0.0, 1.0]], bcinclusion)
    inc.add_bc_subdomain(bc_inc)

    fulldomain.add_hole(hole)
    fulldomain.add_subdomain(inc)

    # start computations

    pde = Poisson_2D(fulldomain)
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
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="tanh")
    pinn = pinn_x.PINNx(network, pde)
    losses = pinn_losses.PinnLossesData(bc_loss_bool=True, w_res=1.0, w_bc=30.0)
    optimizers = training_tools.OptimizerData(learning_rate=9.0e-3, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=8000,
    )

    trainer.train(epochs=10, n_collocation=10, n_bc_collocation=5, n_data=0)


test_laplacian2D_domainhole()
