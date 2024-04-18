import torch

try:
    from .sampling_functions import ParametricFunction_t, ParametricFunctionsSampler_t
    from .sampling_ode import TSampler
    from .sampling_parameters import MuSampler
    from .uniform_sampling import UniformSampling

except ImportError:
    from scimba.sampling.sampling_functions import (
        ParametricFunction_t,
        ParametricFunctionsSampler_t,
    )
    from scimba.sampling.sampling_ode import TSampler
    from scimba.sampling.sampling_parameters import MuSampler
    from scimba.sampling.uniform_sampling import UniformSampling


class ode_data:
    def __init__(
        self,
        sampler_t: TSampler,
        sampler_params: MuSampler,
        sampler_initial_condition: UniformSampling,
        source: ParametricFunction_t,
        n_sensor: int,
        resample_sensors: bool = False,
    ):
        # NOTE: sampler_initial_condition must sample w(0) and the derivatives w'(0), etc
        self.sampler_t = sampler_t
        self.sampler_params = sampler_params
        self.sampler_initial_condition = sampler_initial_condition
        self.source = source

        self.resample_sensors = resample_sensors
        self.n_sensor = n_sensor

        if not self.resample_sensors:
            self.t_sensor = self.sampler_t.sampling(self.n_sensor)

        self.coupling_training = False

    def sampling(self, n_collocation: int, n_simu: int):
        # d_t number of time dimensions (d_t = 1)
        # d_w number of unknowns
        # d_mu number of parameters
        # self.source: R -> R^d_f

        batched_dim = n_simu * n_collocation
        t_sensor = torch.empty((batched_dim, 1, self.n_sensor))
        f_sensor = torch.empty((batched_dim, self.source.dim_f, self.n_sensor))
        w_initial = torch.empty((batched_dim, self.sampler_initial_condition.dim))
        params = torch.empty((batched_dim, self.sampler_params.dim))
        t_loss = torch.empty((batched_dim, 1))
        f_loss = torch.empty((batched_dim, self.source.dim_f))

        for i_f in range(n_simu):
            mask = torch.arange(n_collocation) + i_f * n_collocation

            if self.resample_sensors:
                self.t_sensor = self.sampler_t.sampling(self.n_sensor)

            t_loss[mask] = self.sampler_t.sampling(n_collocation)

            self.source_sampler = ParametricFunctionsSampler_t(
                self.source, t_sensor=self.t_sensor, t_loss=t_loss[mask]
            )

            f_sensor_, f_loss_ = self.source_sampler.sampling(1)
            f_loss[mask] = f_loss_[0]

            w_initial_ = self.sampler_initial_condition.sampling(1)
            params_ = self.sampler_params.sampling(1)

            t_sensor[mask] = self.repeat_t_sensor(self.t_sensor, n_collocation)
            f_sensor[mask] = self.repeat_f_sensor(f_sensor_, n_collocation)
            w_initial[mask] = self.repeat_w_params(w_initial_, n_collocation)
            params[mask] = self.repeat_w_params(params_, n_collocation)

        return ode_loss_evaluation(
            t_sensor, f_sensor, w_initial, params, t_loss
        ), f_loss

    @staticmethod
    def repeat_t_sensor(tensor: torch.tensor, n_repeat: int) -> torch.tensor:
        tensor = tensor[:, :, None]  # [n_sensor, some_dim, 1]
        tensor = torch.transpose(tensor, 0, 2)  # [1, some_dim, n_sensor]
        return tensor.repeat(n_repeat, 1, 1)  # [n_repeat, some_dim, n_sensor]

    @staticmethod
    def repeat_f_sensor(tensor: torch.tensor, n_repeat: int) -> torch.tensor:
        tensor = torch.transpose(tensor, 1, 2)  # [1, some_dim, n_sensor]
        return tensor.repeat(n_repeat, 1, 1)  # [n_repeat, some_dim, n_sensor]

    @staticmethod
    def repeat_w_params(tensor: torch.tensor, n_repeat: int) -> torch.tensor:
        return tensor.repeat(n_repeat, 1)  # [n_repeat, some_dim, n_sensor]


class ode_loss_evaluation:
    def __init__(
        self,
        t_sensor: torch.tensor,
        f_sensor: torch.tensor,
        w_initial: torch.tensor,
        params: torch.tensor,
        t_loss: torch.tensor,
    ):
        self.t_sensor = t_sensor
        self.f_sensor = f_sensor
        self.w_initial = w_initial
        self.params = params
        self.t_loss = t_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return ode_loss_evaluation(
            self.t_sensor[indices],
            self.f_sensor[indices],
            self.w_initial[indices],
            self.params[indices],
            self.t_loss[indices],
        )


class ode_physical_loss_evaluation:
    def __init__(
        self,
        ode_loss: ode_loss_evaluation,
        f_loss: torch.tensor,
    ):
        self.ode_loss = ode_loss
        self.f_loss = f_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return ode_physical_loss_evaluation(
            self.ode_loss[indices],
            self.f_loss[indices],
        )


class ode_data_loss_evaluation:
    def __init__(
        self,
        ode_loss: ode_loss_evaluation,
        w_loss: torch.tensor,
    ):
        self.ode_loss = ode_loss
        self.w_loss = w_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return ode_data_loss_evaluation(
            self.ode_loss[indices],
            self.w_loss[indices],
        )


"""
time only:
[
    ### DATA FOR SIMULATION ###
    t_sensor: n_sensor
    mu: n_mu
    f(t_sensor): d_f x n_sensor
    u_0: d_u

    ### DATA FOR LOSS EVALUATION ###
    [
        t: 1
        f(t): d_f x 1
    ] * n_t (n_t loss evaluations per simulation) * n_simu (number of simulations)
]
"""


if __name__ == "__main__":
    import scimba.equations.pdes as pdes
    import scimba.sampling.sampling_functions as sampling_functions
    import scimba.sampling.sampling_ode as sampling_ode
    import scimba.sampling.sampling_parameters as sampling_parameters
    import scimba.sampling.uniform_sampling as uniform_sampling

    class SimpleOde(pdes.AbstractODE):
        r"""
        .. math::

            \frac{u}{dt} + \mu u = 0

        """

        def __init__(self):
            super().__init__(
                nb_unknowns=1,
                time_domain=[0.0, 10.0],
                nb_parameters=2,
                parameter_domain=[[0.5, 1], [-1, -0.5]],
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

    ode = SimpleOde()
    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=ode)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    w_ini_sampler = uniform_sampling.UniformSampling(ode.nb_unknowns, [[0.0, 1.0]])

    class my_function(sampling_functions.ParametricFunction_t):
        def __init__(self, f_dim=3, p_dim=1, p_domain=[[0.0, 1.0]]):
            super().__init__(f_dim, p_dim, p_domain)

        def __call__(self, t: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
            mu = self.get_parameters(params)
            return torch.cat((t * mu, t, mu), dim=1)

    ode_data_sampler = ode_data(
        sampler_t=t_sampler,
        sampler_params=mu_sampler,
        sampler_initial_condition=w_ini_sampler,
        source=my_function(),
        n_sensor=10,
        resample_sensors=False,
    )

    sample, f_loss = ode_data_sampler.sampling(n_collocation=4, n_simu=2)
