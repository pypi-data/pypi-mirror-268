import torch

try:
    from ..equations.domain import SpaceTensor
    from .sampling_functions import (
        ParametricFunction_tx,
        ParametricFunction_x,
        ParametricFunctionsSampler_tx,
        ParametricFunctionsSampler_x,
    )
    from .sampling_ode import TSampler
    from .sampling_parameters import MuSampler
    from .sampling_pde import XSampler

except ImportError:
    from scimba.equations.domain import SpaceTensor
    from scimba.sampling.sampling_functions import (
        ParametricFunction_tx,
        ParametricFunction_x,
        ParametricFunctionsSampler_tx,
        ParametricFunctionsSampler_x,
    )
    from scimba.sampling.sampling_ode import TSampler
    from scimba.sampling.sampling_parameters import MuSampler
    from scimba.sampling.sampling_pde import XSampler


class pde_tx_data:
    def __init__(
        self,
        sampler_t: TSampler,
        sampler_x: XSampler,
        sampler_params: MuSampler,
        source: ParametricFunction_tx,
        initial: ParametricFunction_x,
        boundary: ParametricFunction_x,
        n_sensor: int,
        n_sensor_bc: int,
        n_sensor_ini: int,
        resample_sensors: bool = False,
    ):
        self.sampler_t = sampler_t
        self.sampler_x = sampler_x
        self.sampler_params = sampler_params
        self.source = source
        self.initial = initial
        self.boundary = boundary

        self.resample_sensors = resample_sensors
        self.n_sensor = n_sensor
        self.n_sensor_bc = n_sensor_bc
        self.n_sensor_ini = n_sensor_ini

        if not self.resample_sensors:
            self.t_sensor = self.sampler_t.sampling(self.n_sensor)
            self.x_sensor = self.sampler_x.sampling(self.n_sensor)
            self.t_sensor_bc = self.sampler_t.sampling(self.n_sensor_bc)
            self.x_sensor_bc = self.sampler_x.bc_sampling(self.n_sensor_bc)
            self.t_sensor_ini = torch.zeros((self.n_sensor_ini, 1))
            self.x_sensor_ini = self.sampler_x.sampling(self.n_sensor_ini)

        self.coupling_training = False
        self.dim_x = sampler_x.dim

    def sampling(self, n_collocation: int, n_simu: int):
        batched_dim = n_simu * n_collocation

        # create tensors for inner points
        t_sensor = torch.empty((batched_dim, 1, self.n_sensor))
        x_sensor = SpaceTensor(
            torch.empty((batched_dim, self.dim_x, self.n_sensor)),
            torch.empty((batched_dim, self.n_sensor), dtype=int),
        )
        f_sensor = torch.empty((batched_dim, self.source.dim_f, self.n_sensor))
        t_loss = torch.empty((batched_dim, 1))
        x_loss = SpaceTensor(
            torch.empty((batched_dim, self.dim_x)),
            torch.empty(batched_dim, dtype=int),
        )
        f_loss = torch.empty((batched_dim, self.source.dim_f))

        # create tensors for boundary points
        t_sensor_bc = torch.empty((batched_dim, 1, self.n_sensor_bc))
        x_sensor_bc = SpaceTensor(
            torch.empty((batched_dim, self.dim_x, self.n_sensor_bc)),
            torch.empty((batched_dim, self.n_sensor_bc), dtype=int),
        )
        f_sensor_bc = torch.empty((batched_dim, self.boundary.dim_f, self.n_sensor_bc))
        t_loss_bc = torch.empty((batched_dim, 1))
        x_loss_bc = SpaceTensor(
            torch.empty((batched_dim, self.dim_x)),
            torch.empty(batched_dim, dtype=int),
        )
        f_loss_bc = torch.empty((batched_dim, self.boundary.dim_f))

        # create tensors for initial points
        t_sensor_ini = torch.empty((batched_dim, 1, self.n_sensor_ini))
        x_sensor_ini = SpaceTensor(
            torch.empty((batched_dim, self.dim_x, self.n_sensor_ini)),
            torch.empty((batched_dim, self.n_sensor_ini), dtype=int),
        )
        f_sensor_ini = torch.empty((batched_dim, self.initial.dim_f, self.n_sensor_ini))
        t_loss_ini = torch.empty((batched_dim, 1))
        x_loss_ini = SpaceTensor(
            torch.empty((batched_dim, self.dim_x)),
            torch.empty(batched_dim, dtype=int),
        )
        f_loss_ini = torch.empty((batched_dim, self.initial.dim_f))

        # create parameters tensors (to be repeated)
        params = torch.empty((batched_dim, self.sampler_params.dim))
        params_bc = torch.empty((batched_dim, self.sampler_params.dim))
        params_ini = torch.empty((batched_dim, self.sampler_params.dim))

        # fill tensors

        for i_f in range(n_simu):
            mask = torch.arange(n_collocation) + i_f * n_collocation

            if self.resample_sensors:
                self.t_sensor = self.sampler_t.sampling(self.n_sensor)
                self.x_sensor = self.sampler_x.sampling(self.n_sensor)
                self.t_sensor_bc = self.sampler_t.sampling(self.n_sensor_bc)
                self.x_sensor_bc = self.sampler_x.bc_sampling(self.n_sensor_bc)
                self.t_sensor_ini = self.t_sensor_ini = torch.zeros(
                    (self.n_sensor_ini, 1)
                )
                self.x_sensor_ini = self.sampler_x.sampling(self.n_sensor_ini)

            t_loss[mask] = self.sampler_t.sampling(n_collocation)
            x_loss[mask] = self.sampler_x.sampling(n_collocation)
            t_loss_bc[mask] = self.sampler_t.sampling(n_collocation)
            x_loss_bc[mask] = self.sampler_x.bc_sampling(n_collocation)
            t_loss_ini[mask] = torch.zeros((n_collocation, 1))
            x_loss_ini[mask] = self.sampler_x.sampling(n_collocation)

            self.source_sampler = ParametricFunctionsSampler_tx(
                self.source,
                t_sensor=self.t_sensor,
                t_loss=t_loss[mask],
                x_sensor=self.x_sensor,
                x_loss=x_loss[mask],
            )

            f_sensor_, f_loss_ = self.source_sampler.sampling(1)
            f_loss[mask] = f_loss_[0]

            self.boundary_sampler = ParametricFunctionsSampler_x(
                self.boundary,
                t_sensor=self.t_sensor_bc,
                t_loss=t_loss_bc[mask],
                x_sensor=self.x_sensor_bc,
                x_loss=x_loss_bc[mask],
            )

            f_sensor_bc_, f_loss_bc_ = self.boundary_sampler.sampling(1)
            f_loss_bc[mask] = f_loss_bc_[0]

            self.initial_sampler = ParametricFunctionsSampler_x(
                self.initial,
                t_sensor=self.t_sensor_ini,
                t_loss=t_loss_ini[mask],
                x_sensor=self.x_sensor_ini,
                x_loss=x_loss_ini[mask],
            )

            f_sensor_ini_, f_loss_ini_ = self.initial_sampler.sampling(1)
            f_loss_ini[mask] = f_loss_ini_[0]

            params_ = self.sampler_params.sampling(1)

            t_sensor[mask] = self.repeat_t_sensor(self.t_sensor, n_collocation)
            x_sensor[mask] = self.repeat_x_sensor(self.x_sensor, n_collocation)
            f_sensor[mask] = self.repeat_f_sensor(f_sensor_, n_collocation)
            params[mask] = self.repeat_params(params_, n_collocation)

            t_sensor_bc[mask] = self.repeat_t_sensor(self.t_sensor_bc, n_collocation)
            x_sensor_bc[mask] = self.repeat_x_sensor(self.x_sensor_bc, n_collocation)
            f_sensor_bc[mask] = self.repeat_f_sensor(f_sensor_bc_, n_collocation)
            params_bc[mask] = self.repeat_params(params_, n_collocation)

            t_sensor_ini[mask] = self.repeat_t_sensor(self.t_sensor_ini, n_collocation)
            x_sensor_ini[mask] = self.repeat_x_sensor(self.x_sensor_ini, n_collocation)
            f_sensor_ini[mask] = self.repeat_f_sensor(f_sensor_ini_, n_collocation)
            params_ini[mask] = self.repeat_params(params_, n_collocation)

        loss_pde = pde_loss_evaluation(
            t_sensor, x_sensor, f_sensor, params, t_loss, x_loss
        )
        loss_bc = pde_loss_evaluation_bc(
            t_sensor_bc, x_sensor_bc, f_sensor_bc, params_bc, t_loss_bc, x_loss_bc
        )
        loss_ini = pde_loss_evaluation_ini(
            t_sensor_ini, x_sensor_ini, f_sensor_ini, params_ini, t_loss_ini, x_loss_ini
        )

        return loss_pde, f_loss, loss_bc, f_loss_bc, loss_ini, f_loss_ini

    @staticmethod
    def repeat_t_sensor(tensor: torch.Tensor, n_repeat: int) -> torch.Tensor:
        tensor = tensor[:, :, None]  # [n_sensor, some_dim, 1]
        tensor = torch.transpose(tensor, 0, 2)  # [1, some_dim, n_sensor]
        return tensor.repeat(n_repeat, 1, 1)  # [n_repeat, some_dim, n_sensor]

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
        t_sensor: torch.Tensor,
        x_sensor: torch.Tensor,
        f_sensor: torch.Tensor,
        params: torch.Tensor,
        t_loss: torch.Tensor,
        x_loss: torch.Tensor,
    ):
        self.t_sensor = t_sensor
        self.x_sensor = x_sensor
        self.f_sensor = f_sensor
        self.params = params
        self.t_loss = t_loss
        self.x_loss = x_loss

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_loss_evaluation(
            self.t_sensor[indices],
            self.x_sensor[indices],
            self.f_sensor[indices],
            self.params[indices],
            self.x_loss[indices],
        )

    def __str__(self) -> str:
        string = "shapes:\n"
        string += f"t_sensor: {self.t_sensor.shape}\n"
        string += f"x_sensor: {self.x_sensor.shape}\n"
        string += f"f_sensor: {self.f_sensor.shape}\n"
        string += f"params: {self.params.shape}\n"
        string += f"t_loss: {self.t_loss.shape}\n"
        string += f"x_loss: {self.x_loss.shape}\n"
        string += f"params: \n{self.params}\n"
        string += f"t_loss: \n{self.t_loss}\n"
        string += f"x_loss: \n{self.x_loss}\n"
        return string

    def __repr__(self) -> str:
        return str(self)


