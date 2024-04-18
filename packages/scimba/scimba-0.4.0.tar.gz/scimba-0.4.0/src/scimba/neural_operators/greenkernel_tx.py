from torch import nn
from torch.autograd import grad as grad


class MLPKernel_tx:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class FourierKernel_tx:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class LocalMLPKernel_tx:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class LocalFourierKernel_tx:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


def LowRank_MLPKernel_tx(net: nn.Module, **kwargs):
    class LowRank_MLPKernel_tx(net):
        def __int__(self, in_size, out_size, **kwargs):
            super(net, self).__init__(nn.Module())

    ## TOO DOO finish init
    ## TOO DOO implement forward

    LowRank_MLPKernel_tx(**kwargs)


def LowRank_FourierKernel_tx(net: nn.Module, **kwargs):
    class LowRank_FourierKernel_tx(net):
        def __int__(self, in_size, out_size, **kwargs):
            super(net, self).__init__(nn.Module())

    ## TOO DOO finish init
    ## TOO DOO implement forward

    LowRank_FourierKernel_tx(**kwargs)
