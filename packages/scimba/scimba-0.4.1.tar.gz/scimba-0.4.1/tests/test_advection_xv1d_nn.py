import scimba.equations.domain as domain
import scimba.equations.pdes as pdes
import scimba.neuralgalerkin.neural_galerkin_xv as ng
import scimba.pinns.pinn_xv as pinn_xv
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.sampling_pde_txv as sampling_pde_txv
import scimba.sampling.uniform_sampling as uniform_sampling
import torch

PI = 3.14159265358979323846


class Advection_xv_1D(pdes.AbstractPDExv):
    def __init__(self, xdomain, vdomain, p_domain=[[1.0, 1.00001]]):
        super().__init__(
            nb_unknowns=1,
            space_domain=xdomain,
            velocity_domain=vdomain,
            nb_parameters=1,
            parameter_domain=p_domain,
        )

        self.first_derivative_x = True
        self.first_derivative_v = True
        self.second_derivative_x = False
        self.second_derivative_x = False

    def bc_residual(self, w, x, v, mu):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, v, mu, **kwargs):
        u_x = self.get_variables(w, "w_x")
        u_v1 = self.get_variables(w, "w_v1")
        ax = 1.0
        av = 1.0
        return -(ax * u_x + av * u_v1)


def sol_ref(t, x, v, mu):
    x_ = x.get_coordinates()
    x1_t = 0.5 + t[:, 0]
    x2_t = 0.5 + t[:, 0]
    sig0 = 0.12
    f = torch.exp(-((x_ - x1_t) ** 2.0 + (v - x2_t) ** 2.0) / sig0**2)
    return f + 1.0


def init(x, v, mu, w):
    x_ = x.get_coordinates()
    sig0 = 0.12
    f = torch.exp(-((x_ - 0.5) ** 2.0 + (v - 0.5) ** 2.0) / sig0**2)
    return f + 1.0


def Test_NG_xv():
    xdomain = domain.SpaceDomain(1, domain.SquareDomain(1, [[0.0, 1.0]]))
    vdomain = domain.SquareDomain(1, [[0.0, 1.0]])
    pde = Advection_xv_1D(xdomain=xdomain, vdomain=vdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    v_sampler = sampling_pde_txv.VSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    tlayers = [3, 2]
    network = pinn_xv.MLP_xv(
        pde=pde,
        layer_sizes=tlayers,
        activation_type="tanh",
    )
    pinn = pinn_xv.PINNxv(network, pde, init_net_bool=False)

    # create the model
    model = ng.NeuralGalerkin_xv(
        pde,
        x_sampler,
        v_sampler,
        mu_sampler,
        pinn,
        scheme="rk2",
        type_init=1,
        n_points=10,
        epoch_initial_train=5,
        lr_initial_train=5e-2,
    )

    # solve the problem
    model.compute_initial_data(w0=init)
    model.time_loop(dt=0.005, T=0.01)


Test_NG_xv()
