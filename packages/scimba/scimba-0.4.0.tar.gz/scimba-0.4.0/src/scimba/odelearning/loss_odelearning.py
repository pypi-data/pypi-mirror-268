
import sys
import copy

import torch
import torch.nn as nn
import pylab as plt
from abc import ABC, abstractmethod


class LossODELearning_withdata(ABC):

    def __init__(self, ode):
        self.ode = ode 
       
    @abstractmethod
    def apply(self,x,x_ref,t,mu):
        """
        x: shape(nb_time, nb_samples, nb_unknowns)
        """
        pass

    def averaged_sampled_solutions(self,x,time_index):
        n= len(x[time_index,:,0])
        if self.ode.nb_parameters == 1:
            return sum(x[:,time_index,0])/n
        else:
            return (sum(x[:,time_index,i])/n for i in range(self.nb_parameters))
        
    def averaged_time_solutions(self,x):
        if self.ode.nb_parameters == 1:
            return sum(x[:,:,0],axis=0)
        else:
            return (sum(x[:,:,i],axis=0) for i in range(self.nb_parameters))
        

class LossODELearning(ABC):

    def __init__(self, ode):
        self.ode = ode 
       
    @abstractmethod
    def apply(self,x,t,mu):
        """
        x: shape(nb_time, nb_samples, nb_unknowns)
        """
        pass

    def averaged_sampled_solutions(self,x,time_index):
        n= len(x[time_index,:,0])
        if self.ode.nb_parameters == 1:
            return sum(x[:,time_index,0])/n
        else:
            return (sum(x[:,time_index,i])/n for i in range(self.nb_parameters))
        
    def averaged_time_solutions(self,x):
        if self.ode.nb_parameters == 1:
            return sum(x[:,:,0],axis=0)
        else:
            return (sum(x[:,:,i],axis=0) for i in range(self.nb_parameters))