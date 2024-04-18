import torch

from .pdes import AbstractODE

PI = 3.14159265358979323846

###
# Description: this file contains example of nonlinear classic and conservative ODE
###


class SimpleNonlinearOde(AbstractODE):
    r"""
    Class to define the problem:

    .. math::
        \frac{du}{dt} - alpha * t / u = 0
        u(0) = 1

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`. 

    We use the model :math:`u_{\theta}=u_0+t NN(t)`
    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return torch.ones_like(alpha)

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        return u_t - alpha * t / u

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t*w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**2)


class SimpleNonlinearOdeFactored(AbstractODE):
    r"""
    Class to define the problem:

    .. math::

        \frac{d(u^2 / 2)}{dt} - alpha * t = 0
        u(0) = 1

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`

    We use the model :math:`u_{\theta}=u_0+t NN(t)`
    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

        self.f_t = lambda w, t, mu: self.get_variables(w) ** 2 / 2

    def initial_condition(self, mu, **kwargs):
        return torch.ones_like(mu[:, 0, None])

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        f_u_t = self.get_variables(w, "f_w_t")
        return f_u_t - alpha * t

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t*w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**2)


class SimpleNonlinearSecondOrderOde(AbstractODE):
    r"""
    Class to define the problem:

    .. math::

        u * \frac{d^2 u}{dt^2} + \left(\frac{du}{dt}\right)^2 - 3 * alpha * t = 0
        u(0) = 1
        u'(0) = 0

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`

    We use the model :math:`u_{\theta}=u_0+t NN(t)`
    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return [torch.ones_like(alpha), torch.zeros_like(alpha)]

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        u_tt = self.get_variables(w, "w_tt")
        return u * u_tt + u_t**2 - 3 * alpha * t

    def bc_add(self, t, mu, w):
        return torch.ones_like(w)

    def bc_mul(self, t, mu):
        return t

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**3)


class SimpleNonlinearSecondOrderOdeFactored(AbstractODE):
    r"""
    Class to define the problem:

    .. math::

        \frac{d^2 (u^2 / 2)}{dt^2} - 3 * alpha * t = 0
        u(0) = 1
        u'(0) = 0

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`

    We use the model :math:`u_{\theta}=u_0+t NN(t)`

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = False
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

        self.f_tt = lambda w, t, mu: self.get_variables(w) ** 2 / 2

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return [torch.ones_like(alpha), torch.zeros_like(alpha)]

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        f_u_tt = self.get_variables(w, "f_w_tt")
        return f_u_tt - 3 * alpha * t

    def bc_add(self, t, mu, w):
        return torch.ones_like(w)

    def bc_mul(self, t, mu):
        return t

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**3)


class SimpleNonlinearFirstAndSecondOrderOde(AbstractODE):
    r"""
    Class to define the problem:

    .. math::

        2 * u * (\frac{d^2 u}{dt^2} + \frac{du}{dt}\right)
        + 2 * \left(\frac{du}{dt}\right)^2 - alpha * t = 0
        u(0) = 1
        u'(0) = 0

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`

    We use the model :math:`u_{\theta}=u_0+t NN(t)`

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return [torch.ones_like(alpha), torch.zeros_like(alpha)]

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        u_tt = self.get_variables(w, "w_tt")
        return 2 * u * (u_tt + u_t) + 2 * u_t**2 - alpha * t

    def bc_add(self, t, mu, w):
        return torch.ones_like(w)

    def bc_mul(self, t, mu):
        return t

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * (t**2 / 2 - t + 1 - torch.exp(-t)))


class SimpleNonlinearFirstAndSecondOrderOdeFactored(AbstractODE):
    r"""
    Class to define the problem:
    
    .. math::

        \frac{d^2(u^2)}{dt^2} + \frac{d^2(u^2)}{dt^2} - alpha * t = 0
        u(0) = 1
        u'(0) = 0

    with :math:`\alpha \in [0.5,1.5], t\in [0,1]`

    We use the model :math:`u_{\theta}=u_0+t NN(t)`

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 1.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"
        self.f_t = lambda w, t, mu: self.get_variables(w) ** 2
        self.f_tt = lambda w, t, mu: self.get_variables(w) ** 2

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return [torch.ones_like(alpha), torch.zeros_like(alpha)]

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        f_u_t = self.get_variables(w, "f_w_t")
        f_u_tt = self.get_variables(w, "f_w_tt")
        return f_u_tt + f_u_t - alpha * t

    def bc_add(self, t, mu, w):
        return torch.ones_like(w)

    def bc_mul(self, t, mu):
        return t

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * (t**2 / 2 - t + 1 - torch.exp(-t)))
