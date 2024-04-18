"""
This module contains a class for training a PINN
approximating the solution to a parametric ODE.
"""

import copy
from pathlib import Path

import torch

from .. import device
from ..equations import ode_basic
from ..nets import training_tools
from ..sampling import sampling_ode, uniform_sampling
from . import pinn_t
from .pinn_losses import PinnLossesData


class TrainerPINNTime:
    """
    This class construct a trainer to solve a PINNs for ODE problem

    :param ode: the ODE considered
    :type network: AbstractOde
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
        self.ode = kwargs.get("ode", ode_basic.SimpleOde())
        self.network = kwargs.get(
            "network",
            pinn_t.PINNt(pinn_t.MLP_t(ode=self.ode), self.ode),
        )
        self.sampler = kwargs.get(
            "sampler",
            sampling_ode.OdeFullSampler(
                sampler=uniform_sampling.UniformSampling, ode=self.ode
            ),
        )
        self.optimizers = kwargs.get(
            "optimizers", training_tools.OptimizerData(**kwargs)
        )
        self.losses = kwargs.get("losses", PinnLossesData(**kwargs))

        folder_for_saved_networks = Path.cwd() / Path(self.FOLDER_FOR_SAVED_NETWORKS)
        folder_for_saved_networks.mkdir(parents=True, exist_ok=True)

        file_name = kwargs.get("file_name", self.ode.file_name)
        self.file_name = folder_for_saved_networks / file_name
        self.batch_size = kwargs.get("batch_size", 1000)

        self.create_network()
        print(">> load network", self.file_name)
        self.load(self.file_name)

        self.to_be_trained = kwargs.get("to_be_trained", self.to_be_trained)
        self.t_collocation = None
        self.mu_collocation = None

    def __call__(self, t: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        """
        Call the PINN in time.

        :param t: sampled times
        :type t: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the result of the network at (t,mu)
        :rtype: torch.Tensor
        """
        return self.net(t, mu)

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
        """
        Load the network and optimizers from a file.

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
        """
        save the network and optimizers to a file.

        :params file_name: name of the .pth file containing the network, losses and optimizers
        :type file_name: str
        :params epoch: the current epoch index
        :type: int
        :params net_state: the dictionary of the current network
        :type: dict
        :params loss: the current value of the loss
        :type: torch.Tensor
        """
        dic1 = {epoch: epoch, "model_state_dict": net_state}
        dic2 = self.optimizers.dict_for_save()
        dic3 = self.losses.dict_for_save(loss)
        dic1.update(dic2)
        dic1.update(dic3)
        torch.save(dic1, file_name)

    def residual(
        self, t: torch.Tensor, mu: torch.Tensor, **kwargs: dict
    ) -> torch.Tensor:
        """
        Compute the ODE residual from sampled space points and parameters.

        This function
            #. evaluates the network at points t and mu
            #. computes its first derivatives at points t and mu
            #. if needed, computes its second derivatives at points t and mu
            #. uses this information to compute the PDE residual

        :param t: sampled times
        :type t: torch.Tensor
        :param mu: sampled parameters
        :type mu: torch.Tensor
        :return: the residual of the PDE at (t, mu)
        :rtype: torch.Tensor
        """

        # get the approximation of the unknown function
        w = self.network.setup_w_dict(t, mu)

        # the remainder of the function has to compute
        # d(f_t(w)) / dt and d^2(f_tt(w)) / dt^2

        # computation of the first derivatives
        if self.ode.first_derivative:
            # compute dw / dt
            if (
                self.ode.force_compute_1st_derivatives_in_residual
                or self.ode.force_compute_2nd_derivatives_in_residual
            ):
                self.network.get_first_derivatives(w, t)

            # compute d(f_t(w)) / dt
            if not self.ode.f_t_is_identity:
                self.network.get_first_derivatives_f(w, t, mu, self.ode.f_t)

        # computation of the second derivatives
        if self.ode.second_derivative:
            # compute d^2w / dt^2
            if self.ode.force_compute_2nd_derivatives_in_residual:
                self.network.get_second_derivatives(w, t)

            # compute d^2(f_tt(w)) / dt^2
            if not self.ode.f_tt_is_identity:
                self.network.get_second_derivatives_f(w, t, mu, self.ode.f_tt)

        # compute the ODE residual and concatenate it, if needed
        ode_residual = self.ode.residual(w, t, mu, **kwargs)
        if isinstance(ode_residual, torch.Tensor):
            return ode_residual
        elif isinstance(ode_residual, tuple):
            return torch.cat(ode_residual, axis=0)
        else:
            raise ValueError("ode_residual should be a tensor or a tuple of tensors")

    def train(self, **kwargs):
        """
        Main training loop.

            This function computes the values of the loss function
            (made of data, PDE, and boudary losses),
            and uses automatic differentiation to optimize
            the parameters of the neural network.

            :params epochs: the number of epoch
            :type epochs: int
            :params n_collocation: the number of collocation points
            :type n_collocation: int
            :params n_init_collocation: the number of collocation points for initial data
            :type n_init_collocation: int
            :params n_data: the number of data
            :type: int
        """
        epochs = kwargs.get("epochs", 500)
        n_collocation = kwargs.get("n_collocation", 1_000)
        n_init_collocation = kwargs.get("n_init_collocation", 0)
        n_data = kwargs.get("n_data", 0)

        if self.losses.init_loss_bool and n_init_collocation == 0:
            raise ValueError("n_init_collocation must be > 0 if init_loss_bool is True")

        if n_data > 0 and self.losses.data_loss_bool:
            if self.ode.data_construction == "sampled":
                self.input_t, self.input_mu = self.sampler.sampling(n_data)
                self.output = self.ode.reference_solution(self.input_t, self.input_mu)
            else:
                self.input_t, self.input_mu, self.output = self.ode.make_data(n_data)

        try:
            best_loss_value = self.losses.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        epoch = 0

        if n_collocation == 0:
            m = self.input_t.size()[0]
        if n_data == 0:
            m = n_collocation
        if n_data > 0 and n_collocation > 0:
            m = min(self.input_t.size()[0], n_collocation)

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
                        self.t_collocation, self.mu_collocation = self.sampler.sampling(
                            n_collocation
                        )
                        f_out = self.residual(
                            self.t_collocation,
                            self.mu_collocation,
                            **kwargs,
                        )
                        weights = self.sampler.density(
                            self.t_collocation,
                            self.mu_collocation,
                        )
                        zeros = torch.zeros_like(f_out)
                        self.losses.update_residual_loss(
                            self.losses.residual_f_loss(f_out / weights, zeros)
                        )

                    if self.losses.init_loss_bool:
                        batch_bc_t, batch_bc_mu = self.sampler.sampling(
                            n_init_collocation
                        )
                        batch_bc_t = batch_bc_t * 0.0
                        w = self.network.setup_w_dict(batch_bc_t, batch_bc_mu)
                        bi = self.ode.initial_condition(batch_bc_mu, **kwargs)

                        if not self.ode.second_derivative:
                            res = self.losses.init_f_loss(w["w"], bi)
                        else:
                            self.network.get_first_derivatives(w, batch_bc_t)
                            init_loss_on_w = self.losses.init_f_loss(w["w"], bi[0])
                            init_loss_on_w_t = self.losses.init_f_loss(w["w_t"], bi[1])
                            res = init_loss_on_w + init_loss_on_w_t
                        self.losses.update_init_loss(res)

                    if n_data > 0:
                        batch_t, batch_mu, batch_y = (
                            self.input_t[indices],
                            self.input_mu[indices],
                            self.output[indices],
                        )
                        prediction = self.network.get_w(batch_t, batch_mu)
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

                if self.sampler.coupling_training:
                    self.sampler.training_to_sampler(self.losses)

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

    def plot(self, random: bool = False, reference_solution: bool = False):
        """
        Plotting function; uses matplotlib.

        Plots the value of the prediction of the ODE solution,
        compared with a reference solution.

        :params random: do we choose the average value of parameters or a random value
        :type random: bool
        :params reference_solution: do we plot a reference solution
        :type reference_solution: bool
        """
        import matplotlib.pyplot as plt

        _, ax = plt.subplots(1, 3, figsize=(15, 5))
        ax[0] = self.losses.plot(ax[0])

        n_visu = 500

        t = torch.linspace(self.ode.t_min, self.ode.t_max, n_visu)[:, None]

        shape = (n_visu, self.ode.nb_parameters)
        ones = torch.ones(shape)
        if random:
            _, mu = self.sampler.sampling(1)
            mu = mu * ones
        else:
            mu = torch.mean(self.ode.parameter_domain, axis=1) * ones

        parameter_string = ", ".join(
            [
                f"{mu[0, i].detach().cpu().numpy():2.2f}"
                for i in range(self.ode.nb_parameters)
            ]
        )

        w_pred = self.network.get_w(t, mu)
        ax[1].plot(t.cpu(), w_pred[:, 0].detach().cpu(), label="prediction")
        if reference_solution:
            w_ex = self.ode.reference_solution(t, mu)
            ax[1].plot(t.cpu(), w_ex[:, 0].detach().cpu(), label="exact")

        ax[1].set_title(f"prediction, parameters = {parameter_string}")
        ax[1].legend()

        if reference_solution:
            error = torch.abs(w_pred - w_ex)[:, 0].detach().cpu()

            ax[2].plot(t.cpu(), error)
            ax[2].set_title("prediction error")
        plt.show()