class pde_loss_evaluation_bc:
    def __init__(
        self,
        t_sensor_bc: torch.Tensor,
        x_sensor_bc: torch.Tensor,
        f_sensor_bc: torch.Tensor,
        params_bc: torch.Tensor,
        t_loss_bc: torch.Tensor,
        x_loss_bc: torch.Tensor,
    ):
        self.t_sensor_bc = t_sensor_bc
        self.x_sensor_bc = x_sensor_bc
        self.f_sensor_bc = f_sensor_bc
        self.params_bc = params_bc
        self.t_loss_bc = t_loss_bc
        self.x_loss_bc = x_loss_bc

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_loss_evaluation_bc(
            self.t_sensor_bc[indices],
            self.x_sensor_bc[indices],
            self.f_sensor_bc[indices],
            self.params_bc[indices],
            self.t_loss_bc[indices],
            self.x_loss_bc[indices],
        )

    def __str__(self) -> str:
        string = "shapes:\n"
        string += f"t_sensor_bc: {self.t_sensor_bc.shape}\n"
        string += f"x_sensor_bc: {self.x_sensor_bc.shape}\n"
        string += f"f_sensor_bc: {self.f_sensor_bc.shape}\n"
        string += f"params_bc: {self.params_bc.shape}\n"
        string += f"t_loss_bc: {self.t_loss_bc.shape}\n"
        string += f"x_loss_bc: {self.x_loss_bc.shape}\n"
        string += f"params_bc: \n{self.params_bc}\n"
        string += f"t_loss_bc: \n{self.t_loss_bc}\n"
        string += f"x_loss_bc: \n{self.x_loss_bc}\n"
        return string

    def __repr__(self) -> str:
        return str(self)


