import torch
from torch import nn

from .mesh import LocalQuad1D, Mesh


class concat_localbasis(nn.Module):
    def __init__(self, f1: nn.Module, f2: nn.Module):
        super().__init__()
        self.f1 = f1
        self.f2 = f2
        self.a = self.f1.a
        self.b = self.f2.b

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.where(
            x < 0.5 * (self.a + self.b), self.f1.forward(x), self.f2.forward(x)
        )


class zero_prolongation(nn.Module):
    def __init__(self, f: nn.Module):
        super().__init__()
        self.f = f
        self.a = self.f.a
        self.b = self.f.b

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        res = torch.zeros_like(x)
        cond = (self.a <= x) & (x <= self.b)
        res[cond] = self.f.forward(x[cond])
        return res


class LocalLagrangeBasis1D(nn.Module):
    def __init__(self, iloc, cell, localdof: LocalQuad1D):
        super().__init__()
        self.a = cell[0]
        self.b = cell[1]
        self.iloc = iloc
        self.localdof = localdof

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        _, xp = self.localdof.apply(self.a, self.b)
        c = [
            (x - xp[m]) / (xp[self.iloc] - xp[m])
            for m in range(self.localdof.order + 1)
            if m != self.iloc
        ]
        c = torch.stack(c)
        ans = torch.prod(c, dim=0)
        ## to do 0 en dehors de a,b
        return ans


class GlobaleLagrangeBasis1D(nn.Module):
    def __init__(self, idof: int, mesh: Mesh, localdof: LocalQuad1D):
        super().__init__()
        self.mesh = mesh
        self.localdof = localdof
        self.order = localdof.order
        self.idof = idof  ## full number  N+1 + N (order -1)

        ### mesh nodes
        if self.idof == 0:
            self.basis = LocalLagrangeBasis1D(0, self.mesh[0], self.localdof)
        if self.idof == self.mesh.nb_cells:
            self.basis = LocalLagrangeBasis1D(self.order, self.mesh[-1], self.localdof)
        if self.idof > 0 and self.idof < self.mesh.nb_cells:
            f1 = LocalLagrangeBasis1D(
                self.order, self.mesh[self.idof - 1], self.localdof
            )
            f2 = LocalLagrangeBasis1D(0, self.mesh[self.idof], self.localdof)
            self.basis = concat_localbasis(f1, f2)

        ## internal dof
        if self.idof > self.mesh.nb_cells:
            i = self.idof - (
                self.mesh.nb_cells + 1
            )  ## allows to go between 0 and N (order-1) -1
            icell = int(i / (self.order - 1))
            iloc = i % (self.order - 1)
            self.basis = LocalLagrangeBasis1D(iloc + 1, self.mesh[icell], self.localdof)

        self.globalbasis = zero_prolongation(self.basis)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.globalbasis.forward(x)


class ScalarLagrangeFE1D(nn.Module):
    def __init__(self, mesh, lquad):
        super().__init__()
        self.mesh = mesh
        self.lquad = lquad
        self.ndof = self.mesh.nb_nodes + self.mesh.nb_cells * (self.lquad.order - 1)
        self.linear = nn.Linear(self.ndof, 1, bias=False)

        self.basisfunctions = nn.ParameterList(
            [GlobaleLagrangeBasis1D(i, self.mesh, self.lquad) for i in range(self.ndof)]
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        basis_list = self.basisfunctions[0].forward(x)
        for i in range(1, self.ndof):
            basis_list = torch.cat(
                (basis_list, self.basisfunctions[i].forward(x)), dim=1
            )
        res = self.linear(basis_list)
        return res


class ScalarLagrangeFE1D_Parameters(nn.Module):
    def __init__(self, mesh, lquad):
        super().__init__()
        self.network = ScalarLagrangeFE1D(mesh, lquad)

    def forward(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        return self.network.forward(x)
