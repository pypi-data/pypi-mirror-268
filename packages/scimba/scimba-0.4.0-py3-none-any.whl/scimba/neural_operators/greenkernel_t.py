from torch import nn
from torch.autograd import grad as grad


class MLPKernel_t:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class FourierKernel_t:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


def LowRank_MLPKernel_t(net: nn.Module, **kwargs):
    class LowRank_MLPKernel_t(net):
        def __int__(self, in_size, out_size, **kwargs):
            super(net, self).__init__(nn.Module())

    ## TOO DOO finish init
    ## TOO DOO implement forward

    LowRank_MLPKernel_t(**kwargs)


def LowRank_FourierKernel_t(net: nn.Module, **kwargs):
    class LLowRank_FourierKernel_t(net):
        def __int__(self, in_size, out_size, **kwargs):
            super(net, self).__init__(nn.Module())

    ## TOO DOO finish init
    ## TOO DOO implement forward

    LowRank_FourierKernel_t(**kwargs)
