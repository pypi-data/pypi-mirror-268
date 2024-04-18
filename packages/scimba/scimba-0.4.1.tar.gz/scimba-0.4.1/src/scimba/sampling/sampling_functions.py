from abc import ABC, abstractmethod
from typing import Union

import torch
from torch.distributions.bernoulli import Bernoulli

from . import uniform_sampling


class ParametricFunction_t(ABC):
    """
    Represents a parametric function which depends on the time variable t.

    :param dim_f: dimension of the function output
    :type dim_f: int

    :param dim_p: number of parameters
    :type dim_p: int

    :param p_domain: domain of the parameters
    :type p_domain: list (of lists of floats)
    """

    def __init__(self, dim_f: int = 1, dim_p: int = 1, p_domain: list = [[0.0, 1.0]]):
        self.dim_f = dim_f
        self.dim_p = dim_p
        self.p_domain = p_domain

    def get_parameters(self, params: torch.Tensor) -> Union[torch.Tensor, torch.Tensor]:
        """
        Returns the physical parameters from the parameter tensor.

        ----
        Inputs:
        - mu: the parameters tensor
        """
        if self.dim_p == 1:
            return params[:, 0, None]
        else:
            return (params[:, i, None] for i in range(self.dim_p))

    @abstractmethod
    def __call__(self, t: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
        pass


class Default_ParametricFunction_t(ParametricFunction_t):
    def __init__(self, dim_f: int = 1, dim_p: int = 1, p_domain: list = [[0.0, 1.0]]):
        super().__init__(dim_f, dim_p, p_domain)

    def __call__(self, t: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
        return t * self.get_parameters(params)


class ParametricFunction_x(ABC):
    """
    Represents a parametric function which depends on the space variable x.

    :param dim_f: dimension of the function output
    :type dim_f: int

    :param dim_x: space dimension
    :type dim_x: int

    :param dim_p: number of parameters
    :type dim_p: int

    :param p_domain: domain of the parameters
    :type p_domain: list (of lists of floats)
    """

    def __init__(
        self,
        dim_f: int = 1,
        dim_x: int = 1,
        dim_p: int = 1,
        p_domain: list = [[0.0, 1.0]],
    ):
        self.dim_f = dim_f
        self.dim_x = dim_x
        self.dim_p = dim_p
        self.p_domain = p_domain

    def get_parameters(self, params: torch.Tensor) -> Union[torch.Tensor, torch.Tensor]:
        """
        Returns the physical parameters from the parameter tensor.

        ----
        Inputs:
        - mu: the parameters tensor
        """
        if self.dim_p == 1:
            return params[:, 0, None]
        else:
            return (params[:, i, None] for i in range(self.dim_p))

    def get_coordinates(self, x: torch.Tensor) -> Union[torch.Tensor, torch.Tensor]:
        """
        Returns the physical coordinates from the x tensor.

        ----
        Inputs:
        - x: the coordinates tensor
        """
        if self.dim_x == 1:
            return x[:, 0, None]
        else:
            return (x[:, i, None] for i in range(self.dim_x))

    @abstractmethod
    def __call__(self, x: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
        pass


class Default_ParametricFunction_x(ParametricFunction_x):
    def __init__(
        self,
        dim_f: int = 1,
        dim_x: int = 1,
        dim_p: int = 1,
        p_domain: list = [[0.0, 1.0]],
    ):
        super().__init__(dim_f, dim_x, dim_p, p_domain)

    def __call__(self, x: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
        return x * self.get_parameters(params)


class ParametricFunction_tx(ABC):
    """
    Represents a parametric function which depends on the variables t and x.

    :param dim_f: dimension of the function output
    :type dim_f: int

    :param dim_x: space dimension
    :type dim_x: int

    :param dim_p: number of parameters
    :type dim_p: int

    :param p_domain: domain of the parameters
    :type p_domain: list (of lists of floats)
    """

    def __init__(
        self,
        dim_f: int = 1,
        dim_x: int = 1,
        dim_p: int = 1,
        p_domain: list = [[0.0, 1.0]],
    ):
        self.dim_p = dim_p
        self.dim_f = dim_f
        self.dim_x = dim_x
        self.p_domain = p_domain

    def get_parameters(self, params: torch.Tensor) -> Union[torch.Tensor, torch.Tensor]:
        """
        Returns the physical parameters from the parameter tensor.

        ----
        Inputs:
        - mu: the parameters tensor
        """
        if self.dim_p == 1:
            return params[:, 0, None]
        else:
            return (params[:, i, None] for i in range(self.dim_p))

    def get_coordinates(self, x: torch.Tensor) -> Union[torch.Tensor, torch.Tensor]:
        """
        Returns the physical coordinates from the x tensor.

        ----
        Inputs:
        - x: the coordinates tensor
        """
        if self.dim_x == 1:
            return x[:, 0, None]
        else:
            return (x[:, i, None] for i in range(self.dim_x))

    @abstractmethod
    def __call__(
        self, t: torch.Tensor, x: torch.Tensor, params: torch.Tensor
    ) -> torch.Tensor:
        pass


class Default_ParametricFunction_tx(ParametricFunction_tx):
    def __init__(
        self,
        dim_f: int = 1,
        dim_x: int = 1,
        dim_p: int = 1,
        p_domain: list = [[0.0, 1.0]],
    ):
        super().__init__(dim_f, dim_x, dim_p, p_domain)

    def __call__(
        self, x: torch.Tensor, t: torch.Tensor, params: torch.Tensor
    ) -> torch.Tensor:
        return t * x * self.get_parameters(params)


class ParametricFunctionsSampler_t:
    def __init__(
        self,
        class_f: ParametricFunction_t,
        t_sensor: torch.Tensor = None,
        t_loss: torch.Tensor = None,
        proba: float = 0.9,
        **kwargs,
    ):
        self.f_dim = class_f.dim_f
        self.params_dim = class_f.dim_p
        self.params_domain = class_f.p_domain
        self.sampler_params = uniform_sampling.UniformSampling(
            self.params_dim, self.params_domain
        )

        self.t_sensor = t_sensor
        self.t_loss = t_loss
        self.f = class_f
        self.bernoulli_sampling = Bernoulli(torch.Tensor([proba]))

        self.coupling_training = False

    def sampling(self, n_f: int) -> Union[torch.Tensor, torch.Tensor]:
        self.params = self.sampler_params.sampling(n_f)

        f_sensor = torch.zeros((n_f, self.t_sensor.shape[0], self.f_dim))
        f_loss = torch.zeros((n_f, self.t_loss.shape[0], self.f_dim))

        for i in range(n_f):
            switch = self.bernoulli_sampling.sample().item()
            params_sensor = self.params[i].repeat(self.t_sensor.shape[0], 1)
            params_loss = self.params[i].repeat(self.t_loss.shape[0], 1)
            f_sensor[i] = self.f(self.t_sensor, params_sensor)
            f_loss[i] = switch * self.f(self.t_loss, params_loss)

        return f_sensor, f_loss


class ParametricFunctionsSampler_x:
    def __init__(
        self,
        class_f: ParametricFunction_x,
        x_sensor: torch.Tensor = None,
        x_loss: torch.Tensor = None,
        **kwargs,
    ):
        self.f_dim = class_f.dim_f
        self.params_dim = class_f.dim_p
        self.params_domain = class_f.p_domain
        self.sampler_params = uniform_sampling.UniformSampling(
            self.params_dim, self.params_domain
        )

        self.x_sensor = x_sensor
        self.x_loss = x_loss
        self.f = class_f

        self.coupling_training = False

    def sampling(self, n_f: int) -> Union[torch.Tensor, torch.Tensor]:
        self.params = self.sampler_params.sampling(n_f)

        f_sensor = torch.zeros((n_f, self.x_sensor.shape[0], self.f_dim))
        f_loss = torch.zeros((n_f, self.x_loss.shape[0], self.f_dim))

        for i in range(n_f):
            params_sensor = self.params[i].repeat(self.x_sensor.shape[0], 1)
            params_loss = self.params[i].repeat(self.x_loss.shape[0], 1)
            f_sensor[i] = self.f(self.x_sensor, params_sensor)
            f_loss[i] = self.f(self.x_loss, params_loss)

        return f_sensor, f_loss


class ParametricFunctionsSampler_tx:
    def __init__(
        self,
        class_f: ParametricFunction_tx,
        t_sensor: torch.Tensor = None,
        t_loss: torch.Tensor = None,
        x_sensor: torch.Tensor = None,
        x_loss: torch.Tensor = None,
        **kwargs,
    ):
        self.f_dim = class_f.dim_f
        self.params_dim = class_f.dim_p
        self.params_domain = class_f.p_domain
        self.sampler_params = uniform_sampling.UniformSampling(
            self.params_dim, self.params_domain
        )

        self.t_sensor = t_sensor
        self.t_loss = t_loss
        self.x_sensor = x_sensor
        self.x_loss = x_loss
        self.f = class_f

        self.coupling_training = False

    def sampling(self, n_f: int) -> Union[torch.Tensor, torch.Tensor]:
        params = self.sampler_params.sampling(n_f)

        f_sensor = torch.zeros((n_f, self.t_sensor.shape[0], self.f_dim))
        f_loss = torch.zeros((n_f, self.t_loss.shape[0], self.f_dim))

        for i in range(0, n_f):
            params_sensor = params[i].repeat(self.t_sensor.shape[0], 1)
            params_loss = params[i].repeat(self.t_loss.shape[0], 1)
            f_sensor[i] = self.f(self.t_sensor, self.x_sensor, params_sensor)
            f_loss[i] = self.f(self.t_loss, self.x_loss, params_loss)

        return f_sensor, f_loss


###### old way of sampling (to be deleted) ######


# def id_f(t, x, params):
#     if t is None:
#         res = torch.ones_like(x)
#     elif x is None:
#         res = torch.ones_like(t)
#     else:
#         res = torch.ones_like(t, x)
#     return res


# class FunctionsSampler:
#     def __init__(self, p_dim, p_domain, sampler, **kwargs):
#         self.sampler = sampler
#         self.params_dim = p_dim
#         self.params_domain = p_domain
#         self.sampler_params = uniform_sampling.UniformSampling(
#             self.params_dim, self.params_domain
#         )

#         self.t_sampler = kwargs.get("t_sampler", None)
#         self.x_sampler = kwargs.get("x_sampler", None)
#         self.f = kwargs.get("f", id_f)
#         self.fourier_data = kwargs.get("fourier_data", False)
#         self.N = kwargs.get("n_sensor", 50)
#         self.resampling_sensor = kwargs.get("resampling_sensor", False)

#         self.coupling_training = False

#         if self.t_sampler is not None:
#             self.t_sensor = self.t_sampler.sampling(self.N)
#         if self.x_sampler is not None:
#             self.x_sensor = self.x_sampler.sampling(self.N)

#     def sampling(self, n_f, n_points):
#         if n_f == 0 and n_points == 0:
#             return None, None, None, None

#         if self.resampling_sensor:
#             if self.t_sampler is not None:
#                 self.t_sensor = self.t_sampler.sampling(self.N)
#             if self.x_sampler is not None:
#                 self.x_sensor = self.x_sampler.sampling(self.N)

#         params = self.sampler_params.sampling(n_f)
#         self.params = params

#         if self.x_sampler is None:
#             t_sensor = self.t_sensor
#             t_sensor = t_sensor[:, :, None]  # [n_sensor, dim_t, 1]
#             t_sensor = torch.transpose(t_sensor, 0, 2)  # [1, dim_t, n_sensor]
#             t_sensor = t_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_t, n_sensor]
#             f_sensor = self.f(self.t_sensor, params[0, :])
#             f_sensor = f_sensor[:, :, None]  # [n_sensor, dim_f, 1]
#             f_sensor = torch.transpose(f_sensor, 0, 2)  # [1, dim_f, n_sensor]
#             f_sensor = f_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_f, n_sensor]
#             t, mu = self.sampler.sampling(n_points)
#             f = self.f(t, params[0, :].unsqueeze(0))
#             for i in range(1, len(params)):
#                 f_sensor_l = self.f(self.t_sensor, params[i, :])
#                 f_sensor_l = f_sensor_l[:, :, None]
#                 f_sensor_l = torch.transpose(f_sensor_l, 0, 2)
#                 f_sensor_l = f_sensor_l.repeat(n_points, 1, 1)
#                 t_l, mu_l = self.sampler.sampling(n_points)
#                 f_l = self.f(t_l, params[i, :].unsqueeze(0))

#                 f_sensor = torch.cat([f_sensor, f_sensor_l], axis=0)
#                 t = torch.cat([t, t_l], axis=0)
#                 mu = torch.cat([mu, mu_l], axis=0)
#                 f = torch.cat([f, f_l], axis=0)
#             # t_sensor is the same indepent of params so we put it outside of
#             # the loop for the sake of simplicity
#             t_sensor = t_sensor.repeat(len(params), 1, 1)
#             return t_sensor, f_sensor, t, mu, f

#         elif self.t_sampler is None:
#             x_sensor = self.x_sensor  # [n_sensor, dim_x]
#             x_sensor = x_sensor[:, :, None]  # [n_sensor, dim_x, 1]
#             x_sensor = torch.transpose(x_sensor, 0, 2)  # [1, dim_x, n_sensor]
#             x_sensor = x_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_x, n_sensor]
#             f_sensor = self.f(self.x_sensor, params[0, :])  # [n_sensor, dim_f]
#             f_sensor = f_sensor[:, :, None]  # [n_sensor, dim_f, 1]
#             f_sensor = torch.transpose(f_sensor, 0, 2)  # [1, dim_f, n_sensor]
#             f_sensor = f_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_f, n_sensor]
#             x, mu = self.sampler.sampling(n_points)
#             f = self.f(x, params[0, :])
#             for i in range(1, len(params)):
#                 f_sensor_l = self.f(self.x_sensor, params[i, :])
#                 f_sensor_l = f_sensor_l[:, :, None]
#                 f_sensor_l = torch.transpose(f_sensor_l, 0, 2)
#                 f_sensor_l = f_sensor_l.repeat(n_points, 1, 1)
#                 x_l, mu_l = self.sampler.sampling(n_points)
#                 f_l = self.f(x_l, params[i, :])

#                 # x_sensor = torch.cat([x_sensor, x_l], axis=0)
#                 f_sensor = torch.cat([f_sensor, f_sensor_l], axis=0)
#                 x = torch.cat([x, x_l], axis=0)
#                 mu = torch.cat([mu, mu_l], axis=0)
#                 f = torch.cat([f, f_l], axis=0)
#             # x_sensor is the same indepent of params so we put it outside of
#             # the loop for the sake of simplicity
#             x_sensor = x_sensor.repeat(len(params), 1, 1)
#             return x_sensor, f_sensor, x, mu, f

#         else:
#             t_sensor = self.t_sensor
#             t_sensor = t_sensor[:, :, None]  # [n_sensor, dim_t, 1]
#             t_sensor = torch.transpose(t_sensor, 0, 2)  # [1, dim_t, n_sensor]
#             t_sensor = t_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_t, n_sensor]
#             x_sensor = self.x_sensor  # [n_sensor, dim_x]
#             x_sensor = x_sensor[:, :, None]  # [n_sensor, dim_x, 1]
#             x_sensor = torch.transpose(x_sensor, 0, 2)  # [1, dim_x, n_sensor]
#             x_sensor = x_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_x, n_sensor]
#             f_sensor = self.f(self.t_sensor, self.x_sensor, params[0, :])
#             f_sensor = f_sensor[:, :, None]  # [n_sensor, dim_f, 1]
#             f_sensor = torch.transpose(f_sensor, 0, 2)  # [1, dim_f, n_sensor]
#             f_sensor = f_sensor.repeat(n_points, 1, 1)  # [N_batched, dim_f, n_sensor]
#             t, x, mu = self.sampler.sampling(n_points)
#             f = self.f(t, x, params[0, :].unsqueeze(0))
#             for i in range(1, len(params)):
#                 f_sensor_l = self.f(self.t_sensor, self.x_sensor, params[i, :])
#                 f_sensor_l = f_sensor_l[:, :, None]
#                 f_sensor_l = torch.transpose(f_sensor_l, 0, 2)
#                 f_sensor_l = f_sensor_l.repeat(n_points, 1, 1)
#                 t_l, x_l, mu_l = self.sampler.sampling(n_points)
#                 f_l = self.f(t_l, x_l, params[i, :].unsqueeze(0))

#                 f_sensor = torch.cat([f_sensor, f_sensor_l], axis=0)
#                 t = torch.cat([t, t_l], axis=0)
#                 x = torch.cat([x, x_l], axis=0)
#                 mu = torch.cat([mu, mu_l], axis=0)
#                 f = torch.cat([f, f_l], axis=0)
#             # t_sensor and x_sensor are the same indepent of params so we put
#             # it outside of the loop for the sake of simplicity
#             t_sensor = t_sensor.repeat(len(params), 1, 1)
#             x_sensor = x_sensor.repeat(len(params), 1, 1)
#             return t_sensor, x_sensor, f_sensor, t, x, mu, f


# # for make data compute f use that at the beginning and compute sol with the f
# # f is given to the PDE by a function
