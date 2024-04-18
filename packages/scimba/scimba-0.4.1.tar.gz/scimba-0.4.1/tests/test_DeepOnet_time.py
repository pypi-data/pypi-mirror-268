from pathlib import Path

import torch
from scimba.equations.pdes import AbstractODE
from scimba.neural_operators import deeponet_t
from scimba.pinns import pinn_t
from scimba.pinos import pino_t, training_t
from scimba.sampling import (
    data_sampling_ode,
    sampling_functions,
    sampling_ode,
    sampling_parameters,
    uniform_sampling,
)

"""
    Using DeepONet to solve the equation below:

        \frac{du}{dt} + \mu_1 u = f, u(0)=1

    where f = exp(-\mu_2 t)
"""


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
            parameter_domain=[[0.9999, 1]],
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
        f = kwargs.get("f", None)
        return u_t + alpha * u - f

    def post_processing(self, t, mu, w):
        return self.initial_condition(mu) + t * w

    def reference_solution(self, t, mu):
        return None


def inner_test_DeepOnet_t(encoder_type: str, decoder_type: str):
    ode = SimpleOdeWithSource()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    w_initial_usampler = uniform_sampling.UniformSampling(1, [[1.0, 1.000001]])

    class myFunc(sampling_functions.ParametricFunction_t):
        def __init__(self):
            super().__init__(dim_f=1, dim_p=1, p_domain=[[0.0, 1.0]])

        def __call__(self, t, params):
            return torch.exp(-self.get_parameters(params) * t)

    ode_sampler = data_sampling_ode.ode_data(
        sampler_t=t_usampler,
        sampler_params=mu_usampler,
        sampler_initial_condition=w_initial_usampler,
        source=myFunc(),
        n_sensor=2,
    )

    no_network = deeponet_t.DeepONetTime(
        net=pinn_t.MLP_t,
        ode=ode,
        ode_sampler=ode_sampler,
        lat_size=1,
        layers_b=[3, 2],
        layers_t=[2, 3],
        decoder_type=decoder_type,
        encoder_type=encoder_type,
    )

    network = pino_t.PINOt(no_network, ode)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINOTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    trainer = training_t.TrainerPINOTime(
        network=network,
        ode=ode,
        sampler=ode_sampler,
        batch_size=1000,
        learning_rate=2e-3,
        decay=0.99,
        file_name=file_name,
    )

    trainer.train(epochs=2, n_simu=2, n_collocation_t=3)


def test_DeepOnet_t():
    for encoder_type in ["PointNet", "MLP"]:
        for decoder_type in ["linear", "nonlinear"]:
            inner_test_DeepOnet_t(encoder_type, decoder_type)
