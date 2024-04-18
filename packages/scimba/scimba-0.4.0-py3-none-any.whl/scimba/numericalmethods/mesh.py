from abc import ABC, abstractmethod

# import time
import torch

from scimba.equations import domain


class Mesh(ABC):
    def __init__(self,xdomain:domain.AbstractDomain):
        self.dim =xdomain.dim
        self.xdomain = xdomain
        self.nodes= None
        self.cells = None
        self.nb_nodes =0
        self.nb_cells =0

    @abstractmethod
    def build(self):
        pass

    def __getitem__(self,i):
        return self.cells[i]


class UniformMesh(Mesh):
    def __init__(self,xdomain:domain.AbstractDomain,N:list=[10]):
        super().__init__(xdomain)
        self.N = N
        self.nb_nodes = 1
        self.nb_cells = 1
        for i in range(0,len(N)):
            self.nb_nodes= self.nb_nodes*(N[i]+1)
        for i in range(0,len(N)):
            self.nb_cells= self.nb_cells*N[i]

    def build(self):
        if self.dim==1:
            a=self.xdomain.bound[0][0]
            b=self.xdomain.bound[0][1]

            self.nodes= torch.linspace(a,b,self.N[0]+1)
            self.cells = torch.tensor([[self.nodes[i],self.nodes[i+1]] for i in range(0,self.N[0])])

            self.neighbords= []
            self.neighbords.append([0])
            for i in range(1,self.N[0]):
                self.neighbords.append([i-1,i])
            self.neighbords.append([self.N[0]-1])

class LocalQuad1D:
    def __init__(self,q:int):
        self.order = q

    def apply(self,a,b):
        if self.order==1:
            wp = torch.zeros(2); xp = torch.zeros(2)
            wp[0] = 0.5; xp[0]= 0.0
            wp[1] = 0.5; xp[1]= 1.0
        elif self.order==2:
            wp = torch.zeros(3); xp = torch.zeros(3)
            wp[0] = 0.166666666666666666666666666667; xp[0]= 0.0
            wp[1] = 0.666666666666666666666666666668; xp[1]= 0.5
            wp[2] = 0.166666666666666666666666666667; xp[2]= 1.0
        elif self.order==3:
            wp = torch.zeros(4); xp = torch.zeros(4)
            wp[0] = 0.0833333333333333333333333333333; xp[0]= 0.0
            wp[1] = 0.416666666666666666666666666666; xp[1]= 0.276393202250021030359082633127
            wp[2] = 0.416666666666666666666666666666; xp[2]= 0.723606797749978969640917366873
            wp[3] = 0.0833333333333333333333333333333; xp[3]= 1.0
        else:
            wp = torch.zeros(5); xp = torch.zeros(5)
            wp[0] = 0.05; xp[0]= 0.0
            wp[1] = 0.272222222222222222222222222223; xp[1]= 0.172673164646011428100853771877
            wp[2] = 0.355555555555555555555555555556; xp[2]= 0.5
            wp[3] = 0.272222222222222222222222222223; xp[3]= 0.827326835353988571899146228123
            wp[4] = 0.05; xp[4]= 1.0

        xp= (b-a) * xp + a*torch.ones_like(xp)
        wp= (b-a) * wp
        return wp,xp

class Sampling_MeshQuad1D:
    def __init__(self,lq:LocalQuad1D,mesh:Mesh):
        self.localquad = lq
        self.mesh = mesh
        self.n_collocation = (self.mesh.nb_cells +1) + self.mesh.nb_cells*(self.localquad.order-1)
        self.n_bc_collocation = 2

    def sampling(self,n_points):
        N = self.mesh.nb_cells
        quadpoints = torch.zeros((self.localquad.order+1)*N)

        q =self.localquad.order +1
        for i in range(0,N):
            a= self.mesh[i][0]
            b= self.mesh[i][1]
            _,quadpoints[i*q:(i+1)*q]= self.localquad.apply(a,b)

        quadpoints.requires_grad_()
        return quadpoints

    def bc_sampling(self,n_points):
        N = self.mesh.nb_cells
        bc_point = torch.tensor([self.mesh.nodes[0],self.mesh.nodes[-1]])

        bc_point.requires_grad_()
        return bc_point

    def density(self, x):
        return 1


