import copy
from pathlib import Path

import torch

import scimba.sampling.sampling_functions as sampling_functions
import scimba.sampling.sampling_ode as sampling_ode
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.uniform_sampling as uniform_sampling
from scimba.equations import ode_basic
from scimba.nets.training_tools import OptimizerData
from scimba.pinns.pinn_losses import PinnLossesData
from scimba.sampling.data_sampling_ode import ode_data

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

torch.set_default_dtype(torch.double)
torch.set_default_device(device)


class TrainerPINOTime:
    FOLDER_FOR_SAVED_NETWORKS = "networks"

    def __init__(self, **kwargs):
        self.ode = kwargs.get("ode", ode_basic.SimpleOdeWithSource())

        self.network = kwargs.get("network", None)
        if self.network is None:
            raise ValueError("network must be provided to TrainerDeepONetTime")

        self.sampler = kwargs.get("sampler", None)

        if self.sampler is None:
            t_usampler = sampling_ode.TSampler(
                sampler=uniform_sampling.UniformSampling, ode=self.ode
            )
            mu_usampler = sampling_parameters.MuSampler(
                sampler=uniform_sampling.UniformSampling, model=self.ode
            )
            w_initial_usampler = uniform_sampling.UniformSampling(1, [[0.0, 1.0]])
            self.sampler = ode_data(
                sampler_t=t_usampler,
                sampler_params=mu_usampler,
                sampler_initial_condition=w_initial_usampler,
                source=sampling_functions.Default_ParametricFunction_t(),
                n_sensor=70,
                resample_sensors=False,
            )

        self.optimizers = kwargs.get("optimizers", OptimizerData(**kwargs))
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

    def residual(self, sample: ode_data, f: torch.Tensor) -> torch.Tensor:
        t, mu = sample.t_loss, sample.params

        w = self.network.setup_w_dict(t, mu, sample)
        self.network.get_first_derivatives(w, t)

        if self.ode.second_derivative:
            self.network.get_second_derivatives(w, t)

        # compute the ODE residual and concatenate it, if needed
        ode_residual = self.ode.residual(w, t, mu, f=f)
        if isinstance(ode_residual, torch.Tensor):
            return ode_residual
        elif isinstance(ode_residual, tuple):
            return torch.cat(ode_residual, axis=0)
        else:
            raise ValueError("ode_residual should be a tensor or a tuple of tensors")

    def train(self, **kwargs):
        epochs = kwargs.get("epochs", 500)
        n_simu = kwargs.get("n_simu", 10)
        n_collocation_t = kwargs.get("n_collocation_t", 200)
        n_collocation_init = kwargs.get("n_collocation_init", 200)
        n_data_f = kwargs.get("n_data_f", 0)
        n_data_t = kwargs.get("n_data_t", 0)

        if n_data_f > 0 or n_data_t > 0:
            data_sample = self.ode.make_data(n_data_t)

        try:
            best_loss_value = self.losses.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        epoch = 0

        if n_collocation_t == 0:
            m = self.input_t.size()[0]
        if n_data_t == 0:
            m = n_collocation_t
        if n_data_t > 0 and n_collocation_t > 0:
            m = min(self.input_t.size()[0], n_collocation_t)

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

                    if n_simu > 0 and n_collocation_t > 0:
                        sample, f_loss = self.sampler.sampling(n_collocation_t, n_simu)
                        f_out = self.residual(sample, f_loss)
                        zeros = torch.zeros_like(f_out)
                        self.losses.update_residual_loss(
                            self.losses.residual_f_loss(f_out, zeros)
                        )

                    if self.losses.init_loss_bool:
                        sample, f_loss = self.sampler.sampling(
                            n_collocation_init, n_simu
                        )

                        t = 0 * sample.t_loss
                        mu = sample.params

                        w = self.network.setup_w_dict(t, mu, sample)
                        w_init = sample.w_initial

                        if not self.ode.second_derivative:
                            res = self.losses.init_f_loss(w["w"], w_init)
                        else:
                            self.network.get_first_derivatives(w, t)
                            init_loss_on_w = self.losses.init_f_loss(w["w"], w_init[0])
                            init_loss_on_w_t = self.losses.init_f_loss(
                                w["w_t"], w_init[1]
                            )
                            res = init_loss_on_w + init_loss_on_w_t
                        self.losses.update_init_loss(res)

                    if self.losses.data_loss_bool:
                        masked_sample = data_sample[indices]
                        prediction = self.network.get_w(masked_sample)
                        self.losses.update_data_loss(
                            self.losses.data_f_loss(prediction, masked_sample)
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

    # def plot(self, random=False):
    #     import matplotlib.pyplot as plt

    #     _, ax = plt.subplots(1, 3, figsize=(15, 5))
    #     ax[0].semilogy(self.loss_history, label="total loss")
    #     ax[0].semilogy(self.data_loss_history, label="data")
    #     ax[0].semilogy(self.residual_loss_history, label="residual")
    #     ax[0].set_title("loss history")
    #     ax[0].legend()

    #     n_visu = 500

    #     t = torch.linspace(
    #         self.ode.t_min, self.ode.t_max, n_visu, dtype=torch.double, device=device
    #     )[:, None]

    #     shape = (n_visu, self.ode.nb_parameters)
    #     ones = torch.ones(shape)
    #     if random:
    #         mu = self.mu_sampler.sampling(1)
    #         mu = mu * ones
    #     else:
    #         mu = torch.mean(self.ode.parameter_domain, axis=1) * ones

    #     parameter_string = ", ".join(
    #         [f"{mu[0, i].cpu().numpy():2.2f}" for i in range(self.ode.nb_parameters)]
    #     )

    #     v_pred = self.network.get_w(t, mu)
    #     v_ex = self.ode.reference_solution(t, mu)

    #     ax[1].plot(t.cpu(), v_ex.detach().cpu(), label="exact")
    #     ax[1].plot(t.cpu(), v_pred.detach().cpu(), label="prediction")

    #     ax[1].set_title(f"prediction, parameters = {parameter_string}")
    #     ax[1].legend()

    #     error = torch.abs(v_pred - v_ex).detach().cpu()

    #     ax[2].plot(t.cpu(), error)
    #     ax[2].set_title("prediction error")


# %%
