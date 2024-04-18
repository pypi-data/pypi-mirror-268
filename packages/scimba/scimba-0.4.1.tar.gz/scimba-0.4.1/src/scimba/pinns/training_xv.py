import copy
from pathlib import Path

import torch

from .. import device, sampling
from ..equations import pde_1d_laplacian_xv
from ..nets import training_tools
from ..pinns import pinn_xv
from .pinn_losses import PinnLossesData


class TrainerPINNSpaceVel:
    """
    This class construct a trainer to solve a PINNs for stationary kinetic PDE problem

    :param ode: the ODE considered
    :type network: AbstractPDEx
    :param network: the network used
    :type network: nn.Module
    :param network: the sampler used
    :type network: AbstractSampling
    :param losses: the data class for the loss
    :type losses: PinnLossesData

    :param batch_size: the number of data in each batch
    :type batch_size: int
    :param file_name: the name of the file to save the network
    :type file_name: str
    """

    FOLDER_FOR_SAVED_NETWORKS = "networks"

    def __init__(self, **kwargs):
        self.pde = kwargs.get("pde", pde_1d_laplacian_xv.Lap1D_xv)
        self.network = kwargs.get(
            "network",
            pinn_xv.PINNxv(pinn_xv.MLP_xv(self.pde), self.pde),
        )
        sampler_for_x = sampling.sampling_pde.XSampler(self.pde)
        sampler_for_v = sampling.sampling_pde_txv.VSampler(self.pde)
        sampler_for_mu = sampling.sampling_parameters.MuSampler(
            sampler=sampling.uniform_sampling.UniformSampling, model=self.pde
        )
        self.sampler = kwargs.get(
            "sampler",
            sampling.sampling_pde_txv.PdeXVCartesianSampler(
                sampler_for_x, sampler_for_v, sampler_for_mu
            ),
        )
        self.optimizers = kwargs.get(
            "optimizers", training_tools.OptimizerData(**kwargs)
        )
        self.losses = kwargs.get("losses", PinnLossesData(**kwargs))

        folder_for_saved_networks = Path.cwd() / Path(self.FOLDER_FOR_SAVED_NETWORKS)
        folder_for_saved_networks.mkdir(parents=True, exist_ok=True)

        file_name = kwargs.get("file_name", self.pde.file_name)
        self.file_name = folder_for_saved_networks / file_name
        self.batch_size = kwargs.get("batch_size", 1000)

        self.create_network()
        print(">> load network", self.file_name)
        self.load(self.file_name)

        self.to_be_trained = kwargs.get("to_be_trained", self.to_be_trained)
        self.x_collocation = None
        self.v_collocation = None
        self.bc_x_collocation = None
        self.bc_v_collocation = None
        self.mu_collocation = None

    def __call__(self, x, v, mu):
        """
        Call the PINN in space and velocity.

        :param x: sampled spatial points
        :type x: torch.Tensor
        :param v: sampled velocity points
        :type v: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the result of the network at (x, v, ,mu)
        :rtype: torch.Tensor
        """
        return self.net(x, v, mu)

    def create_network(self):
        """
        Create the neural network and associated optimizers.

        This function creates four elements:
            - self.net, the neural network
            - the optimizer data which init the onr or two optimizer and the
            parameters associated
        """
        self.net = self.network.to(device)
        self.optimizers.create_first_opt(self.net.parameters())

    def load(self, file_name: str):
        """Load the network and optimizers from a file.

        :params file_name: name of the .pth file containing the network, losses and optimizers
        :type file_name: str
        """
        try:
            try:
                checkpoint = torch.load(file_name)
            except RuntimeError:
                checkpoint = torch.load(file_name, map_location=torch.device("cpu"))

            self.net.load_state_dict(checkpoint["model_state_dict"])
            self.optimizers.load(self.net.parameters(), checkpoint)
            self.losses.load(checkpoint)

            self.to_be_trained = False
            print("network loaded")

        except FileNotFoundError:
            self.to_be_trained = True
            print("network was not loaded from file: training needed")

    def save(
        self,
        file_name: str,
        epoch: int,
        net_state: dict,
        loss: torch.Tensor,
    ):
        """Save the network and optimizers to a file."""
        dic1 = {epoch: epoch, "model_state_dict": net_state}
        dic2 = self.optimizers.dict_for_save()
        dic3 = self.losses.dict_for_save(loss)
        dic1.update(dic2)
        dic1.update(dic3)
        torch.save(dic1, file_name)

    def residual(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor, **kwargs: dict
    ) -> torch.Tensor:
        """Compute the PDE residual from sampled space points, velocities and parameters.

        This function
            #. evaluates the network at points x, v and mu
            #. computes its first derivatives at points x, v and mu
            #. if needed, computes its second derivatives at points x, v and mu
            #. uses this information to compute the PDE residual

        :param x: sampled space points
        :type x: torch.Tensor
        :param v: sampled velocity points
        :type v: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the residual of the PDE at (x, v, mu)
        :rtype: torch.Tensor
        """

        # compute w and its derivatives
        w = self.network.setup_w_dict(x, v, mu)
        self.network.get_first_derivatives_x(w, x)
        self.network.get_first_derivatives_v(w, v)

        if self.pde.second_derivative_x:
            self.network.get_second_derivatives_x(w, x)

        if self.pde.second_derivative_v:
            self.network.get_second_derivatives_v(w, v)

        # compute the PDE residual and concatenate it, if needed
        pde_residual = self.pde.residual(w, x, v, mu, **kwargs)
        if isinstance(pde_residual, torch.Tensor):
            return pde_residual
        elif isinstance(pde_residual, tuple):
            return torch.cat(pde_residual, axis=0)
        else:
            raise ValueError("pde_residual should be a tensor or a tuple of tensors")

    def bc_residual(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor, **kwargs: dict
    ) -> torch.Tensor:
        """Compute the residual of the PDE at boundary points.

        :param x: sampled boundary points
        :type x: torch.Tensor
        :param v: sampled velocity points
        :type v: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the boundary residual of the PDE at (x, v, mu)
        :rtype: torch.Tensor
        """

        # compute w
        w = self.network.setup_w_dict(x, v, mu)

        # compute the PDE boundary residual and concatenate it, if needed
        pde_bc_residual = self.pde.bc_residual(w, x, v, mu, **kwargs)
        if isinstance(pde_bc_residual, torch.Tensor):
            return pde_bc_residual
        elif isinstance(pde_bc_residual, tuple):
            return torch.cat(pde_bc_residual, axis=1)
        else:
            raise ValueError("pde_residual should be a tensor or a tuple of tensors")

    def train(self, **kwargs):
        epochs = kwargs.get("epochs", 500)
        n_collocation = kwargs.get("n_collocation", 1_000)
        n_bc_collocation = kwargs.get("n_bc_collocation", 0)
        n_data = kwargs.get("n_data", 0)

        if self.pde.data_construction == "sampled":
            self.input_x, self.input_v, self.input_mu = self.sampler.sampling(n_data)
            self.output = self.pde.reference_solution(
                self.input_x, self.input_v, self.input_mu
            )
        else:
            self.input_x, self.input_v, self.input_mu, self.output = self.pde.make_data(
                n_data
            )

        try:
            best_loss_value = self.losses.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        epoch = 0

        if n_collocation == 0:
            m = self.input_x.size()[0]
        if n_data == 0:
            m = n_collocation
        if n_data > 0 and n_collocation > 0:
            m = min(self.input_x.size()[0], n_collocation)

        self.second_opt_activated = self.optimizers.second_opt is not None

        for epoch in range(epochs):
            permutation = torch.randperm(m)

            for i in range(0, m, self.batch_size):
                indices = permutation[i : i + self.batch_size]

                def closure():
                    if self.second_opt_activated:
                        self.optimizers.second_opt.zero_grad()
                    else:
                        self.optimizers.first_opt.zero_grad()

                    self.losses.init_losses()

                    if n_collocation > 0:
                        (
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                        ) = self.sampler.sampling(n_collocation)
                        f_out = self.residual(
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                            **kwargs,
                        )
                        weights = self.sampler.density(
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                        )
                        zeros = torch.zeros_like(f_out)
                        self.losses.update_residual_loss(
                            self.losses.residual_f_loss(f_out / weights, zeros)
                        )

                    if self.losses.bc_loss_bool:
                        batch_bc_x, batch_bc_v, batch_bc_mu = self.sampler.bc_sampling(
                            n_bc_collocation
                        )
                        bc_out = self.bc_residual(
                            batch_bc_x,
                            batch_bc_v,
                            batch_bc_mu,
                            **kwargs,
                        )
                        bc_zeros = torch.zeros_like(bc_out)
                        self.losses.update_bc_loss(
                            self.losses.bc_f_loss(bc_out, bc_zeros)
                        )

                    if self.losses.data_loss_bool:
                        batch_x, batch_v, batch_mu, batch_y = (
                            self.input_x[indices],
                            self.input_v[indices],
                            self.input_mu[indices],
                            self.output[indices],
                        )
                        prediction = self.network.get_w(batch_x, batch_v, batch_mu)
                        self.losses.update_data_loss(
                            self.losses.data_f_loss(prediction, batch_y)
                        )

                    self.losses.compute_full_loss(self.optimizers,epoch)
                    self.losses.loss.backward(retain_graph=True)
                    return self.losses.loss

                if self.second_opt_activated:
                    self.optimizers.second_opt.step(closure)
                else:
                    closure()
                    self.optimizers.first_opt.step()
                    self.optimizers.scheduler.step()
            self.losses.update_histories()

            if epoch % 500 == 0:
                print(
                    f"epoch {epoch: 5d}: current loss = {self.losses.loss.item():5.2e}"
                )

            if (self.losses.loss.item() < best_loss_value) | (epoch == 0):
                string = (
                    f"epoch {epoch: 5d}: best loss = {self.losses.loss.item():5.2e}"
                )
                if self.optimizers.second_opt_activated:
                    string += "; LBFGS activated"
                print(string)

                best_loss = self.losses.loss.clone()
                best_loss_value = best_loss.item()
                best_net = copy.deepcopy(self.net.state_dict())
                self.optimizers.update_best_opt()

            if epoch == 0:
                initial_loss = self.losses.loss.item()
            else:
                self.optimizers.test_activation_second_opt(
                    self.net.parameters(),
                    self.losses.loss_history,
                    self.losses.loss.item(),
                    initial_loss,
                )

        print(f"epoch {epoch: 5d}: current loss = {self.losses.loss.item():5.2e}")

        try:
            self.save(
                self.file_name,
                epoch,
                best_net,
                best_loss,
            )
            print("load network:", self.file_name)
            self.load(self.file_name)
        except UnboundLocalError:
            print("save not work")
            pass

    def plot(self, n_visu=100000, random=False, reference_solution=False):
        import matplotlib.pyplot as plt

        x = self.sampler.sampling_x(n_visu)
        v = self.sampler.sampling_v(n_visu)
        shape = (n_visu, self.pde.nb_parameters)
        ones = torch.ones(shape)
        mu = torch.mean(self.pde.parameter_domain, axis=1) * ones

        parameter_string = ", ".join(
            [f"{mu[0, i].cpu().numpy():2.2f}" for i in range(self.pde.nb_parameters)]
        )

        w_pred = self.network.setup_w_dict(x, v, mu)
        # first_derivatives = self.network.get_first_derivatives(u, x)
        # self.network.get_second_derivatives(u, x, first_derivatives)
        if reference_solution:
            w_ex = self.pde.reference_solution(x, v, mu)

        x = x.get_coordinates()
        if self.pde.dimension_x == 1:
            _, ax = plt.subplots(2, 2, figsize=(12, 6))
            ax[0, 0] = self.losses.plot(ax[0, 0])

            ax[0, 1].scatter(
                x.detach().cpu().numpy(),
                v.detach().cpu().numpy(),
                s=3,
                c=w_pred["w"][:, 0].detach().cpu().numpy(),
                cmap="gist_ncar",
                label="u_theta(x, y)",
            )
            ax[0, 1].set_title(f"prediction, parameters = {parameter_string}")
            ax[0, 1].legend()

            if reference_solution:
                ax[1, 0].scatter(
                    x.detach().cpu().numpy(),
                    v.detach().cpu().numpy(),
                    s=3,
                    c=w_ex[:, 0].detach().cpu().numpy(),
                    cmap="gist_ncar",
                    label="u_theta(x, y)",
                )

                ax[
                    1,
                    0,
                ].set_title(f"solution, parameters = {parameter_string}")
                ax[1, 0].legend()

                error = torch.abs(w_pred["w"] - w_ex).detach().cpu()

                ax[1, 1].scatter(
                    x.detach().cpu().numpy(),
                    v.detach().cpu().numpy(),
                    s=3,
                    c=error[:, 0],
                    cmap="gist_ncar",
                    label="u_theta(x, y)",
                )

                ax[1, 1].set_title("prediction error")
        plt.show()


# %%
