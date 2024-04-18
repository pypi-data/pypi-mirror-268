import torch
from torch import nn

from .activation import ActivationFunction, Heaviside


class GenericMLP(nn.Module):
    """
    class representing a general Multi-Layer Perceptron architecture

    :param in_size: dimension of inputs
    :type in_size: int
    :param out_size: dimension of outputs
    :type out_size: int

    :Keyword Arguments:
    * *activation_type* (``string``) --
      the type of activation function
    * *activation_output* (``string``) --
      the type of activation function for the output
    * *layer_sizes* (``list[int]``) --
      the list of neural networks for each layer

    :Learnable Parameters:
    * *hidden_layers* (``list[LinearLayer]``)
        the list of hidden of linear layer
    * *output_layer* (``LinearLayer``)
        the last linear layer
    """

    def __init__(self, in_size: int, out_size: int, **kwargs):
        super().__init__()

        activation_type = kwargs.get("activation_type", "tanh")
        activation_output = kwargs.get("activation_output", "id")
        layer_sizes = kwargs.get("layer_sizes", [10, 20, 20, 20, 5])

        self.in_size = in_size
        self.out_size = out_size

        self.layer_sizes = [in_size] + layer_sizes + [out_size]
        self.hidden_layers = []

        for l1, l2 in zip(self.layer_sizes[:-2], self.layer_sizes[+1:-1]):
            self.hidden_layers.append(nn.Linear(l1, l2))
        self.hidden_layers = nn.ModuleList(self.hidden_layers)

        self.output_layer = nn.Linear(self.layer_sizes[-2], self.layer_sizes[-1])
        self.activation = []

        for _ in range(len(self.layer_sizes) - 1):
            self.activation.append(
                ActivationFunction(activation_type, in_size=in_size, **kwargs)
            )

        self.activation_output = ActivationFunction(
            activation_output, in_size=in_size, **kwargs
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs .

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        for hidden_layer, activation in zip(
            self.hidden_layers[0:], self.activation[0:]
        ):
            inputs = activation(hidden_layer(inputs))

        return self.activation_output(self.output_layer(inputs))

    def __str__(self):
        return "MLP network"


class DiscontinuousLayer(nn.Module):
    """
    class which encode a fully connected layer which can be discontinuous or not

        :math:`y=sigma(Ax+b) + \epsilon * H(Ax+b)`

    with :math:`H(x)` a Heaviside function and :math:`\epsilon` a vector

    :param in_size: dimension of inputs
    :type in_size: int
    :param out_size: dimension of outputs
    :type out_size: int

    :Keyword Arguments:
    * *activation_type* (``string``) --
      the type of activation function

    :Learnable Parameters:
    * *linearlayer* (``LinearLayer``)
        the  linear layer
    * *eps* (``torch.nn.Parameter``)
        the parameters which multiply the Heaviside. The size is the size of the output of the layer
    """

    def __init__(self, in_size: int, out_size: int, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size

        self.layer_type = kwargs.get("dis", True)
        self.activation_type = kwargs.get("activation_type", "tanh")

        self.linearlayer = nn.Linear(in_size, out_size)
        self.eps = nn.Parameter(torch.rand((out_size)))
        self.activation = ActivationFunction(
            self.activation_type, in_size=in_size, **kwargs
        )

        self.heaviside = Heaviside(k=100)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs .

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        if self.layer_type:
            x1 = self.activation(self.linearlayer(inputs))
            x2 = self.activation(self.linearlayer(inputs))
            res = x1 + self.eps[None, :] * x2
        else:
            res = self.activation(self.linearlayer(inputs))

        return res


class DiscontinuousMLP(nn.Module):
    """
    class MLP which Encode a general discontinuous MLP architecture

    :param in_size: dimension of inputs
    :type in_size: int
    :param out_size: dimension of outputs
    :type out_size: int

    :Keyword Arguments:
    * *activation_type* (``string``) --
      the type of activation function
    * *activation_output* (``string``) --
      the type of activation function for the output
    * *layer_sizes* (``list[int]``) --
      the list of neural networks for each layer

    :Learnable Parameters:
    * *hidden_layers* (``list[DiscontinuousLayer]``)
        the list of hidden of discontinuous layer
    * *output_layer* (``LinearLayer``)
        the last linear layer
    """

    def __init__(self, in_size: int, out_size: int, **kwargs):
        super().__init__()

        self.activation_type = kwargs.get("activation_type", "tanh")
        self.activation_output_type = kwargs.get("activation_output", "id")
        layer_sizes = kwargs.get("layer_sizes", [10, 20, 20, 20, 5])
        layer_type = kwargs.get("layer_type", [False, False, True, False, False])

        self.in_size = in_size
        self.out_size = out_size

        self.layer_sizes = [in_size] + layer_sizes + [out_size]
        self.layer_type = layer_type + ["C"]
        self.hidden_layers = []

        for l1, l2, ltype in zip(
            self.layer_sizes[:-2], self.layer_sizes[+1:-1], self.layer_type
        ):
            self.hidden_layers.append(
                DiscontinuousLayer(
                    l1, l2, dis=ltype, activation_type=self.activation_type
                )
            )
        self.hidden_layers = nn.ModuleList(self.hidden_layers)

        self.output_layer = nn.Linear(self.layer_sizes[-2], self.layer_sizes[-1])

        self.activation_output = ActivationFunction(
            self.activation_output_type, in_size=in_size, **kwargs
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        for hidden_layer in self.hidden_layers:
            inputs = hidden_layer(inputs)

        return self.activation_output(self.output_layer(inputs))

    def __str__(self):
        return "Discontinuous MLP network"


class EnhancedFeatureNet(nn.Module):
    """
    class which create a one layer network which generate some learnable features like Fourier features.
    the weights are generated a normal law

    :param in_size: dimension of inputs
    :type in_size: int

    :Keyword Arguments:
    * *nb_features* (``int``) --
      the number of features created by the network
    * *type_feature* (``string``) --
      the name of the feature that you want (Fourier, Wavelet etc)
    * *std* (``float``) --
      the std used to generate the weights of the layer.

    :Learnable Parameters:
    * *layer* (``LinearLayer``)
        the linear layer applied to the vector of features
    """

    def __init__(self, in_size: int, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.nb_features = kwargs.get("nb_features", 1)
        self.type_feature = kwargs.get("type_feature", "fourier")
        self.std = kwargs.get("std", 1.0)

        print("mmmmmm", self.std)
        self.layer = nn.Linear(in_size, self.nb_features, bias=False)
        nn.init.normal_(self.layer.weight, 0.0, self.std)

        if self.type_feature == "fourier":
            self.ac = ActivationFunction("sine", **kwargs)
            self.ac2 = ActivationFunction("cosin", **kwargs)
            self.enhanced_dim = 2 * self.nb_features
        if self.type_feature == "rbf_isotrope":
            self.ac = ActivationFunction("isotropic_radial", in_size=in_size, **kwargs)
            self.enhanced_dim = self.nb_features
        if self.type_feature == "rbf_anisotrope":
            self.ac = ActivationFunction(
                "anisotropic_radial", in_size=in_size, **kwargs
            )
            self.enhanced_dim = self.nb_features

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        if self.type_feature == "fourier":
            out1 = self.ac(self.layer.forward(x))
            out2 = self.ac2(self.layer.forward(x))
            out = torch.cat([out1, out2], axis=1)
        else:
            out = self.ac(self.layer.forward(x))

        return out
