import torch
from torch import nn


class GradPotential(nn.Module):
    def __init__(self, y_dim, p_dim, width, **kwargs):
        super().__init__()
        self.linear_y = nn.Linear(y_dim, width, bias=False)
        self.linear_p = nn.Linear(p_dim, width)
        self.activation = kwargs.get('activation', nn.Tanh())
        self.scaling = nn.Linear(p_dim, width)

    def forward(self, y, p):
        z = self.activation(self.linear_y(y) + self.linear_p(p))
        return (self.scaling(p) * z) @ self.linear_y.weight


# Parameter size could be made lazy to seemlessly merge with non-parametric implementation.
# Currently, this still works with `p_dim = 0` (despite a zero-size warning), so perhaps it could already be merged.
class HenonLayer(nn.Module):
    def __init__(self, y_dim, p_dim, **kwargs):
        super().__init__()
        width = kwargs.get('width', 5)
        self.grad_potential = GradPotential(y_dim, p_dim, width)
        self.shift = kwargs.get('shift', nn.Linear(p_dim, y_dim))
        self.hard_init_cond = kwargs.get('hard_init_cond', True)

    def forward(self, x, y, p):
        t = p[:, 0, None] if self.hard_init_cond else 1.0
        x, y = y + t * self.shift(p), -x + t * self.grad_potential(y, p) # 1st iteration
        x, y = y + t * self.shift(p), -x + t * self.grad_potential(y, p) # 2nd iteration
        x, y = y + t * self.shift(p), -x + t * self.grad_potential(y, p) # 3rd iteration
        x, y = y + t * self.shift(p), -x + t * self.grad_potential(y, p) # 4th iteration
        return x, y


class HenonNet(nn.Module):
    def __init__(self, y_dim, p_dim, widths = [12] * 20, **kwargs):
        super().__init__()
        self.y_dim = y_dim
        self.p_dim = p_dim
        self.layers = nn.ModuleList([HenonLayer(y_dim, p_dim, width=w, **kwargs) for w in widths])

    def forward(self, inputs: torch.Tensor):
        x, y, p = inputs.tensor_split((self.y_dim, 2*self.y_dim, ), dim=1)
        for layer in self.layers:
            x, y = layer(x, y, p)
        return torch.cat((x, y), dim=1)