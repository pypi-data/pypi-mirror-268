import torch
from scimba.equations import domain, pdes
from scimba.neuralgalerkin import neural_galerkin_x as ng
from scimba.pinns import pinn_x
from scimba.sampling import sampling_parameters, sampling_pde, uniform_sampling


class AdvectionDiffusion2D(pdes.AbstractPDEx):
    def __init__(self, xdomain, p_domain=[[1.0, 1.00001]]):
        super().__init__(
            nb_unknowns=1,
            space_domain=xdomain,
            nb_parameters=1,
            parameter_domain=p_domain,
        )

        self.first_derivative = True
        self.second_derivative = True

    def bc_residual(self, w, x, mu):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        u_x = self.get_variables(w, "w_x")
        u_y = self.get_variables(w, "w_y")
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        ax = -2.0 * torch.pi * x2  # mu[:,0,None]
        ay = 2.0 * torch.pi * x1  # mu[:,0,None]
        D = 0.02  # mu[:,1,None]
        return -(ax * u_x + ay * u_y - D * (u_xx + u_yy))


def sol_ref(t, x, mu):
    x1, x2 = x.get_coordinates()
    x1_t = 0.4 * torch.cos(2.0 * torch.pi * t[0])
    x2_t = 0.4 * torch.sin(2.0 * torch.pi * t[0])
    D = 0.02  # mu[:,1,None]
    sig0 = 0.1
    c_t = sig0 * sig0 / (4 * D * t + sig0 * sig0)
    sig2 = 4 * D * t + sig0 * sig0
    f = torch.exp(-((x1 - x1_t) ** 2.0 + (x2 - x2_t) ** 2.0) / (sig2))
    return c_t * f + 1.0


def projector_heatsol2D(net):
    state_dict = net.state_dict()
    print(state_dict)
    m = state_dict["net.net.layer.0.activation.0.m"]
    transformed_m = torch.tensor([0.4, 0.0, 1.0])
    m.copy_(transformed_m)
    sig = state_dict["net.net.layer.0.activation.0.sig"]
    transformed_sig = 0.1
    sig.copy_(transformed_sig)
    w = state_dict["net.net.layer.0.layer.weight"]
    transformed_w = 1.0
    w.copy_(transformed_w)
    b = state_dict["net.net.layer.0.layer.bias"]
    transformed_b = 1.0
    b.copy_(transformed_b)


def test_neural_galerkin():
    xdomain = domain.SpaceDomain(2, domain.DiskBasedDomain(2, [0.0, 0.0], 0.7))
    pde = AdvectionDiffusion2D(xdomain=xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    network = pinn_x.RBFNet_x(pde=pde, type_g="isotropic", norm=2, nb_gaussian=1)
    pinn = pinn_x.PINNx(network, pde)

    # create the model
    model = ng.NeuralGalerkin_x(
        pde, x_sampler, mu_sampler, pinn, scheme="rk2", n_points=5
    )

    # solve the problem
    model.compute_initial_data(projector_heatsol2D)
    print(model.network.state_dict())
    model.time_loop(dt=0.05, T=0.2)

    assert True


test_neural_galerkin()
