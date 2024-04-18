import torch
import torch.distributions as D
from torch import nn


class GaussianMixtures(nn.Module):
    """
    Class to define a Gaussian Mixture to approximate :math:`p(y)`


    :param dim: the dimension of the Gaussian Mixture
    :type dim: int
    :param nb_gaussians: the number of Gaussian Mixture
    :type nb_gaussian: int

    :Learnable Parameters:
    * *weights* (``list[float]``)
        the list of the coefficient in the mixture (size= nb_gaussian)
    * *means* (``list[torch.Tensor]``)
         the list of the means in the mixture (size= nb_gaussian * dim)
    * *stdevs* (``list[torch.Tensor]``)
         the list of the std matrix in the mixture (size= nb_gaussian * dim* dim)
    """

    def __init__(self, dim: int = 1, nb_gaussians: int = 2):
        super().__init__()
        self.dim = dim
        self.nb_gaussians = nb_gaussians
        weights = torch.ones(
            nb_gaussians,
        )
        means = torch.randn(nb_gaussians, dim)
        stdevs = torch.rand((nb_gaussians, dim, dim))
        self.weights = torch.nn.Parameter(weights)
        self.means = torch.nn.Parameter(means)
        self.stdevs = torch.nn.Parameter(stdevs)
        self.weights_ouput_layer = nn.Softmax(dim=0)

    def forward(self, y: torch.Tensor, x: torch.Tensor) -> float:
        """
            The forward compute the gaussian mixture distribution 
            and gives the log of the probability p(y)

            :param y: sample of the current distribution
            :type y: torch.Tensor
            :param x: conditional variable (not used here)
            :type x: torch.Tensor
            :return: sample of the current distribution
            :rtype: torch.Tensor
        """
        sig2 = torch.bmm(torch.transpose(self.stdevs, 1, 2), self.stdevs)
        mix = D.Categorical(self.weights_ouput_layer(self.weights))
        comp = D.MultivariateNormal(self.means, sig2)
        gmm = D.MixtureSameFamily(mix, comp)
        return -gmm.log_prob(y).mean()

    def sample(self, num_samples: int = 1) -> torch.Tensor:
        """
            Gives some sample of the mixture gaussian distribution 

            :param num_samples: the number of sample that we want
            :type num_samples: int
            :return: sample of the current distribution
            :rtype: torch.Tensor
        """
        sig2 = torch.bmm(torch.transpose(self.stdevs, 1, 2), self.stdevs)

        mix = D.Categorical(self.weights_ouput_layer(self.weights))
        comp = D.MultivariateNormal(self.means, sig2)
        gmm = D.MixtureSameFamily(mix, comp)
        return gmm.sample((num_samples,))


def ConditionalGaussianMixtures(net, **kwargs):
    """
    Class to define a Gaussian Mixture to approximate the conditional law :math:`p(y\mid x)`
        Here the coefficients (weights, means, stdevs) are networks dependant of x

    :param dim: the dimension of the Gaussian Mixture
    :type dim: int, optional
    :param dim_condtional: the dimension of conditional variable of the Gaussian Mixture
    :type dim_conditional: int, optional
    :param nb_gaussians: the number of Gaussian Mixture
    :type nb_gaussian: int, optional
    """

    class ConditionalGaussianMixtures(nn.Module):
        def __init__(
            self, dim: int = 1, dim_conditional: int = 0, nb_gaussians: int = 2
        ):
            super().__init__()
            self.dim = dim
            self.nb_gaussians = nb_gaussians
            self.dim_conditional = dim_conditional
            self.weights = net(
                in_size=self.dim_conditional, out_size=self.nb_gaussians, **kwargs
            )
            self.means = net(
                in_size=self.dim_conditional,
                out_size=self.dim * self.nb_gaussians,
                **kwargs,
            )
            self.stdevs = net(
                in_size=self.dim_conditional,
                out_size=self.dim * self.dim * self.nb_gaussians,
                **kwargs,
            )
            self.weights_output_layer = nn.Softmax(dim=0)

        def compute_distribution(self, x: torch.Tensor) -> torch.distributions:
            """
                Compute the conditional distribution`

                :param x: the tensor of the conditional data x
                :type x: int, optional
                :return: the distribution
                :rtype: torch.distribution
            """
            weights = self.weights(x)
            means = torch.reshape(self.means(x), (-1, self.nb_gaussians, self.dim))
            sig = torch.reshape(
                self.stdevs(x), (-1, self.nb_gaussians, self.dim, self.dim)
            )
            sig2 = torch.einsum("abij,abjk->abik", torch.transpose(sig, 2, 3), sig)
            mix = D.Categorical(self.weights_output_layer(weights))
            comp = D.MultivariateNormal(means, sig2)
            gmm = D.MixtureSameFamily(mix, comp)
            return gmm

        def forward(self, y: torch.Tensor, x: torch.Tensor) -> float:
            """
                The forward compute the gaussian mixture distribution 
                and gives the log of the probability p(y\mid x)

                :param y: sample of the current distribution
                :type y: torch.Tensor
                :param x: conditional variable 
                :type x: torch.Tensor
                :return: :math:` -log p(y\mid x)`
                :rtype: torch.Tensor
            """
            gmm = self.compute_distribution(x)
            return -gmm.log_prob(y).mean()

        def sample(self, x: torch.Tensor, num_samples: int = 1) -> torch.Tensor:
            """
                Gives some sample of the conditional mixture gaussian distribution 

                :param x: conditional variable (not used here)
                :type x: torch.Tensor
                :param num_samples: the number of sample that we want
                :type num_samples: int
                :return: sample of the current distribution
                :rtype: torch.Tensor
            """
            gmm = self.compute_distribution(x)
            return gmm.sample((num_samples,))

        def density(self, y: torch.Tensor, x: torch.Tensor) -> float:
            """
                Gives the density value at the point y/mid x

                :param y: sample of the current distribution
                :type y: torch.Tensor
                :param x: conditional variable 
                :type x: torch.Tensor
                :return: :math:` -log p(y\mid x)`
                :rtype: torch.Tensor
            """
            gmm = self.compute_distribution(x)
            return torch.exp(gmm.log_prob(y))

    return ConditionalGaussianMixtures(**kwargs)