class pde_loss_evaluation_ini:
    def __init__(
        self,
        t_sensor_ini: torch.Tensor,
        x_sensor_ini: torch.Tensor,
        f_sensor_ini: torch.Tensor,
        params_ini: torch.Tensor,
        t_loss_ini: torch.Tensor,
        x_loss_ini: torch.Tensor,
    ):
        self.t_sensor_ini = t_sensor_ini
        self.x_sensor_ini = x_sensor_ini
        self.f_sensor_ini = f_sensor_ini
        self.params_ini = params_ini
        self.t_loss_ini = t_loss_ini
        self.x_loss_ini = x_loss_ini

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_loss_evaluation_ini(
            self.t_sensor_ini[indices],
            self.x_sensor_ini[indices],
            self.f_sensor_ini[indices],
            self.params_ini[indices],
            self.t_loss_ini[indices],
            self.x_loss_ini[indices],
        )

    def __str__(self) -> str:
        string = "shapes:\n"
        string += f"t_sensor_ini: {self.t_sensor_ini.shape}\n"
        string += f"x_sensor_ini: {self.x_sensor_ini.shape}\n"
        string += f"f_sensor_ini: {self.f_sensor_ini.shape}\n"
        string += f"params_ini: {self.params_ini.shape}\n"
        string += f"t_loss_ini: {self.t_loss_ini.shape}\n"
        string += f"x_loss_ini: {self.x_loss_ini.shape}\n"
        string += f"params_ini: \n{self.params_ini}\n"
        string += f"t_loss_ini: \n{self.t_loss_ini}\n"
        string += f"x_loss_ini: \n{self.x_loss_ini}\n"
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


