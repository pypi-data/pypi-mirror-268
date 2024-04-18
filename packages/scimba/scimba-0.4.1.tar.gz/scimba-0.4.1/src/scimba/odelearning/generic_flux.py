from abc import ABC, abstractmethod

import torch
from torch import nn


class Flux(nn.Module, ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, t, state, mu):
        pass

    def get_variables(self, state):
        nb_unknowns = self.nb_unknowns
        if nb_unknowns == 1:
            return state[..., 0]
        else:
            return (*(state[..., i] for i in range(nb_unknowns)),)

    def get_parameters(self, mu):
        nb_parameters = self.nb_parameters
        if nb_parameters == 1:
            return mu[..., 0]
        else:
            return (*(mu[..., i] for i in range(nb_parameters)),)

    def get_t(self, t):
        if t.shape == torch.Size([]):
            return torch.tensor([t])
        else:
            return t

    def set_derivatives(self, state, *args):
        # res = torch.zeros((*args[0].shape, len(args)))
        res = torch.zeros_like(state)
        for i, arg in enumerate(args):
            try:
                res[..., i] = arg[:, 0]
            except IndexError:
                res[..., i] = arg
        return res

    def prepare_network_inputs(self, *args):
        if args[0].shape == torch.Size([]):
            inputs = torch.zeros(len(args))
            for i, arg in enumerate(args):
                inputs[i] = arg
        else:
            inputs = torch.zeros((*args[0].shape, len(args)))
            for i, arg in enumerate(args):
                inputs[..., i] = arg

        return inputs
