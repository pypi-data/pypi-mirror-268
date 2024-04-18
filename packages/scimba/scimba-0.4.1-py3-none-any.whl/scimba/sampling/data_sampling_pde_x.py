import torch

try:
    from ..equations.domain import SpaceTensor
    from .sampling_functions import ParametricFunction_x, ParametricFunctionsSampler_x
    from .sampling_parameters import MuSampler
    from .sampling_pde import XSampler

except ImportError:
    from scimba.equations.domain import SpaceTensor
    from scimba.sampling.sampling_functions import (
        ParametricFunction_x,
        ParametricFunctionsSampler_x,
    )
    from scimba.sampling.sampling_parameters import MuSampler
    from scimba.sampling.sampling_pde import XSampler


class pde_x_data:
    def __init__(
        self,
        sampler_x: XSampler,
        sampler_params: MuSampler,
        source: ParametricFunction_x,
        boundary: ParametricFunction_x,
        n_sensor: int,
        n_sensor_bc: int,
        resample_sensors: bool = False,
    ):
        self.sampler_x = sampler_x
        self.sampler_params = sampler_params
        self.source = source
        self.boundary = boundary

        self.resample_sensors = resample_sensors
        self.n_sensor = n_sensor
        self.n_sensor_bc = n_sensor_bc

        if not self.resample_sensors:
            self.x_sensor = self.sampler_x.sampling(self.n_sensor)
            self.x_sensor_bc = self.sampler_x.bc_sampling(self.n_sensor_bc)

        self.coupling_training = False
        self.dim_x = sampler_x.dim

    def sampling(self, n_collocation: int, n_simu: int):
        # create tensors for inner points
        batched_dim = n_simu * n_collocation
        x_sensor = SpaceTensor(
            torch.empty((batched_dim, self.dim_x, self.n_sensor)),
            torch.empty((batched_dim, self.n_sensor), dtype=int),
        )
        f_sensor = torch.empty((batched_dim, self.source.dim_f, self.n_sensor))
        x_loss = SpaceTensor(
            torch.empty((batched_dim, self.dim_x)),
            torch.empty(batched_dim, dtype=int),
        )
        f_loss = torch.empty((batched_dim, self.source.dim_f))

        # create tensors for boundary points
        x_sensor_bc = SpaceTensor(
            torch.empty((batched_dim, self.dim_x, self.n_sensor_bc)),
            torch.empty((batched_dim, self.n_sensor_bc), dtype=int),
        )
        f_sensor_bc = torch.empty((batched_dim, self.boundary.dim_f, self.n_sensor_bc))
        x_loss_bc = SpaceTensor(
            torch.empty((batched_dim, self.dim_x)),
            torch.empty(batched_dim, dtype=int),
        )
        f_loss_bc = torch.empty((batched_dim, self.boundary.dim_f))

        # create parameters tensors (to be repeated)
        params = torch.empty((batched_dim, self.sampler_params.dim))
        params_bc = torch.empty((batched_dim, self.sampler_params.dim))

        # fill tensors

        for i_f in range(n_simu):
            mask = torch.arange(n_collocation) + i_f * n_collocation

            if self.resample_sensors:
                self.x_sensor = self.sampler_x.sampling(self.n_sensor)
                self.x_sensor_bc = self.sampler_x.bc_sampling(self.n_sensor)

            x_loss[mask] = self.sampler_x.sampling(n_collocation)
            x_loss_bc[mask] = self.sampler_x.bc_sampling(n_collocation)

            self.source_sampler = ParametricFunctionsSampler_x(
                self.source, x_sensor=self.x_sensor, x_loss=x_loss[mask]
            )

            f_sensor_, f_loss_ = self.source_sampler.sampling(1)
            f_loss[mask] = f_loss_[0]

            self.boundary_sampler = ParametricFunctionsSampler_x(
                self.boundary, x_sensor=self.x_sensor_bc, x_loss=x_loss_bc[mask]
            )

            f_sensor_bc_, f_loss_bc_ = self.boundary_sampler.sampling(1)
            f_loss_bc[mask] = f_loss_bc_[0]

            params_ = self.sampler_params.sampling(1)

            x_sensor[mask] = self.repeat_x_sensor(self.x_sensor, n_collocation)
            f_sensor[mask] = self.repeat_f_sensor(f_sensor_, n_collocation)
            params[mask] = self.repeat_params(params_, n_collocation)

            x_sensor_bc[mask] = self.repeat_x_sensor(self.x_sensor_bc, n_collocation)
            f_sensor_bc[mask] = self.repeat_f_sensor(f_sensor_bc_, n_collocation)
            params_bc[mask] = self.repeat_params(params_, n_collocation)

        return (
            pde_loss_evaluation(x_sensor, f_sensor, params, x_loss),
            f_loss,
            pde_loss_evaluation_bc(x_sensor_bc, f_sensor_bc, params_bc, x_loss_bc),
            f_loss_bc,
        )

    @staticmethod
    def repeat_x_sensor(data: SpaceTensor, n_repeat: int) -> SpaceTensor:
        x = data.x[:, :, None]  # [n_sensor, some_dim, 1]
        x = torch.transpose(x, 0, 2)  # [1, some_dim, n_sensor]
        x = x.repeat(n_repeat, 1, 1)  # [n_repeat, some_dim, n_sensor]
        labels = data.labels[:, None]  # [n_sensor, 1]
        labels = torch.transpose(labels, 0, 1)  # [1, n_sensor]
        labels = labels.repeat(n_repeat, 1, 1).squeeze()  # [n_repeat, n_sensor]
        return SpaceTensor(x, labels)

    @staticmethod
    def repeat_f_sensor(tensor: torch.Tensor, n_repeat: int) -> torch.Tensor:
        tensor = torch.transpose(tensor, 1, 2)  # [1, some_dim, n_sensor]
        return tensor.repeat(n_repeat, 1, 1)  # [n_repeat, some_dim, n_sensor]

    @staticmethod
    def repeat_params(tensor: torch.Tensor, n_repeat: int) -> torch.Tensor:
        return tensor.repeat(n_repeat, 1)  # [n_repeat, some_dim, n_sensor]


