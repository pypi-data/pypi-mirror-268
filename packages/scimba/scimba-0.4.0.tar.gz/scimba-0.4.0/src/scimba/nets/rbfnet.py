import torch
from torch import nn

from . import activation as ac


class RBFScalarLayer(nn.Module):
    """
    class creating a layer to approximate scalar functions using a linear combination of radial basis functions

    :param in_size: dimension of inputs
    :type in_size: int

    :Keyword Arguments:
    * *nb_func* (``int``) --
      the number of radial function is the layer
    * *type_g* (``string``) --
      a string which indicate if the radial function is isotropic or anisotropic
    * *type_rbf* (``string``) --
      the name of rbf function
    * *norm* (``int``) --
      the type of Lp norm used
    * *min_x* (``float``) --
      the minimal value for the random initialization for each direction of mu associated to RBF
    * *max_x* (``float``) --
      the maximal value for the random initialization for each direction of mu associated to RBF

    :Learnable Parameters:
    * *layer* (``LinearLayer``)
        the linear layer applied to the vector of features
    """

    def __init__(self, in_size: int = 1, **kwargs):
        super().__init__()

        self.in_size = in_size
        self.nb_func = kwargs.get("nb_func", 1)  # number of fourier features
        self.type_g = kwargs.get("type_g", "isotropic")
        self.type_rbf = kwargs.get("type_rbf", "gaussian")
        self.norm = kwargs.get("norm", 2)
        self.min_x = kwargs.get("min_x", 0.0)
        self.max_x = kwargs.get("max_x", 1.0)

        self.gaussian = torch.empty((self.nb_func))
        self.layer = nn.Linear(self.nb_func, 1)

        if self.type_g == "isotropic":
            self.activation = nn.ParameterList(
                [
                    ac.IsotropicRadial(in_size=self.in_size, **kwargs)
                    for i in range(self.nb_func)
                ]
            )
        else:
            self.activation = nn.ParameterList(
                [
                    ac.AnisotropicRadial(in_size=self.in_size, **kwargs)
                    for i in range(self.nb_func)
                ]
            )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        gaussian_list = self.activation[0](inputs)
        for i in range(1, self.nb_func):
            gaussian_list = torch.cat(
                (gaussian_list, self.activation[i](inputs)), dim=1
            )
        res = self.layer(gaussian_list)
        return res

    def print_parameters(self):
        for i in range(0, self.nb_func):
            print(self.activation[i])


class RBFLayer(nn.Module):
    """
    class which create a layer with can approximate vectorial function using some RBF scalar layer

    :param in_size: dimension of inputs
    :type in_size: int
    :param out_size: dimension of outputs
    :type out_size: int

    :Keyword Arguments:
    * *nb_func* (``int``) --
      the number of radial function is the layer
    * *type_g* (``string``) --
      a string which indicate if the radial function is isotropic or anisotropic
    * *type_rbf* (``string``) --
      the name of rbf function
    * *norm* (``int``) --
      the type of Lp norm used
    * *min_x* (``float``) --
      the minimal value for the random initialization for each direction of mu associated to RBF
    * *max_x* (``float``) --
      the maximal value for the random initialization for each direction of mu associated to RBF

    :Learnable Parameters:
    * *layer* (``RBFScalarLayer``)
        a tensor of the scalar linear layers
    """

    def __init__(self, in_size: int, out_size: int, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        # number of fourier features
        self.nb_gaussian = kwargs.get("nb_gaussian", 1)
        self.type_g = kwargs.get("type_g", "isotropic")
        self.type_rbf = kwargs.get("type_rbf", "gaussian")
        self.norm = kwargs.get("norm", 2)
        self.min_x = kwargs.get("min_x", 0.0)
        self.max_x = kwargs.get("max_x", 1.0)

        self.layer = nn.ParameterList(
            [
                RBFScalarLayer(in_size=self.in_size, **kwargs)
                for i in range(self.out_size)
            ]
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        """
        Apply the network to the inputs

        :param inputs: input tensor
        :type inputs: torch.Tensor
        :return: the result of the network
        :rtype: torch.Tensor
        """
        outputs = self.layer[0](inputs)
        for i in range(1, self.out_size):
            outputs = torch.cat((outputs, self.layers[i](inputs)), dim=1)
        return outputs
