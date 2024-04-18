import torch
from torch import nn


class ConvexLayer(nn.Module):
    """
    Convex Layer: f(x,z) with x the inputs of the global
    function and z a latent variable. Use convex-increasing activation function,
    linear layer for x and positive linear layer for z
    """

    def __init__(self, dim, in_size, out_size, beta=1):
        super().__init__()
        self.dim = dim  # dimension of the input associatied to the full network
        self.in_size = in_size
        self.out_size = out_size
        self.positive_layer = nn.Linear(in_size, out_size)
        self.layer = nn.Linear(dim, out_size)

        self.activation = torch.nn.Softplus(beta)

    def forward(self, x: torch.Tensor, z: torch.Tensor) -> torch.Tensor:
        return self.activation(self.positive_layer(z) + self.layer(x))


class IConvexNet(nn.Module):
    def __init__(self, dim, out_size, beta=1, layers_size=[2, 4, 4, 2]):
        super().__init__()
        self.dim = dim  # dimension of the input associatied to the full network
        self.out_size = out_size
        self.layers_size = layers_size
        self.layers = []

        self.first_layer = nn.Linear(dim, layers_size[0])
        for i in range(0, len(self.layers_size) - 1):
            self.layers.append(
                ConvexLayer(self.dim, self.layers_size[i], self.layers_size[i + 1])
            )

        self.layers.append(ConvexLayer(self.dim, self.layers_size[-1], self.out_size))

    def forward(self, x):
        z = self.first_layer(x)
        for i in range(0, len(self.layers)):
            z = self.layers[i](x, z)
        return z