class pde_loss_evaluation:
    def __init__(
        self,
        x_sensor: torch.Tensor,
        f_sensor: torch.Tensor,
        params: torch.Tensor,
        x_loss: torch.Tensor,
    ):
        self.x_sensor = x_sensor
        self.f_sensor = f_sensor
        self.params = params
        self.x_loss = x_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_loss_evaluation(
            self.x_sensor[indices],
            self.f_sensor[indices],
            self.params[indices],
            self.x_loss[indices],
        )

    def __str__(self) -> str:
        string = "shapes:\n"
        string += f"x_sensor: {self.x_sensor.shape}\n"
        string += f"f_sensor: {self.f_sensor.shape}\n"
        string += f"params: {self.params.shape}\n"
        string += f"x_loss: {self.x_loss.shape}\n"
        string += f"params: \n{self.params}\n"
        string += f"x_loss: \n{self.x_loss}\n"
        return string

    def __repr__(self) -> str:
        return str(self)


class pde_loss_evaluation_bc:
    def __init__(
        self,
        x_sensor_bc: torch.Tensor,
        f_sensor_bc: torch.Tensor,
        params_bc: torch.Tensor,
        x_loss_bc: torch.Tensor,
    ):
        self.x_sensor_bc = x_sensor_bc
        self.f_sensor_bc = f_sensor_bc
        self.params_bc = params_bc
        self.x_loss_bc = x_loss_bc

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_loss_evaluation_bc(
            self.x_sensor_bc[indices],
            self.f_sensor_bc[indices],
            self.params_bc[indices],
            self.x_loss_bc[indices],
        )

    def __str__(self) -> str:
        string = "shapes:\n"
        string += f"x_sensor_bc: {self.x_sensor_bc.shape}\n"
        string += f"f_sensor_bc: {self.f_sensor_bc.shape}\n"
        string += f"params_bc: {self.params_bc.shape}\n"
        string += f"x_loss_bc: {self.x_loss_bc.shape}\n"
        string += f"params_bc: \n{self.params_bc}\n"
        string += f"x_loss_bc: \n{self.x_loss_bc}\n"
        return string

    def __repr__(self) -> str:
        return str(self)


class pde_physical_loss_evaluation:
    def __init__(
        self,
        pde_loss: pde_loss_evaluation,
        f_loss: torch.Tensor,
    ):
        self.pde_loss = pde_loss
        self.f_loss = f_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_physical_loss_evaluation(
            self.pde_loss[indices],
            self.f_loss[indices],
        )


