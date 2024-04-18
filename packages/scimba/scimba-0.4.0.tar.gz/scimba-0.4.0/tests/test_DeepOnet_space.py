from pathlib import Path

import scimba.equations.domain as domain
import scimba.equations.pdes as pdes
import scimba.sampling.data_sampling_pde_x as data_sampling_pde_x
import scimba.sampling.sampling_functions as sampling_functions
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch
from scimba.nets.training_tools import OptimizerData
from scimba.neural_operators import deeponet_x
from scimba.pinns import pinn_x
from scimba.pinns.pinn_losses import PinnLossesData
from scimba.pinos import pino_x, training_x

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"torch loaded; device is {device}")

torch.set_default_dtype(torch.double)
torch.set_default_device(device)

PI = 3.14159265358979323846


class Poisson_2D(pdes.AbstractPDEx):
    def __init__(self, space_domain):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=0,
            parameter_domain=[],
        )

        self.first_derivative = True
        self.second_derivative = True

    def bc_residual(self, w, x, mu, **kwargs):
        return self.get_variables(w)

    def residual(self, w, x, mu, **kwargs):
        x1, x2 = x.get_coordinates()
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = kwargs.get("f", None)
        return u_xx + u_yy + f

    def post_processing(self, x, mu, w):
        x1, x2 = x.get_coordinates()
        return x1 * (1 - x1) * (1 - x2) * x2 * w


def inner_test_DeepOnet_x(encoder_type: str, decoder_type: str, dim_f_bc: int):
    xdomain = domain.SpaceDomain(2, domain.SquareDomain(2, [[0.0, 1.0], [0.0, 1.0]]))
    pde = Poisson_2D(xdomain)
    x_sampler = sampling_pde.XSampler(pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    class source(sampling_functions.ParametricFunction_x):
        def __init__(self):
            super().__init__(
                dim_f=1, dim_x=2, dim_p=3, p_domain=[[0.1, 0.2], [0.2, 0.7], [0.2, 0.7]]
            )

        def __call__(self, x, params):
            x1, x2 = x.get_coordinates()
            a, b, c = self.get_parameters(params)
            f = 8.0 * PI**2 * torch.sin(2 * PI * x1) * torch.sin(2 * PI * x2)
            g = (((x1 - b) / 0.05) ** 2 + ((x2 - c) / 0.05) ** 2) * torch.exp(
                -(((x1 - b) + (x2 - c)) ** 2) / 0.05
            )
            return f - a * g

    class boundary(sampling_functions.ParametricFunction_x):
        def __init__(self, dim_f_bc):
            super().__init__(dim_f=dim_f_bc, dim_x=2, dim_p=0, p_domain=[])

        def __call__(self, x, params):
            x1, x2 = x.get_coordinates()
            return (0 * x1) * dim_f_bc

    pde_sampler = data_sampling_pde_x.pde_x_data(
        sampler_x=x_sampler,
        sampler_params=mu_sampler,
        source=source(),
        boundary=boundary(dim_f_bc),
        n_sensor=2,
        n_sensor_bc=5,
    )

    no_network = deeponet_x.DeepONetSpace(
        net=pinn_x.MLP_x,
        pde=pde,
        pde_sampler=pde_sampler,
        lat_size=1,
        layers_b=[3, 2],
        layers_t=[2, 3],
        activation_type="sine",
        encoder_type=encoder_type,
        decoder_type=decoder_type,
    )

    network = pino_x.PINOx(no_network, pde)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINOSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    losses = PinnLossesData(w_res=1.0)
    optimizers = OptimizerData(learning_rate=1e-2, decay=0.992)
    trainer = training_x.TrainerPINOSpace(
        network=network,
        pde=pde,
        sampler=pde_sampler,
        batch_size=1000,
        losses=losses,
        optimizers=optimizers,
        bc_loss_bool=False,
        file_name=file_name,
    )

    trainer.train(epochs=2, n_simu=2, n_collocation_x=3)


class reference(sampling_functions.ParametricFunction_x):
    def __init__(self):
        super().__init__(
            dim_f=1, dim_x=2, dim_p=3, p_domain=[[0.1, 0.2], [0.2, 0.7], [0.2, 0.7]]
        )

    def __call__(self, x, params):
        x1, x2 = x.get_coordinates()
        a, b, c = self.get_parameters(params)
        f = torch.sin(2.0 * PI * x1) * torch.sin(2.0 * PI * x2)
        g = torch.exp(-(((x1 - b) + (x2 - c)) ** 2.0) / 0.05)
        return f - a * g


def test_DeepOnet_x():
    for encoder_type in ["PointNet", "MLP"]:
        for decoder_type in ["linear", "nonlinear"]:
            for dim_f_bc in [0, 1, 2]:
                print(f"encoder_type: {encoder_type}")
                print(f"decoder_type: {decoder_type}")
                print(f"dim_f_bc: {dim_f_bc}")
                inner_test_DeepOnet_x(encoder_type, decoder_type, dim_f_bc)


test_DeepOnet_x()
