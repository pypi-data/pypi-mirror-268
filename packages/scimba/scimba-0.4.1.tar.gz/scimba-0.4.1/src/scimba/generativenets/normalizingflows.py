import torch
from torch import nn

# strongly inspired of https://github.com/karpathy/pytorch-normalizing-flows/blob/master/nflib/flows.py

### https://github.com/HosseinEbrahimiK/ScNormFlows a fqaireeeee
class NormalizingFlow(nn.Module):
    """
    Class to define a normalizing flows to approximate the probability :math:`p(y\mid x)`


    :param prior: the input distribution of the normalizing flow
    :type prior: torch.distributions
    :param flows: list of the flows using in each layer
    :type flows: list
    """

    def __init__(self, prior: torch.distributions, flows: list):
        super().__init__()
        self.prior = prior
        self.flows = nn.ModuleList(flows)

    def forward_flows(self, y: torch.Tensor, x: torch.Tensor) -> list[torch.Tensor]:
        """
        Compute the different simple flows associated to the network

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param y: the tensor of the final distribution data y
        :type y: torch.Tensor
        :return: the list contains the samples of the approximated distribution and log of the determinant
        :rtype: list
        """
        m, _ = y.shape
        log_det = torch.zeros(m)
        zs = [y]
        for flow in self.flows:
            y, ld = flow.forward(y, x)
            log_det += ld
            zs.append(y)
        return zs, log_det

    def forward(self, y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
        """
        Compute the loss associated to the flow given by the log of the probability prior and the sum of the log
        to the determinant

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param y: the tensor of the final distribution data y
        :type y: torch.Tensor
        :return: the loss associated to sample z which approximate the target distribution
        :rtype: torch.Tensor
        """
        zs, log_det = self.forward_flows(y, x)
        prior_logprob = self.prior.log_prob(zs[-1]).view(y.size(0), -1).sum(1)
        logprob = prior_logprob + log_det
        return -torch.sum(logprob)

    def backward_flows(self, z: torch.Tensor, x: torch.Tensor) -> list[torch.Tensor]:
        """
        Compute the inverse of the different simple flows associated to the network

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param z: the tensor of the initial distribution data z
        :type z: torch.Tensor
        :return: the list contains the samples of the original distribution and log of the determinant
        :rtype: list
        """
        m, _ = z.shape
        log_det = torch.zeros(m)
        ys = [z]
        for flow in self.flows[::-1]:
            z, ld = flow.backward(z, x)
            log_det += ld
            ys.append(z)
        return ys, log_det

    def backward(self, z: torch.Tensor, x: torch.Tensor) -> list[torch.Tensor]:
        """
        Compute the inverse of the different simple flows associated to the network and the log associated

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param z: the tensor of the initial distribution data z
        :type z: torch.Tensor
        :return: the list contains the samples of the original distribution and log of the determinant
        :rtype: list
        """
        y_s, log_det = self.backward_flows(z, x)
        return y_s, log_det

    def sample_prior(self, num_samples: int) -> torch.Tensor:
        """
        Sample the prior distribution

        :param num_samples: the number of samples
        :type num_samples: int
        :return: the tensor of the sample of the initial prior
        :rtype: torch.Tensor
        """
        z = self.prior.sample((num_samples,))
        return z

    def sample(self, x: torch.Tensor, num_samples: int) -> torch.Tensor:
        """
        Sample the final distribution

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param num_samples: the number of samples
        :type num_samples: int
        :return: the tensor of the sample of final distribution
        :rtype: torch.Tensor
        """
        z = self.prior.sample((num_samples,))
        y_s, _ = self.backward_flows(z, x)
        return y_s

    def density(self, y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
        """
        Compute the density associated to the sample y of the final distribution

        :param x: the tensor of the conditional data x
        :type x: torch.Tensor
        :param y: the tensor of the final distribution data y
        :type y: torch.Tensor
        :return: the tensor of the density associated to y
        :rtype: torch.Tensor
        """
        zs, log_det = self.forward_flows(y, x)
        prior_logprob = self.prior.log_prob(zs[-1]).view(y[:, None].size(0), -1).sum(1)
        logprob0 = prior_logprob + log_det
        return torch.exp(logprob0)
