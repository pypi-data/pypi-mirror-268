import torch

from .pdes import AbstractODE


class SimpleOde(AbstractODE):
    r"""
    .. math::

        \frac{u}{dt} + \mu u = 0

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 10.0],
            nb_parameters=1,
            parameter_domain=[[0.5, 1]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        return torch.ones_like(mu[:, 0, None])

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        return u_t + alpha * u

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    # construit le jeu de données autrement qu'en samplant la solution de reference
    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.exp(-alpha * t)


class SimpleNonlinearOde(AbstractODE):
    r"""
    .. math::

        \frac{du}{dt} - alpha * t / u = 0
        u(0) = 1

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
        return torch.ones_like(mu[:, 0, None])

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        return u_t - alpha * t / u

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**2)


class SimpleNonlinearOdeFactored(AbstractODE):
    r"""
    .. math::

        \frac{d(u^2 / 2)}{dt} - alpha * t = 0
        u(0) = 1

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
        self.f_t = lambda u: u**2 / 2

    def initial_condition(self, mu, **kwargs):
        return torch.ones_like(mu[:, 0, None])

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        f_u_t = self.get_variables(w, "f_w_t")
        return f_u_t - alpha * t

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**2)


class SimpleNonlinearSecondOrderOde(AbstractODE):
    r"""
    .. math::

        u * \frac{d^2 u}{dt^2} + \left(\frac{du}{dt}\roght)^2 - 3 * alpha * t = 0
        u(0) = 1
        u'(0) = 0

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

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**3)


class SimpleNonlinearSecondOrderOdeFactored(AbstractODE):
    r"""
    .. math::

        \frac{d^2(u^2 / 6)}{dt^2} - alpha * t = 0
        u(0) = 1
        u'(0) = 0

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
        self.f_tt = lambda u: u**2 / 6

    def initial_condition(self, mu, **kwargs):
        alpha = self.get_parameters(mu)
        return [torch.ones_like(alpha), torch.zeros_like(alpha)]

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        f_u_tt = self.get_variables(w, "f_w_tt")
        return f_u_tt - alpha * t

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def make_data(self, n_data):
        pass

    def reference_solution(self, t, mu):
        alpha = self.get_parameters(mu)
        return torch.sqrt(1 + alpha * t**3)


class AmortizedPendulum(AbstractODE):
    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 20.0],
            nb_parameters=2,
            parameter_domain=[[1.0, 1.5], [1.0, 1.5]],
        )

        self.first_derivative = True
        self.second_derivative = True
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        c = 0.02
        lam, omega = self.get_parameters(mu)
        du0 = -c * lam * omega * 0.5
        return [
            0.5 * torch.ones_like(lam),
            du0 * torch.ones_like(lam),
        ]

    def residual(self, w, t, mu, **kwargs):
        c = 0.02
        lam, omega = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        u_tt = self.get_variables(w, "w_tt")
        return u_tt + 2 * c * lam * omega * u_t + omega * omega * u

    def make_data(self, n_data):
        # construit le jeu de données autrement qu'en samplant la solution de reference
        pass

    def reference_solution(self, t, mu):
        c = 0.02
        lam, omega = self.get_parameters(mu)
        return (
            0.5
            * torch.exp(-c * lam * omega * t)
            * torch.cos((1 - c * c * lam * lam) ** (0.5) * omega * t)
        )


class SimpleOdeWithSource(AbstractODE):
    r"""
    .. math::

        \frac{du}{dt} + \alpha u = f

    """

    def __init__(self):
        super().__init__(
            nb_unknowns=1,
            time_domain=[0, 10.0],
            nb_parameters=1,
            parameter_domain=[[0.99999, 1]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        return torch.ones_like(mu[:, 0, None])

    def residual(self, w, t, mu, **kwargs):
        alpha = self.get_parameters(mu)
        u = self.get_variables(w)
        u_t = self.get_variables(w, "w_t")
        f = kwargs.get("f", None)
        return u_t + alpha * u - f

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def reference_solution(self, t, mu):
        return None


class NonlinearPendulum(AbstractODE):
    """dq/dt = p, dp/dt = -ω*sin(q)

    First-order ODE with a single parameter ω.
    The initial condition is fixed to be q(0) = 0.97*π, p(0) = 0.
    """

    def __init__(self):
        super().__init__(
            nb_unknowns=2,
            time_domain=[0, 30.0],
            nb_parameters=1,
            parameter_domain=[[0.9, 1.1]],
        )

        self.first_derivative = True
        self.second_derivative = False
        self.t_min, self.t_max = self.time_domain[0], self.time_domain[1]
        self.data_construction = "sampled"

    def initial_condition(self, mu, **kwargs):
        omega = self.get_parameters(mu)
        q0 = 0.97 * torch.pi * torch.ones_like(omega)
        p0 = torch.zeros_like(omega)
        return torch.cat((q0, p0), axis=1)

    def vector_field(self, w, t, mu):
        omega = self.get_parameters(mu)
        q, p = self.get_variables(w)
        return torch.cat((p, -(omega**2) * torch.sin(q)), axis=1)

    def residual(self, w, t, mu, **kwargs):
        return w["w_t"] - self.vector_field(w, t, mu)

    def make_data(self, n_data):
        pass
