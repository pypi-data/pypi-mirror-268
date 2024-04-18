import torch
from torch import nn

# strongly inspired of https://github.com/karpathy/pytorch-normalizing-flows/blob/master/nflib/flows.py


def AffineConstantFlow(net, **kwargs):
    class AffineConstantFlow(nn.Module):
        """
        Class for affine constant flow where the type of neural network is given by net.
            It is to approximate probability :math:`p(y\mid x)`

        flow  :math:`z= y \exp^{s(x)}+t(x)`

            with s the scale and t the shift/translation term

        :param dim: the dimension of the input x of the flow
        :type dim: int, optional
        :param dim_conditional: the dimension of the conditional input y of the flow
        :type dim_conditional: int,optional
        :param shift: to indicate if we use a shift term or not
        :type shift: bool,optional
        :param scale: to indicate if we use a scale term or not
        :type scale: bool,optional
        """

        def __init__(
            self,
            dim: int = 1,
            dim_conditional: int = 1,
            scale: bool = True,
            shift: bool = True,
            **kwargs,
        ):
            super().__init__()
            self.dim = dim
            self.dim_conditional = dim_conditional
            if dim_conditional == 0:
                self.s = (
                    nn.Parameter(torch.randn(1, dim, requires_grad=True))
                    if scale
                    else None
                )
                self.t = (
                    nn.Parameter(torch.randn(1, dim, requires_grad=True))
                    if shift
                    else None
                )
            else:
                self.s = (
                    net(in_size=self.dim_conditional, out_size=self.dim, **kwargs)
                    if scale
                    else None
                )
                self.t = (
                    net(in_size=self.dim_conditional, out_size=self.dim, **kwargs)
                    if shift
                    else None
                )

        def forward(self, y, x):
            """
                Compute the flow  :math:`z= y \exp^{s(x)}+t(x)`

                :param x: the tensor of the conditional data x
                :type x: int, optional
                :param y: the tensor of the data y
                :type y: int,optional
                :return: the tensor containing the result
                :rtype: torch.Tensor
            """
            if self.dim_conditional == 0:
                s = self.s if self.s is not None else y.new_zeros(y.size())
                t = self.t if self.t is not None else y.new_zeros(y.size())
            else:
                s = self.s(x) if self.s is not None else y.new_zeros(y.size())
                t = self.t(x) if self.t is not None else y.new_zeros(y.size())
            z = y * torch.exp(s) + t
            log_det = torch.sum(s, dim=1)
            return z, log_det

        def backward(self, z, x):
            """
                Compute the inverse flow  :math:`y= (z- t(x)) \exp^{-s(x)}`

                :param x: the tensor of the conditional data x
                :type x: int, optional
                :param z: the tensor of the data z
                :type z: int,optional
                :return: the tensor containing the result
                :rtype: torch.Tensor
            """
            if self.dim_conditional == 0:
                s = self.s if self.s is not None else z.new_zeros(z.size())
                t = self.t if self.t is not None else z.new_zeros(z.size())
            else:
                s = self.s(x) if self.s is not None else z.new_zeros(z.size())
                t = self.t(x) if self.t is not None else z.new_zeros(z.size())
            y = (z - t) * torch.exp(-s)
            log_det = torch.sum(-s, dim=1)
            return y, log_det

    return AffineConstantFlow(**kwargs)


def RealNVPFlow(net, **kwargs):
    class RealNVPFlow(nn.Module):
        """
        Class for conservative volumes flow where the type of neural network is given by net.
            It is to approximate probability :math:`p(y\mid x)`

        flow  :math:`z[k:d]= y[k:d] \exp^{s(y[1:k],x)}+t(y[1:k],x)` et :math:`z[1:k]= y[1:k]`

            with s the scale and t the shift/translation term

        :param dim: the dimension of the input x of the flow
        :type dim: int
        :param dim_conditional: the dimension of the conditional input y of the flow
        :type dim_conditional: int
        :param partiry: ...
        :type parity: bool
        :param shift: to indicate if we use a shift term or not
        :type shift: bool,optional
        :param scale: to indicate if we use a scale term or not
        :type scale: bool,optional
        """

        def __init__(
            self, dim, dim_conditional, parity, scale=True, shift=True, **kwargs
        ):
            super().__init__()
            self.dim = dim
            self.dim_c = dim_conditional
            self.parity = parity
            self.s_cond = lambda x: x.new_zeros(x.size(0), self.dim // 2 + self.dim_c)
            self.t_cond = lambda x: x.new_zeros(x.size(0), self.dim // 2 + self.dim_c)
            if scale:
                self.s_cond = net(
                    in_size=self.dim // 2 + self.dim_c, out_size=self.dim // 2, **kwargs
                )
            if shift:
                self.t_cond = net(
                    in_size=self.dim // 2 + self.dim_c, out_size=self.dim // 2, **kwargs
                )

        def forward(self, y, x):
            """
                Compute the flow  :math:`z[k:d]= y[k:d] \exp^{s(y[1:k],x)}+t(y[1:k],x)` et :math:`z[1:k]= y[1:k]`

                :param x: the tensor of the conditional data x
                :type x: int, optional
                :param y: the tensor of the data y
                :type y: int,optional
                :return: the tensor containing the result
                :rtype: torch.Tensor
            """
            y0, y1 = y[:, ::2], y[:, 1::2]
            if self.parity:
                y0, y1 = y1, y0
            s = self.s_cond(torch.cat([y0, x], axis=1))
            t = self.t_cond(torch.cat([y0, x], axis=1))
            z0 = y0  # untouched half
            # transform this half as a function of the other
            z1 = torch.exp(s) * y1 + t
            if self.parity:
                z0, z1 = z1, z0
            z = torch.cat([z0, z1], dim=1)
            log_det = torch.sum(s, dim=1)
            return z, log_det


        def backward(self, z, x):
            """
                Compute the flow  :math:`y[k:d]= (z[k:d]-t(z[1:k],x)) \exp^{-s(y[1:k],x)}` et :math:`y[1:k]= z[1:k]`

                :param x: the tensor of the conditional data x
                :type x: int, optional
                :param z: the tensor of the data y
                :type z: int,optional
                :return: the tensor containing the result
                :rtype: torch.Tensor
            """

            z0, z1 = z[:, ::2], z[:, 1::2]
            if self.parity:
                z0, z1 = z1, z0
            s = self.s_cond(torch.cat([z0, x], axis=1))
            t = self.t_cond(torch.cat([z0, x], axis=1))
            y0 = z0  # this was the same
            y1 = (z1 - t) * torch.exp(-s)  # reverse the transform on this half
            if self.parity:
                y0, y1 = y1, y0
            y = torch.cat([y0, y1], dim=1)
            log_det = torch.sum(-s, dim=1)
            return y, log_det

    return RealNVPFlow(**kwargs)
