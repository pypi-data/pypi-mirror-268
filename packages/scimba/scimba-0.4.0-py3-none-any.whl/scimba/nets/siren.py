import numpy as np
import torch
from torch import nn

from .activation import Sine


class SirenLayer(nn.Module):
    """
    class a Siren Layer

    :param in_size: dimension of the inputs
    :type in_size: int
    :param out_size: dimension of the outputs
    :type out_size: int

    :Learnable Parameters:
    * *layer* (``LinearLayer``)
        the linear layer applied to the vector of features
    """

    def __init__(
        self,
        in_size: int,
        out_size: int,
        w0: int = 1,
        c: int = 6,
        is_first: bool = False,
        use_bias: bool = True,
    ):
        super().__init__()
        self.in_size = in_size
        self.is_first = is_first
        self.out_size = out_size

        self.layer = nn.Linear(in_size, out_size, bias=use_bias)
        self.init_(self.layer.weight, self.layer.bias, c=c, w0=w0)

        self.activation = Sine(freq=w0)

    def init_(self, weight: torch.Tensor, bias: torch.Tensor, c: int, w0: int):
        """
        init the weights of the layer using the specific Siren initialization.

        :param weight: the weight of the layer to initialize
        :type weight: torch.Tensor
        :param weight: the bias of the layer to initialize
        :type weight: torch.Tensor
        :param c: a parameter for the weight initialization
        :type c: int
        :param w0: the frequency of the sinus activation function
        :type w0: int
        """
        dim = self.in_size

        w_std = (1 / dim) if self.is_first else (np.sqrt(c / dim) / w0)
        torch.nn.init.uniform_(weight, -w_std, w_std)

        if bias is not None:
            torch.nn.init.uniform_(bias, -w_std, w_std)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs .

        :param x: input tensor
        :type x: torch.Tensor
        :return: the result of the  layer
        :rtype: torch.Tensor
        """
        return self.activation(self.layer(x))


class SirenNet(nn.Module):
    """
    class representing a Siren architecture

    :param in_size: dimension of inputs
    :type in_size: int
    :param out_size: dimension of outputs
    :type out_size: int

    :Keyword Arguments:
    * *w* (``int``) --
      the frequency of the internal layers activation function
    * *w0* (``int``) --
      the frequency of the first layer activation function
    * *layer_sizes* (``list[int]``) --
      the list of neural networks for each layer

    :Learnable Parameters:
    * *layers* (``list[SirenLayer]``)
        the list of hidden of Siren layer and one linear layer at the end
    """

    def __init__(self, in_size: int, out_size: int, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        self.layer_sizes = kwargs.get("layer_sizes", [20, 20, 20])
        self.w = kwargs.get("w", 1)
        self.w0 = kwargs.get("w0", 30)

        self.layers = nn.ModuleList([])
        self.layers.append(
            SirenLayer(
                in_size=self.in_size,
                out_size=self.layer_sizes[0],
                w0=self.w0,
                use_bias=True,
                is_first=True,
            )
        )
        for i in range(1, len(self.layer_sizes) - 1):
            self.layers.append(
                SirenLayer(
                    in_size=self.layer_sizes[i],
                    out_size=self.layer_sizes[i + 1],
                    w0=self.w,
                    use_bias=True,
                    is_first=False,
                )
            )
        self.layers.append(nn.Linear(self.layer_sizes[-1], self.out_size))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs x.

        :param x: input tensor
        :type x: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        for layer in self.layers:
            x = layer(x)
        return x
