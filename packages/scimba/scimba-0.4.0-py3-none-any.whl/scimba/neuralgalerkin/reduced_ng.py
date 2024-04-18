from scimba.pinos import training_x, training_tx
from torch.func import functional_call, jacrev, vmap
import copy
import torch
import matplotlib.pyplot as plt

class ReducedNeuralGalerkin_x:
    def __init__(self, pde_x, x_sampler, mu_sampler, mu_sampler_test, u_sampler, AE, file_name,
                 n_points=500, epochs=100, n_data_f=1, n_data_x=100,
                 p_domain_test=[[0.5, 0.5000001]],
                 projector=None,**kwargs):
        self.pde = pde_x
        self.x_sampler = x_sampler
        self.mu_sampler = mu_sampler
        self.mu_sampler_test = mu_sampler_test
        self.u_sampler = u_sampler
        self.network = AE
        self.file_name = file_name
        self.N = n_points
        self.epochs = epochs
        self.n_data_f = n_data_f
        self.n_data_x = n_data_x
        self.w_data = kwargs.get("w_data", 1.0)
        self.w_res = kwargs.get("w_res", 0.0)
        self.w_bc = kwargs.get("w_bc", 0.0)
        self.w_init = kwargs.get("w_init", 0.0)
        self.switch_to_LBFGS = kwargs.get("switch_to_LBFGS", False)

        self.t_sampler = kwargs.get("t_sampler")

    def sampling(self):
        """
        this method calls the sampling function of the two samplers,
        and saves the number of points
        """
        self.x = self.x_sampler.sampling(self.N)
        # self.x_no_grad = copy.deepcopy(self.x)
        # self.x_no_grad.requires_grad = False
        self.mu_collocation = self.mu_sampler_test.sampling(1)
        self.mu = self.mu_collocation * torch.ones(self.N, 1)
        
    def sampling_time(self):
        """
        this method calls the sampling function of the two samplers,
        and saves the number of points
        """
        self.x = self.x_sampler.sampling(self.N)
        self.x.requires_grad = True
        self.t = self.time * torch.ones(self.N, 1)
        self.t.requires_grad = True
        # self.x_no_grad = copy.deepcopy(self.x)
        # self.x_no_grad.requires_grad = False
        self.mu_collocation = self.mu_sampler_test.sampling(1)
        self.mu = self.mu_collocation * torch.ones(self.N, 1)

    def compute_initial_data(self):

        trainer = training_x.TrainerPINOSpace(
            network=self.network,
            pde=self.pde,
            sampler=self.u_sampler,
            file_name=self.file_name,
            w_data=self.w_data,
            w_res=self.w_res,
            w_bc=self.w_bc,
            w_init=self.w_init,
            switch_to_LBFGS=self.switch_to_LBFGS
        )

        trainer.train(epochs=self.epochs,
                      n_collocation_f=0,
                      n_collocation_x=0,
                      n_data_f=self.n_data_f,
                      n_data_x=self.n_data_x)

        print(f"Training the autoencoder to compute the initial data with \mu = {trainer.input_mu[0].item():5.2e}")

        # We use the points of the f sampling used for the data test (fixed points for deepOnet not necessary for the rest)
        # we use en encoder to find the initialization of reduced parameters

    def jacobian(self, z, x, mu):
        """
        this function compute the Jacobians of the model
        with respect to the weights at each (x,mu) of a tensor
        If we have n points, we have n jacobians J(\theta)(x,mu).
        """
        def Rnet(z, x, mu):
            x.requires_grad=True
            z_in = z * torch.ones(mu.size(0), 1)
            u = self.network.no_net.forward_decoder(x, mu, z)
            up = self.network.post_processing(x, mu, u)
            w = {
                "w": up,
                "w_x": None,
                "w_y": None,
                "w_xx": None,
                "w_yy": None,
            }
            self.network.get_first_derivatives(w, x)

            if self.pde.second_derivative:
                self.network.get_second_derivatives(w, x)

            return self.pde.residual(w, x, mu)

        # (None, 0, 0) means that:
        #   - the first argument (z) is not batched
        #   - the second argument (x) is batched along the first dimension
        #   - the third argument (mu) is batched along the first dimension
        # jac = vmap(jacrev(Rnet), (None, 0, 0))(z, x, mu)
        jac = jacrev(Rnet)(z, x, mu)

        jac = jac.squeeze(2)

        return jac
    
    # def jacobian(self, z, x, mu):
    #     """
    #     this function compute the Jacobians of the model
    #     with respect to the weights at each (x,mu) of a tensor
    #     If we have n points, we have n jacobians J(\theta)(x,mu).
    #     """
    #     def Rnet(z, x, mu):
    #         x.requires_grad=True
    #         u = self.network.no_net.forward_decoder(x.unsqueeze(0), mu.unsqueeze(0), z)
    #         up = self.network.post_processing(x.unsqueeze(0), mu.unsqueeze(0), u)
    #         w = {
    #             "w": up,
    #             "w_x": None,
    #             "w_y": None,
    #             "w_xx": None,
    #             "w_yy": None,
    #         }
    #         self.network.get_first_derivatives(w, x)

    #         if self.pde.second_derivative:
    #             self.network.get_second_derivatives(w, x)

    #         return self.pde.residual(w, x.unsqueeze(0), mu.unsqueeze(0))

    #     # (None, 0, 0) means that:
    #     #   - the first argument (z) is not batched
    #     #   - the second argument (x) is batched along the first dimension
    #     #   - the third argument (mu) is batched along the first dimension
    #     jac = vmap(jacrev(Rnet), (None, 0, 0))(z, x, mu)

    #     jac = jac.squeeze(2)

    #     return jac

    def compute_model(self, z):
        """
        this function compute the mass matrix and the RHS of the Neural Galerkin method
        M(theta)=frac1/N sum (J(theta) otimes J(theta))(x,mu)
        F(theta)=frac1/N sum (J(theta) f(theta))(x,mu)
        """
        jac = self.jacobian(z, self.x, self.mu)

        #z = z * torch.ones(self.mu.size(0), 1)
        u = self.network.no_net.forward_decoder(self.x, self.mu, z)
        up = self.network.post_processing(self.x, self.mu, u)
        w = {
            "w": up,
            "w_x": None,
            "w_y": None,
            "w_xx": None,
            "w_yy": None,
        }
        self.network.get_first_derivatives(w, self.x)

        if self.pde.second_derivative:
            self.network.get_second_derivatives(w, self.x)

        R = self.pde.residual(w, self.x, self.mu)

        jac_t = jac.transpose(1,2)
        M = torch.einsum("bsj,brj->sr", jac_t, jac_t) / self.N #+ 0*1e-9 * torch.eye(z.shape[0])
        F = torch.einsum("bij,bi->j", jac, R) / self.N

        return M, F

    def iterative_method(self, z0, iter_max):

        self.sampling()

        self.z = z0

        print(f"Solve the PDE with Reduced Neural Galerkin with \mu = {self.mu_collocation.item():5.2e}")


        for iter in range(0, iter_max):


            M, F = self.compute_model(self.z)

            # Update the latent variables
            update_z = torch.linalg.solve(M, -F)


            self.z = self.z + update_z
            self.z = self.z.clone().detach().requires_grad_(True)

            # w_pred = torch.sum(z * trunk_res, dim=1)
            # w_pred = pde.post_processing(x, mu, w_pred)
            # err = torch.linalg.vector_norm(
            #     w_pred - w_exact).detach().cpu() / (n_points**0.5)

            print(f"iteration {iter+1: 2d}: update_z = {max(update_z):5.2e}")

        return self.z

    def check_autoencoder(self, u_sampler, n_visu=500, n_plot=3):

        for i in range(0,n_plot):
            
            (vecx,vecu,x,mu_collocation,out) = u_sampler.sampling(n_f=1, n_points=1)
            x = self.x_sampler.sampling(n_visu)
            mu = mu_collocation * torch.ones(n_visu, 1)
            w_pred = self.network.get_w(vecx, vecu, x, mu)
            #w_pred = self.network.post_processing(x, mu, w)
    
    
    
            plt.scatter(
                x.detach().cpu().numpy(),
                w_pred.detach().cpu().numpy(),s=5,
                label="Autoencoder \mu="
                + str(round(mu_collocation.item(), 2)),
            )
            # plt.scatter(t_collocation.detach().numpy(), f.detach().numpy(), label="f")
    
            x = torch.linspace(self.pde.space_domain.bound[0][0],
                               self.pde.space_domain.bound[0][1],
                               n_visu)[:, None]
    
            w_exact = self.pde.reference_solution(x, mu)
    
            plt.plot(
                x.detach().cpu().numpy(),
                w_exact.detach().cpu().numpy(),
                label="Ref \mu=" + str(round(mu_collocation.item(), 2)),
                color="black",
            )
        plt.legend()

    def plot(self, n_visu):

        x = self.x_sampler.sampling(n_visu)
        mu = self.mu_collocation * torch.ones(n_visu, 1)
        z = self.z * torch.ones(n_visu, 1) 
        w = self.network.no_net.forward_decoder(x, mu, z)
        w_pred = self.network.post_processing(x, mu, w)

        plt.scatter(
            x.detach().cpu().numpy(),
            w_pred.detach().cpu().numpy(),s=5,
            label="Reduced NG mu="
            + str(round(self.mu_collocation.item(), 2)),
        )
        # plt.scatter(t_collocation.detach().numpy(), f.detach().numpy(), label="f")

        x = torch.linspace(self.pde.space_domain.bound[0][0],
                           self.pde.space_domain.bound[0][1],
                           n_visu)[:, None]

        w_exact = self.pde.reference_solution(x, mu)

        plt.plot(
            x.detach().cpu().numpy(),
            w_exact.detach().cpu().numpy(),
            label="Ref \mu=" + str(round(self.mu_collocation.item(), 2)),
            color="blue",
        )
        plt.legend()
