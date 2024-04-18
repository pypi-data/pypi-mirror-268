from torch import nn
from torch.autograd import grad as grad

# kernel ==>  K(x,y,\mu)
# Lowrank kernel ==> sum_1^r K_i(x,\mu)K_i(y,\mu)


## begin Jeremy
class MLPKernel_x:
    # physic dim et parameter dim donnée par edp
    ## output du kernel matrice, input_dim, output_dim
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class LocalMLPKernel_x:
    ## output du kernel matrice, input_dim, output_dim
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class FourierKernel_x:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


class LocalFourierKernel_x:
    ## TOO DOO implement init
    ## TOO DOO implement forward
    pass


def LowRank_Kernel_x(net: nn.Module, **kwargs):
    class LowRank_Kernel_x(net):
        def __int__(self, in_size, out_size, **kwargs):
            super(net, self).__init__(nn.Module())

    ## TOO DOO finish init
    ## TOO DOO implement forward

    LowRank_Kernel_x(**kwargs)


## end jeremy
