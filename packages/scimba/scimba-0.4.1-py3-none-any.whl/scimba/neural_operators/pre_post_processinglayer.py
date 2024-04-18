import scimba.nets.mlp as mlp
import scimba.equations as eq
import scimba.largenets.pointnet as pointnet
import torch
from torch import nn
from torch.autograd import grad as grad

def PrePostProcessingLayer_t(net: nn.Module,**kwargs):
    class PrePostProcessingLayer_t(net):
        def __int__(self,in_size:int,out_size:int,ode:eq.AbstractODE,**kwargs):
            self.in_size= in_size
            self.out_size = out_size
            self.t_dependency = kwargs.get('t_dependency',False)

            self.mu_dependency = kwargs.get('mu_dependency',False)
            self.nb_parameters = ode.nb_parameters

            in_size_f=  in_size + self.t_dependency + self.mu_dependency*self.nb_parameters
            self.layer = net(in_size_f,out_size)

        def forward(self,t:torch.Tensor,f:torch.Tensor,mu:torch.Tensor) -> torch.Tensor:
            inputs = f
            if self.time_dependency==True:
                inputs= torch.cat([inputs,t],axis=1)
            if self.mu_dependency==True:
                inputs=torch.cat([inputs,mu],axis=1)

            return self.layer(inputs)

        
    return PrePostProcessingLayer_t(**kwargs)


def PrePostProcessingLayer_x(net: nn.Module,**kwargs):
    class PrePostProcessingLayer_x(net):
        def __int__(self,in_size:int,out_size:int,pde:eq.AbstractPDEx,**kwargs):
            self.in_size= in_size
            self.out_size = out_size
            self.x_dependency = kwargs.get('x_dependency',False)
            self.x_dim = pde.dimension_x
            self.mu_dependency = kwargs.get('mu_dependency',False)
            self.nb_parameters = pde.nb_parameters

            in_size_f=  in_size + self.x_dependency*self.x_dim + self.mu_dependency*self.nb_parameters
            self.layer = net(in_size_f,out_size)

        def forward(self,x:torch.Tensor,f:torch.Tensor,mu:torch.Tensor) -> torch.Tensor:
            inputs = f
            if self.x_dependency==True:
                inputs= torch.cat([inputs,x],axis=1)
            if self.mu_dependency==True:
                inputs=torch.cat([inputs,mu],axis=1)

            return self.layer(inputs)

        
    return PrePostProcessingLayer_x(**kwargs)

def PrePostProcessingLayer_tx(net: nn.Module,**kwargs):
    class PrePostProcessingLayer_tx(net):
        def __int__(self,in_size:int,out_size:int,pde:eq.AbstractPDEtx,**kwargs):
            self.in_size= in_size
            self.out_size = out_size
            self.tx_dependency = kwargs.get('tx_dependency',False)
            self.x_dim = pde.dimension_x
            self.mu_dependency = kwargs.get('mu_dependency',False)
            self.nb_parameters = pde.nb_parameters

            in_size_f=  in_size + self.tx_dependency*(self.x_dim+1) + self.mu_dependency*self.nb_parameters
            self.layer = net(in_size_f,out_size)
            

        def forward(self,t:torch.Tensor,x:torch.Tensor,f:torch.Tensor,mu:torch.Tensor) -> torch.Tensor:
            inputs = f
            if self.tx_dependency==True:
                inputs= torch.cat([inputs,t,x],axis=1)
            if self.mu_dependency==True:
                inputs=torch.cat([inputs,mu],axis=1)

            return self.layer(inputs)

        
    return PrePostProcessingLayer_tx(**kwargs)