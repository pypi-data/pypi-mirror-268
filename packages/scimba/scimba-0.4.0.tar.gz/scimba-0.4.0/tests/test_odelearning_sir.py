import pylab as plt
import scimba.odelearning.abstract_ode as abstractode
import scimba.odelearning.generation_ode_data as generation_ode_data
import scimba.odelearning.generic_flux as genericflux
import scimba.odelearning.loss_odelearning as loss
import scimba.odelearning.training_diffphy_ode as training
import torch


class SIRflux(genericflux.Flux):
    def __init__(self, beta):
        super().__init__()

        self.beta = torch.nn.Parameter(torch.tensor(beta), requires_grad=True)
        self.nb_unknowns = 3
        self.nb_parameters = 1

    def forward(self, t, state, mu):
        gamma = self.get_parameters(mu)
        S, I, R = self.get_variables(state)

        dS = -self.beta * S * I
        dI = self.beta * S * I - gamma * I
        dR = gamma * I

        return self.set_derivatives(state, dS, dI, dR)


class SIR_ode(abstractode.ClassicODE):
    def random_init_data(self):
        S = 0.9 + 0.1 * torch.rand(1)
        I = 1.0 - S
        R = 0.0
        return S, I, R

    def random_params(self):
        gamma = 0.3 + 0.01 * torch.rand(1)
        return gamma

    def plot_data(self, time, data):
        time = time.detach().cpu()
        data = data.detach().cpu()
        fig, axs = plt.subplots(2, 2, figsize=(14, 10))
        axs[0, 0].plot(time, data[..., 0])
        axs[0, 0].set_title("S dynamic")
        axs[0, 1].plot(time, data[..., 1])
        axs[0, 1].set_title("I dynamic")
        axs[1, 0].plot(time, data[..., 2])
        axs[1, 0].set_title("R dynamic")
        plt.show()


class MSELoss_RefOde(loss.LossODELearning_withdata):
    def __init__(self, ode):
        super().__init__(ode)
        self.loss_used = torch.nn.MSELoss()

    def apply(self, x, xref, t, mu):
        """
        x: shape(nb_time, nb_samples, nb_unknowns)
        """
        return self.loss_used(input=x, target=xref)


def test_odelearning_sir():
    flux_ref = SIRflux(0.7)
    flux = SIRflux(0.4)

    oderef = SIR_ode(flux_ref)
    ode = SIR_ode(flux)

    data_ode = generation_ode_data.DataGenerate(
        oderef, T=2, num_time_batch=2, num_timestep_per_batch=2
    )
    data_ode.create_dataset(2)

    loss_for_training = MSELoss_RefOde(ode)

    print("valeur initiale de beta: ", ode.flux.beta)
    trainer = training.Trainer_DF_ODE_with_data(
        model=ode, data=data_ode, loss_f=loss_for_training, nb_batch=2
    )
    trainer.train(epochs=1)

    print("valeur de beta: ", ode.flux.beta)


test_odelearning_sir()
