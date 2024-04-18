
from abc import ABC, abstractmethod

import torch


class ClassicODE(ABC):
    """
    Define the Van der Pol oscillator as a PyTorch module.
    """

    def __init__(self, flux, **kwargs):
        super().__init__()
        self.flux = flux
        self.nb_unknowns = flux.nb_unknowns
        self.nb_parameters = flux.nb_parameters
        self.order = 1

    def apply_flux(self, t, state, mu):
        return self.flux.forward(t, state, mu)

    @abstractmethod
    def random_init_data(self):
        pass

    @abstractmethod
    def random_params(self):
        pass

    @abstractmethod
    def plot_data(self, time):
        pass

    def generate_initial_conditions(self, nb_samples):
        if self.nb_unknowns == 1:
            return torch.tensor([[self.random_init_data()] for _ in range(nb_samples)])
        else:
            return torch.tensor([self.random_init_data() for _ in range(nb_samples)])

    def generate_parameters(self, nb_samples):
        if self.nb_parameters == 1:
            return torch.tensor([[self.random_params()] for _ in range(nb_samples)])
        else:
            return torch.tensor([self.random_params() for _ in range(nb_samples)])

    def get_parameters(self, mu):
        if self.ode.nb_parameters == 1:
            return mu[:, 0]
        else:
            return (mu[:, i] for i in range(self.nb_parameters))

    def get_solutions(self, time):
        if self.ode.nb_parameters == 1:
            return self.solutions[time, :, 0]
        else:
            return (self.solutions[time, :, i] for i in range(self.nb_parameters))

    def get_sample_solutions(self, time, sample):
        if self.ode.nb_parameters == 1:
            return self.solutions[time, sample, 0]
        else:
            return (self.solutions[time, sample, i] for i in range(self.nb_parameters))

    def time_scheme(self, initial_data, t, mu):
        if self.order == 1:
            self.euler(initial_data, t, mu)

    def euler(self, initial_data, t, mu):
        """
        :param model: the desired model (e.g. SIR, transport equation, ...)
        :param initial_data: solution at t=0
        :param t: time steps
        :return: solution for t=T
        """
        self.solution = torch.empty(len(t), *initial_data.shape)
        self.solution[0] = initial_data

        # le passage par y0 et y1 est nécessaire !!!!

        # Euler scheme: y(t+h) ~ y(t) + dt y'(t)
        #                      = y(t) + dt F(y(t))
        y0 = initial_data
        for n in range(1, len(t)):
            dt = t[n] - t[n - 1]
            y1 = y0 + dt * self.apply_flux(t[n - 1], y0, mu)
            self.solution[n] = y1
            y0 = y1

        return self.solution