class pde_physical_loss_evaluation_ini:
    def __init__(
        self,
        pde_loss_ini: pde_loss_evaluation_ini,
        f_loss_ini: torch.Tensor,
    ):
        self.pde_loss_ini = pde_loss_ini
        self.f_loss_ini = f_loss_ini

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_physical_loss_evaluation_ini(
            self.pde_loss_ini[indices],
            self.f_loss_ini[indices],
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


class pde_data_loss_evaluation_ini:
    def __init__(
        self,
        pde_loss_ini: pde_loss_evaluation_ini,
        w_loss_ini: torch.Tensor,
    ):
        self.pde_loss_ini = pde_loss_ini
        self.w_loss_ini = w_loss_ini

    def __getitem__(self, indices: torch.Tensor):
        assert isinstance(indices, torch.Tensor), "indices must be a tensor"
        return pde_data_loss_evaluation_ini(
            self.pde_loss_ini[indices],
            self.w_loss_ini[indices],
        )


"""
space-time:
[
    ### DATA FOR SIMULATION ###
    xt_sensor: n_sensor
    x_BC_sensor: n_BC_sensor
    x_ini_sensor: n_ini_sensor
    mu: n_mu
    f(xt_sensor): d_f x n_sensor
    g(x_BC_sensor): d_g x n_BC_sensor
    u0(x_ini_sensor): d_u x n_ini_sensor

    ### DATA FOR INNER LOSS EVALUATION ###
    [
        xt: 1
        f(xt): d_f x 1
    ] * n_xt (n_xt loss evaluations per simulation) * n_simu (number of simulations)

    ### DATA FOR INITIAL LOSS EVALUATION ###
    [
        x_ini: 1
        u0(x_ini): d_u x 1
    ] * n_ini (n_ini loss evaluations per simulation) * n_simu (number of simulations)

    ### DATA FOR BOUNDARY LOSS EVALUATION ###
    [
        x_BC: 1
        g(x_BC): d_g x 1
    ] * n_BC (n_BC loss evaluations per simulation) * n_simu (number of simulations)
]
"""


if __name__ == "__main__":
    import scimba.equations.domain as domain
    import scimba.equations.pdes as pdes
    import scimba.sampling.sampling_functions as sampling_functions
    import scimba.sampling.sampling_parameters as sampling_parameters
    import scimba.sampling.uniform_sampling as uniform_sampling
    from scimba.sampling import sampling_ode, sampling_pde

    class PDE_tx(pdes.AbstractPDEtx):
        def __init__(self):
            x_domain = domain.SpaceDomain(
                2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]])
            )
            super().__init__(
                nb_unknowns=1,
                time_domain=[0.0, 1.0],
                space_domain=x_domain,
                nb_parameters=1,
                parameter_domain=[[0.4, 0.7]],
            )

        def residual(self, w, t, x, mu, **kwargs):
            pass

        def bc_residual(self, w, t, x, mu, **kwargs):
            pass

        def initial_condition(self, x, mu, **kwargs):
            pass

        def make_data(self, n_data):
            pass

        def reference_solution(self, t, x, mu):
            pass

    pde = PDE_tx()
    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=pde)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    class Source(sampling_functions.ParametricFunction_tx):
        def __init__(self, dim_f=4, dim_x=2, dim_p=1, p_domain=[[0.0, 1.0]]):
            super().__init__(dim_f, dim_x, dim_p, p_domain)

        def __call__(
            self, t: torch.Tensor, x: torch.Tensor, params: torch.Tensor
        ) -> torch.Tensor:
            x1, x2 = x.get_coordinates()
            mu = self.get_parameters(params)
            return torch.cat((t, x1, x2, mu), dim=1)

    class Boundary(sampling_functions.ParametricFunction_x):
        def __init__(self, dim_f=3, dim_x=2, dim_p=1, p_domain=[[0.0, 1.0]]):
            super().__init__(dim_f, dim_x, dim_p, p_domain)

        def __call__(self, x: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
            x1, x2 = x.get_coordinates()
            mu = self.get_parameters(params)
            return torch.cat((x1, x2, mu), dim=1)

    class Initial(sampling_functions.ParametricFunction_x):
        def __init__(self, dim_f=2, dim_x=2, dim_p=1, p_domain=[[0.0, 1.0]]):
            super().__init__(dim_f, dim_x, dim_p, p_domain)

        def __call__(self, x: torch.Tensor, params: torch.Tensor) -> torch.Tensor:
            x1, x2 = x.get_coordinates()
            mu = self.get_parameters(params)
            return torch.cat((x1, x2 * mu), dim=1)

    pde_data_sampler = pde_tx_data(
        sampler_t=t_sampler,
        sampler_x=x_sampler,
        sampler_params=mu_sampler,
        source=Source(),
        boundary=Boundary(),
        initial=Initial(),
        n_sensor=9,
        n_sensor_bc=3,
        n_sensor_ini=4,
        resample_sensors=False,
    )

    loss_pde, f_loss, loss_bc, f_loss_bc, loss_ini, f_loss_ini = (
        pde_data_sampler.sampling(n_collocation=5, n_simu=2)
    )
