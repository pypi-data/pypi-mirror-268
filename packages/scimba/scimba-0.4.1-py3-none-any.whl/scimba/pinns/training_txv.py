import copy
from pathlib import Path

import torch

from .. import device
from ..equations import pdes
from ..nets import training_tools
from ..sampling import (
    sampling_ode,
    sampling_parameters,
    sampling_pde,
    sampling_pde_txv,
    uniform_sampling,
)
from .pinn_losses import PinnLossesData


class TrainerPinnKinetic:
    """
    This class construct a trainer to solve a PINNs for time space PDE problem

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

    def __init__(self, pde: pdes.AbstractPDEtxv, network, **kwargs):
        self.pde = pde
        self.network = network

        sampler_for_x = sampling_pde.XSampler(self.pde)
        sampler_for_v = sampling_pde_txv.VSampler(self.pde)
        sampler_for_t = sampling_ode.TSampler(
            sampler=uniform_sampling.UniformSampling, ode=self.pde
        )
        sampler_for_mu = sampling_parameters.MuSampler(
            sampler=uniform_sampling.UniformSampling, model=self.pde
        )

        self.sampler = kwargs.get(
            "sampler",
            sampling_pde_txv.PdeTXVCartesianSampler(
                sampler_for_t, sampler_for_x, sampler_for_v, sampler_for_mu
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

        self.batch_size = kwargs.get("batch_size", 1000)

        self.t_collocation = None
        self.x_collocation = None
        self.v_collocation = None
        self.bc_x_collocation = None
        self.bc_v_collocation = None
        self.mu_collocation = None

    def __call__(
        self, t: torch.Tensor, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        """
        Call the PINN for kinetic equations.

        :param t: sampled times
        :type t: torch.Tensor
        :param x: sampled spatial points
        :type x: torch.Tensor
        :param v: sampled velocity points
        :type v: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the result of the network at (t,mu)
        :rtype: torch.Tensor
        """
        return self.net(t, x, v, mu)

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
        self,
        t: torch.Tensor,
        x: torch.Tensor,
        v: torch.Tensor,
        mu: torch.Tensor,
        **kwargs,
    ) -> torch.Tensor:
        """Compute the PDE residual from sampled times, space points, velocities and parameters.

        This function
            #. evaluates the network at points x and mu
            #. computes its first derivatives at points x and mu
            #. if needed, computes its second derivatives at points x and mu
            #. uses this information to compute the PDE residual

        :param t: sampled times
        :type t: torch.Tensor
        :param x: sampled space points
        :type x: torch.Tensor
        :param x: sampled velocities
        :type x: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the residual of the PDE at (t, x, v, mu)
        :rtype: torch.Tensor
        """

        #  TODO: maybe some of those need "retain_graph=True" in the case
        #        of a xy_derivative (not yet implemented)

        # get the approximation of the unknown function and its derivatives
        w = self.network.setup_w_dict(t, x, v, mu)
        self.network.get_first_derivatives(w, t, x, v)

        # compute the PDE residual and concatenate it, if needed
        pde_residual = self.pde.residual(w, t, x, v, mu, **kwargs)
        if isinstance(pde_residual, torch.Tensor):
            return pde_residual
        elif isinstance(pde_residual, tuple):
            return torch.cat(pde_residual, axis=0)
        else:
            raise ValueError("pde_residual should be a tensor or a tuple of tensors")

    def bc_residual(
        self,
        t: torch.Tensor,
        x: torch.Tensor,
        v: torch.Tensor,
        mu: torch.Tensor,
        **kwargs,
    ) -> torch.Tensor:
        """Compute the residual of the PDE at boundary points.

        :param t: sampled times
        :type t: torch.Tensor
        :param x: sampled boundary points
        :type x: torch.Tensor
        :param v: sampled velocities
        :type v: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the boundary residual of the PDE at (t, x, v, mu)
        :rtype: torch.Tensor
        """

        # compute w and its derivatives
        w = self.network.setup_w_dict(t, x, v, mu)

        # compute the PDE boundary residual and concatenate it, if needed
        pde_bc_residual = self.pde.bc_residual(w, t, x, v, mu, **kwargs)
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
        n_init_collocation = kwargs.get("n_init_collocation", 0)
        n_data = kwargs.get("n_data", 0)

        """
        Define data for computing the data_loss function
        """

        if n_data > 0:
            if self.pde.data_construction == "sampled":
                (
                    self.input_t,
                    self.input_x,
                    self.input_v,
                    self.input_mu,
                ) = self.sampler.sampling(n_data)
                self.output = self.pde.reference_solution(
                    self.input_t, self.input_x, self.input_v, self.input_mu
                )
            else:
                (
                    self.input_t,
                    self.input_x,
                    self.input_v,
                    self.input_mu,
                    self.output,
                ) = self.pde.make_data(n_data)

        try:
            best_loss_value = self.losses.loss.item()
        except AttributeError:
            best_loss_value = 1e10

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

                    """
                    Computation of the loss function of the residual (the pde)
                    """
                    if n_collocation > 0:
                        (
                            self.t_collocation,
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                        ) = self.sampler.sampling(n_collocation)

                        f_out = self.residual(
                            self.t_collocation,
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                        )

                        weights = self.sampler.density(
                            self.t_collocation,
                            self.x_collocation,
                            self.v_collocation,
                            self.mu_collocation,
                        )

                        zeros = torch.zeros_like(f_out)
                        self.losses.update_residual_loss(
                            self.losses.residual_f_loss(f_out / weights, zeros)
                        )

                    if self.losses.bc_loss_bool:
                        (
                            batch_bc_t,
                            batch_bc_x,
                            batch_bc_v,
                            batch_bc_mu,
                        ) = self.sampler.bc_sampling(n_bc_collocation)

                        bc_out = self.bc_residual(
                            batch_bc_t,
                            batch_bc_x,
                            batch_bc_v,
                            batch_bc_mu,
                            **kwargs,
                        )

                        bc_zeros = torch.zeros_like(bc_out)
                        self.losses.update_bc_loss(
                            self.losses.bc_f_loss(bc_out, bc_zeros)
                        )

                    if self.losses.init_loss_bool:
                        (
                            batch_ic_t,
                            batch_ic_x,
                            batch_ic_v,
                            batch_ic_mu,
                        ) = self.sampler.sampling(n_init_collocation)
                        batch_ic_t = batch_ic_t * 0.0

                        bi = self.pde.initial_condition(
                            batch_ic_x, batch_ic_v, batch_ic_mu
                        )
                        w = self.network.setup_w_dict(
                            batch_ic_t, batch_ic_x, batch_ic_v, batch_ic_mu
                        )
                        res = self.losses.init_f_loss(w["w"], bi)
                        self.losses.update_init_loss(res)

                    if self.losses.data_loss_bool:
                        batch_t, batch_x, batch_v, batch_mu, batch_w = (
                            self.input_t[indices],
                            self.input_x[indices],
                            self.input_v[indices],
                            self.input_mu[indices],
                            self.output[indices],
                        )

                        prediction = self.network.get_w(
                            batch_t, batch_x, batch_v, batch_mu
                        )
                        self.losses.update_data_loss(
                            self.losses.data_f_loss(prediction, batch_w)
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

        print(f"epoch {epochs: 5d}: current loss = {self.losses.loss.item():5.2e}")
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

    def plot(self, n_visu=10000, random=False, reference_solution=False):
        x_min = self.pde.space_domain.large_domain.bound[0][0]
        x_max = self.pde.space_domain.large_domain.bound[0][1]
        v_min = self.pde.velocity_domain.bound[0][0]
        v_max = self.pde.velocity_domain.bound[0][1]

        # TODO: take into account the dimension of the PDE:
        #       add a condition -> if self.pde.dimension==1:
        if self.pde.dimension_x > 1:
            raise NotImplementedError("trainer.plot not implemented for dimension 2")

        import matplotlib.pyplot as plt

        x = self.sampler.sampling_x(n_visu)
        v = self.sampler.sampling_v(n_visu)
        mu = self.sampler.mu_sampler.sampling(n_visu)

        tplot = self.pde.t_max
        t = tplot * torch.ones_like(x.get_coordinates())

        parameter_string = ", ".join(
            [f"{mu[0, i].cpu().numpy():2.2f}" for i in range(self.pde.nb_parameters)]
        )

        w_pred = self.network.setup_w_dict(t, x, v, mu)

        if reference_solution:
            w_ex = self.pde.reference_solution(t, x, v, mu)

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