class pde_physical_loss_evaluation_bc:
    def __init__(
        self,
        pde_loss_bc: pde_loss_evaluation_bc,
        f_loss_bc: torch.Tensor,
    ):
        self.pde_loss_bc = pde_loss_bc
        self.f_loss_bc = f_loss_bc

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_physical_loss_evaluation_bc(
            self.pde_loss_bc[indices],
            self.f_loss_bc[indices],
        )


class pde_data_loss_evaluation:
    def __init__(
        self,
        pde_loss: pde_loss_evaluation,
        w_loss: torch.Tensor,
    ):
        self.pde_loss = pde_loss
        self.w_loss = w_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_data_loss_evaluation(
            self.pde_loss[indices],
            self.w_loss[indices],
        )


class pde_data_loss_evaluation_bc:
    def __init__(
        self,
        pde_loss_bc: pde_loss_evaluation_bc,
        w_loss_bc: torch.Tensor,
    ):
        self.pde_loss_bc = pde_loss_bc
        self.w_loss_bc = w_loss_bc

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_data_loss_evaluation_bc(
            self.pde_loss_bc[indices],
            self.w_loss_bc[indices],
        )


"""
space only:
[
    ### DATA FOR SIMULATION ###
    x_sensor: n_sensor
    x_sensor_bc: n_sensor_bc
    mu: n_mu
    f(x_sensor): d_f x n_sensor
    g(x_sensor_bc): d_g x n_sensor_bc

    ### DATA FOR INNER LOSS EVALUATION ###
    [
        x: 1
        f(x): d_f x 1
    ] * n_x (n_x loss evaluations per simulation) * n_simu (number of simulations)

    ### DATA FOR BOUNDARY LOSS EVALUATION ###
    [
        x_bc: 1
        g(x_bc): d_g x 1
    ] * n_bc (n_bc loss evaluations per simulation) * n_simu (number of simulations)
]
"""


if __name__ == "__main__":
    import scimba.equations.domain as domain
    import scimba.equations.pdes as pdes
    import scimba.sampling.sampling_functions as sampling_functions
    import scimba.sampling.sampling_parameters as sampling_parameters
    import scimba.sampling.sampling_pde as sampling_pde
    import scimba.sampling.uniform_sampling as uniform_sampling

    class Poisson2D(pdes.AbstractPDEx):
        r"""

        .. math::

            \frac{d^2u}{dx^2} + \frac{d^2u}{dy^2} + f = 0

        """

        def __init__(self):
            x_domain = domain.SpaceDomain(
                2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]])
            )
            super().__init__(
                nb_unknowns=1,
                space_domain=x_domain,
                nb_parameters=0,
                parameter_domain=[[0.0, 1.0]],
            )

            self.first_derivative = True
            self.second_derivative = True

        def bc_residual(self, w, x, mu, **kwargs):
            return self.get_variables(w)

        def residual(self, w, x, mu, **kwargs):
            x1, x2 = x.get_coordinates()
            # alpha = self.get_parameters(mu)
            u_xx = self.get_variables(w, "w_xx")
            u_yy = self.get_variables(w, "w_yy")
            sin_x1 = torch.sin(2 * torch.pi * x1)
            sin_x2 = torch.sin(2 * torch.pi * x2)
            # f = 8 * torch.pi**2 * alpha * sin_x1 * sin_x2
            f = 8 * torch.pi**2 * sin_x1 * sin_x2
            return u_xx + u_yy + f

        def reference_solution(self, x, mu):
            x1, x2 = x.get_coordinates()
            # alpha = self.get_parameters(mu)
            # return alpha * torch.sin(2 * torch.pi * x1) * torch.sin(2 * torch.pi * x2)
            return torch.sin(2 * torch.pi * x1) * torch.sin(2 * torch.pi * x2)

    pde = Poisson2D()
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    class my_function(sampling_functions.ParametricFunction_x):
        def __init__(self, dim_f=3, dim_x=2, dim_p=1, p_domain=[[0.0, 1.0]]):
            super().__init__(dim_f, dim_x, dim_p, p_domain)

        def __call__(self, x: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
            x1, x2 = x.get_coordinates()
            mu = self.get_parameters(params)
            return torch.cat((x1 * mu, x2, mu), dim=1)

    pde_data_sampler = pde_x_data(
        sampler_x=x_sampler,
        sampler_params=mu_sampler,
        source=my_function(),
        boundary=my_function(),
        n_sensor=9,
        n_sensor_bc=3,
        resample_sensors=False,
    )

    sample, f_loss, sample_bc, f_loss_bc = pde_data_sampler.sampling(
        n_collocation=5, n_simu=2
    )
