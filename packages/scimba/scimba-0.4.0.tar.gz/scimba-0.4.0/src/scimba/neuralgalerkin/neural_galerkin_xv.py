import copy

# import time
import torch
from torch.func import functional_call, jacrev, vmap

import scimba.sampling.sampling_pde_txv as sampling_pde_txv

from .. import device
from . import projector_training

# Here the network depend of space and physical parameters
# The weights of the network evolve in time,
# The class needs
# a PDE which gives the domain, the spatial and unknowns dimension
# a parametric model (call here networks)
# objects to sample space and parameters
# a type of initialization method
# a name of time scheme


class NeuralGalerkin_xv:
    def __init__(self, pde_xv, sampler_x, sampler_v, sampler_mu, network, **kwargs):
        self.pde = pde_xv
        self.sampler_x = sampler_x
        self.sampler_v = sampler_v
        self.sampler_mu = sampler_mu
        self.network = copy.deepcopy(network)
        # self.network_backup = copy.deepcopy(network)
        self.type_init = kwargs.get("type_init", 0)
        self.scheme = kwargs.get("scheme", "euler_ex")
        self.N = kwargs.get("n_points", 1000)
        self.matrix_regularization = kwargs.get("matrix_regularization", 1e-6)
        self.epoch = kwargs.get("epoch_initial_train", 500)
        self.lr = kwargs.get("lr_initial_train", 1e-3)

        nb_params = len(torch.nn.utils.parameters_to_vector(self.network.parameters()))
        print("number of parameters", nb_params)

    def compute_initial_data(self, projector=None, w0=None):
        """
        3 ways of computing the initial data:
        - we gives a projector which gives explicitly the init weights
        - we make a learning step
        - we put the inital condition int the model with bc add (Hesthaven style);
        this requires storing the initial condition
        """
        if self.type_init == 0:
            projector(self.network)
        if self.type_init == 1:
            self.sampler = sampling_pde_txv.PdeXVCartesianSampler(
                self.sampler_x, self.sampler_v, self.sampler_mu
            )
            self.projector = projector_training.Projector_xv(
                self.network, self.sampler, w0=w0, learning_rate=self.lr
            )
            self.projector.train(epochs=self.epoch, n_collocation=5000)
        if self.type_init == 2:
            pass

    def sampling(self):
        """
        this method calls the sampling function of the two samplers,
        and saves the number of points
        """
        self.x = self.sampler_x.sampling(self.N)
        self.x_no_grad = copy.deepcopy(self.x.x)
        self.x_no_grad.requires_grad = False
        self.v = self.sampler_v.sampling(self.N)
        self.v_no_grad = copy.deepcopy(self.v)
        self.v_no_grad.requires_grad = False
        self.mu = self.sampler_mu.sampling(self.N)
        self.mu_no_grad = copy.deepcopy(self.mu)
        self.mu_no_grad.requires_grad = False

    def params_to_vect(self):
        """
        this function takes the current paramaters of the model,
        and concatenates them in the vector theta
        """
        self.theta = torch.nn.utils.parameters_to_vector(self.network.parameters())

    def vect_to_params(self, theta: torch.Tensor):
        """
        this function take a vector theta and put it in the paramaters models
        """
        torch.nn.utils.vector_to_parameters(theta, self.network.parameters())

    def jacobian(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        """
        this function compute the Jacobians of the model
        with respect to the weights at each (x,mu) of a tensor
        If we have n points, we have n jacobians J(\theta)(x,mu).
        """
        params = {k: v.detach() for k, v in self.network.named_parameters()}

        def fnet(theta, x, v, mu):
            return functional_call(
                self.network, theta, (x.unsqueeze(0), v.unsqueeze(0), mu.unsqueeze(0))
            ).squeeze(0)

        # (None, 0, 0) means that:
        #   - the first argument (params) is not batched
        #   - the second argument (x) is batched along the first dimension
        #   - the third argument (v) is batched along the first dimension
        #   - the fourth argument (mu) is batched along the first dimension
        jac = vmap(jacrev(fnet), (None, 0, 0, 0))(params, x, v, mu).values()

        # jac is a dict of jagged tensors, we want to:
        #   - first reshape each jagged tensor to (N, nb_unknowns, nb_params)
        #   - then concatenate them along the last dimension
        return torch.cat(
            [j.reshape((self.N, self.pde.nb_unknowns, -1)) for j in jac], axis=-1
        )

    def compute_model(self):
        """
        this function compute the mass matrix and the RHS of the Neural Galerkin method
        M(theta)=frac1/N sum (J(theta) otimes J(theta))(x,mu)
        F(theta)=frac1/N sum (J(theta) f(theta))(x,mu)
        """
        m_jac = self.jacobian(self.x_no_grad, self.v_no_grad, self.mu_no_grad)

        self.M = torch.einsum("bjs,bjr->sr", m_jac, m_jac) / self.N + self.eye_matrix

        w = self.network.setup_w_dict(self.x, self.v, self.mu)
        self.network.get_first_derivatives_x(w, self.x)
        self.network.get_first_derivatives_v(w, self.v)

        if self.pde.second_derivative_x:
            self.network.get_second_derivatives_x(w, self.x)
        if self.pde.second_derivative_v:
            self.network.get_second_derivatives_v(w, self.v)

        large_f = self.residual(w, self.x, self.v, self.mu)
        self.f = torch.einsum("bji,bj->i", m_jac, large_f) / self.N

    def residual(
        self, w: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        """this function computes the PDE residual and concatenates it, if needed"""
        pde_residual = self.pde.residual(w, x, v, mu)
        if isinstance(pde_residual, torch.Tensor):
            return pde_residual
        elif isinstance(pde_residual, tuple):
            return torch.cat(pde_residual, axis=1)
        else:
            raise ValueError("pde_residual should be a tensor or a tuple of tensors")

    # this function computes the evolution of error of the solution in time
    def compute_error_in_time(self, t, x, v, mu, sol_exact):
        w_pred = self.network.setup_w_dict(x, v, mu)

        w_exact = sol_exact(t, x, v, mu)
        err_abs = torch.linalg.vector_norm(w_pred["w"] - w_exact).detach().cpu() / (
            self.N**0.5
        )

        return err_abs

    def time_step(self, dt):
        self.sampling()
        self.params_to_vect()
        if self.scheme == "euler_exp":
            self.euler_exp(dt)
        if self.scheme == "rk2":
            self.rk2(dt)
        self.list_theta.append(self.theta.detach())
        self.vect_to_params(self.theta)

    def euler_exp(self, dt):
        self.compute_model()
        b = self.f.flatten()
        update = torch.linalg.solve(self.M, b)
        self.theta = self.list_theta[-1] + dt * update

    def rk2(self, dt):
        self.compute_model()
        M = torch.linalg.cholesky(self.M)
        update = torch.cholesky_solve(self.f[:, None], M)[:, 0]
        # b = self.f.flatten()
        # update = torch.linalg.solve(self.M, b)
        self.theta = self.list_theta[-1] + 0.5 * dt * update

        self.vect_to_params(self.theta)
        self.compute_model()
        M = torch.linalg.cholesky(self.M)
        update = torch.cholesky_solve(self.f[:, None], M)[:, 0]
        # b = self.f.flatten()
        # update = torch.linalg.solve(self.M, b)
        self.theta = self.list_theta[-1] + dt * update

    def time_loop(self, dt, T, sol_exact=None):
        self.T = T
        nt = 0
        time = 0
        self.list_theta = []
        self.params_to_vect()

        self.eye_matrix = self.matrix_regularization * torch.eye(self.theta.shape[0])

        self.list_theta.append(self.theta)
        self.times = [0]
        # self.list_err = [0]

        while time < T:
            if time + dt > T:
                dt = T - time
            # if nt % 1 == 0:
            #     print("iteration ", nt, "error", self.list_err[nt])
            self.time_step(dt)
            if sol_exact is not None:
                # err_abs = self.compute_error_in_time(
                #     self, time, self.x_no_grad, self.mu_no_grad, sol_exact
                # )
                w_pred = self.network.setup_w_dict(self.x, self.mu)
                # self.network.get_first_derivatives(w_pred, self.x_no_grad)

                w_exact = sol_exact(time, self.x_no_grad, self.mu_no_grad)
                torch.linalg.vector_norm(
                    w_pred["w"] - w_exact[:, 0:1, None]
                ).detach().cpu() / (self.N**0.5)

                # self.list_err.append(err_abs)
            time = time + dt
            nt = nt + 1
            print("current iteration :", nt)

            self.times.append(time)

    def plot(self, n_visu=20000, sol_exact=None, mu=None):
        import matplotlib.pyplot as plt

        t = torch.ones(n_visu, dtype=torch.double, device=device) * self.T
        t = t[:, None]
        x = self.sampler_x.sampling(n_visu)
        v = self.sampler_v.sampling(n_visu)
        shape = (n_visu, self.pde.nb_parameters)
        ones = torch.ones(shape)

        if self.pde.nb_parameters == 0:
            t_mu = torch.empty(x.size()[0], 0)
        else:
            if mu is None:
                t_mu = torch.mean(self.pde.parameter_domain, axis=1) * ones
            else:
                t_mu = mu * ones

        w_pred = self.network.setup_w_dict(x, v, t_mu)
        self.network.get_first_derivatives_x(w_pred, x)
        self.network.get_first_derivatives_v(w_pred, v)

        if self.pde.dimension_x == 1:
            if sol_exact is not None:
                w_exact = sol_exact(t, x, v, mu)
                print(
                    "erreur ",
                    torch.sum((w_pred["w"] - w_exact) ** 2).detach().cpu()
                    / (self.N**self.pde.dimension_x),
                )

            fig, ax = plt.subplots(2, 2, figsize=(15, 8))
            x = x.get_coordinates()
            im = ax[0, 0].scatter(
                x.detach().cpu().numpy(),
                v.detach().cpu().numpy(),
                s=4,
                c=w_pred["w"][:, 0].detach().cpu().numpy(),
                cmap="gist_ncar",
                label="w_theta(x, y)",
            )
            fig.colorbar(im, ax=ax[0, 0])
            ax[0, 0].set_title("prediction")
            ax[0, 0].legend()

            if sol_exact is not None:
                im = ax[0, 1].scatter(
                    x.detach().cpu().numpy(),
                    v.detach().cpu().numpy(),
                    s=4,
                    c=w_exact[:, 0].detach().cpu().numpy(),
                    cmap="gist_ncar",
                    label="w_ref(x, y)",
                )
            fig.colorbar(im, ax=ax[0, 1])
            ax[0, 1].set_title(" reference")
            ax[0, 1].legend()

            im = ax[1, 0].scatter(
                x.detach().cpu().numpy(),
                v.detach().cpu().numpy(),
                s=10,
                c=w_pred["w_x"][:, 0].detach().cpu().numpy(),
                cmap="gist_ncar",
                label="dx v_theta(x, y)",
            )
            fig.colorbar(im, ax=ax[1, 0])

            ax[1, 0].set_title("dx prediction")
            ax[1, 0].legend()

            im = ax[1, 1].scatter(
                x.detach().cpu().numpy(),
                v.detach().cpu().numpy(),
                s=10,
                c=w_pred["w_v1"][:, 0].detach().cpu().numpy(),
                cmap="gist_ncar",
                label=" dy w_theta(x, y)",
            )
            fig.colorbar(im, ax=ax[1, 1])
            ax[1, 1].set_title("dy prediction")
            ax[1, 1].legend()

        plt.show()
