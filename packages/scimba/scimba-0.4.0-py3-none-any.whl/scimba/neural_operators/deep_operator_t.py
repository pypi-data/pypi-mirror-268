from torch import nn
from torch.autograd import grad as grad


def LinearGreenOperator_t(knet: nn.Module, **kwargs):
    class LinearGreenOperator_t(knet):
        def __int__(self, in_size, out_size, **kwargs):
            super(knet, self).__init__(nn.Module())
            self.in_size = in_size
            self.out_size = out_size
            self.activate_local_sublayer = kwargs.get("activate_local_sublayer", True)
            self.activate_kernel_sublayer = kwargs.get("activate_kernel_sublayer", True)
            self.time_continuous = kwargs.get("time_continuous", True)

    ## TOO DOO finish init
    ## TOO DOO implement forward

    return LinearGreenOperator_t(**kwargs)


def LowRank_LinearGreenOperator_t(knet: nn.Module, **kwargs):
    class LowRank_LinearGreenOperator_t(knet):
        def __int__(self, in_size, out_size, **kwargs):
            self.in_size = in_size
            self.out_size = out_size
            self.activate_local_sublayer = kwargs.get("activate_local_sublayer", True)
            self.activate_kernel_sublayer = kwargs.get("activate_kernel_sublayer", True)
            self.time_continuous = kwargs.get("time_continuous", True)

    ## TOO DOO finish init
    ## TOO DOO implement forward

    return LowRank_LinearGreenOperator_t(**kwargs)


def DeepGreenOperator_t(layer: nn.Module, **kwargs):
    class DeepGreenOperator_t(layer):
        def __int__(self, in_size, out_size, **kwargs):
            super(layer, self).__init__(nn.Module())
            self.in_size = in_size
            self.out_size = out_size
            self.nb_layers = kwargs.get("nb_layers", 1)
            self.dim_layers = kwargs.get(
                "dim_layers", [[in_size, 1], [1, 1], [1, out_size]]
            )
            self.bool_kernel_sb = kwargs.get("bool_kernel_sb", [True])
            self.bool_local_sb = kwargs.get("bool_local_sb", [True])

    ## TOO DOO finish init
    ## TOO DOO implement forward

    return DeepGreenOperator_t(**kwargs)
