import scimba.equations as eq
import scimba.nets.mlp as mlp
from torch import nn
from torch.autograd import grad as grad


class MLPLocalSubLayer_t(nn.Module):
    def __init__(self, in_size: int, out_size: int, ode: eq.AbstractODE, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        self.layer_type = kwargs.get("layer_type", "linear")
        self.t_dependency = kwargs.get("t_dependency", False)
        self.mu_dependency = kwargs.get("mu_dependency", False)
        self.nb_parameters = ode.nb_parameters

        in_size_f = (
            in_size + self.t_dependency + self.mu_dependency * self.nb_parameters
        )
        if self.layer_type == "linear":
            self.layer = nn.Linear(in_size_f, out_size)
        elif self.layer_type == "semilinear":
            self.layer = mlp.GenericMLP(
                1 + self.mu_dependency * self.nb_parameters,
                in_size * out_size,
                **kwargs,
            )
        else:
            self.layer = mlp.GenericMLP(in_size_f, out_size, **kwargs)

    ## TOO DOO implement forward
    pass


class MLPLocalSubLayer_x(nn.Module):
    def __init__(self, in_size: int, out_size: int, pde: eq.AbstractPDEx, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        self.layer_type = kwargs.get("layer_type", "linear")
        self.x_dependency = kwargs.get("x_dependency", False)
        self.xdim = pde.dimension_x
        self.mu_dependency = kwargs.get("mu_dependency", False)
        self.nb_parameters = pde.nb_parameters

        in_size_f = (
            in_size
            + self.x_dependency * self.x_dim
            + self.mu_dependency * self.nb_parameters
        )
        if self.layer_type == "linear":
            self.layer = nn.Linear(in_size_f, out_size)
        elif self.layer_type == "semilinear":
            self.layer = mlp.GenericMLP(
                self.x_dim + self.mu_dependency * self.nb_parameters,
                in_size * out_size,
                **kwargs,
            )
        else:
            self.layer = mlp.GenericMLP(in_size_f, out_size, **kwargs)


## TOO DOO implement forward


class MLPLocalSubLayer_tx(nn.Module):
    def __init__(self, in_size: int, out_size: int, pde: eq.AbstractPDEtx, **kwargs):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        self.layer_type = kwargs.get("layer_type", "linear")
        self.t_dependency = kwargs.get("t_dependency", False)
        self.x_dependency = kwargs.get("x_dependency", False)
        self.xdim = pde.dimension_x
        self.mu_dependency = kwargs.get("mu_dependency", False)
        self.nb_parameters = pde.nb_parameters

        in_size_f = (
            in_size
            + self.t_dependency
            + self.x_dependency * self.x_dim
            + self.mu_dependency * self.nb_parameters
        )
        if self.layer_type == "linear":
            self.layer = nn.Linear(in_size_f, out_size)
        elif self.layer_type == "semilinear":
            self.layer = mlp.GenericMLP(
                1 + self.x_dim + self.mu_dependency * self.nb_parameters,
                in_size * out_size,
                **kwargs,
            )
        else:
            self.layer = mlp.GenericMLP(in_size_f, out_size, **kwargs)

    ## TOO DOO implement forward
