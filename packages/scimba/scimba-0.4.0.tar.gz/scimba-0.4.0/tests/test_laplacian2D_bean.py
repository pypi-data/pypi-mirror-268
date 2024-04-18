from pathlib import Path

import numpy as np
import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.pinn_x as pinn_x
import scimba.pinns.training_x as training_x
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.uniform_sampling as uniform_sampling
import torch
from scimba.equations import domain, pdes
from scimba.shape.eikonal_losses import EikonalLossesData
from scimba.shape.eikonal_x import EikonalPINNx
from scimba.shape.training_x import TrainerEikonal

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"torch loaded; device is {device}")

torch.set_default_dtype(torch.double)
torch.set_default_device(device)

PI = 3.14159265358979323846


# Parametric curve of the Bean shape
class Bean:
    def __init__(self, a=3, b=5):
        self.name = self.__class__.__name__
        self.bord_a, self.bord_b = (-0.5, 1.5)
        self.bord_a2, self.bord_b2 = (-1.5, 0.5)
        self.bound_box = [[self.bord_a, self.bord_b], [self.bord_a2, self.bord_b2]]

        self.a = a
        self.b = b
        self.theta = -PI / 2

    def R(self):
        rot = torch.Tensor(
            [
                [np.cos(self.theta), -np.sin(self.theta)],
                [np.sin(self.theta), np.cos(self.theta)],
            ]
        ).to(device)
        return rot

    def c(self, t):
        arg = 2 * PI * torch.tensor(t)[None, :]
        sin = torch.sin(arg)
        cos = torch.cos(arg)
        x = (sin**self.a + cos**self.b) * cos
        y = (sin**self.a + cos**self.b) * sin
        return self.R() @ torch.cat((x, y), 0)

    def c_prime(self, t):
        arg = 2 * PI * torch.tensor(t)[None, :]
        sin = torch.sin(arg)
        cos = torch.cos(arg)

        x = (
            2 * PI * self.a * sin ** (self.a - 1) * cos
            - 2 * PI * self.b * sin * cos ** (self.b - 1)
        ) * cos - 2 * PI * (sin**self.a + cos**self.b) * sin

        y = (
            2 * PI * self.a * sin ** (self.a - 1) * cos
            - 2 * PI * self.b * sin * cos ** (self.b - 1)
        ) * sin + 2 * PI * (sin**self.a + cos**self.b) * cos

        return self.R() @ torch.cat((x, y), 0)

    def c_prime_rot(self, t, theta=PI / 2):
        rot_mat = torch.Tensor(
            [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
        ).to(device)

        c_prime = self.c_prime(t)  # .detach().numpy()
        return torch.Tensor(rot_mat @ c_prime)


class SDEikonalLap(domain.SignedDistance):
    def __init__(self, threshold: float = 0.0):
        super().__init__(2, threshold)

        # self.bound_box = [[form.bord_a,form.bord_b],[form.bord_a2,form.bord_b2]]

        self.eik_pinns, self.form_trainer = run_shape2D(
            new_training=False,
            tlayers=6 * [64],
            file_name="testlap2Dbean.pth",
            folder="./" if Path.cwd().name == "tests" else "./tests",
        )
        self.pde = self.eik_pinns.pde
        self.mu = torch.tensor([])

    def sdf(self, x):
        """Level set function for the circle domain

        :param X: (x,y) coordinates
        :return: Level set function evaluated at (x,y)
        """
        return self.eik_pinns(x, self.mu)


class Poisson2DSD(pdes.AbstractPDEx):
    def __init__(self, space_domain: domain.SignedDistance):
        super().__init__(
            nb_unknowns=1,
            space_domain=space_domain,
            nb_parameters=0,
            parameter_domain=[],
        )

        self.first_derivative = True
        self.second_derivative = True

    def make_data(self, n_data):
        pass

    def bc_residual(self, w, x, mu, **kwargs):
        u = self.get_variables(w)
        return u

    def residual(self, w, x, mu, **kwargs):
        u_xx = self.get_variables(w, "w_xx")
        u_yy = self.get_variables(w, "w_yy")
        f = 1.0
        return u_xx + u_yy + f

    def post_processing(self, x, mu, w):
        mul = self.space_domain.large_domain.sdf(x)
        return mul * w

    # def get_mul(self,x):
    #     return self.space_domain.sdf(x)

    def reference_solution(self, x, mu):
        print("shape : ", torch.ones_like(x).shape)
        return torch.ones_like(x)


def create_points_from_curve(form, filedir="./", n_bc_points=2000):
    class_name = form.__class__.__name__
    filename = filedir + class_name + "_" + str(n_bc_points) + ".xy"

    # get n_bc_points points on the curve
    t = np.linspace(0, 1, n_bc_points)
    c_t = form.c(t)

    # get the normal vectors
    grad_c_t = form.c_prime_rot(t, theta=-PI / 2).cpu().detach().numpy()
    grad_c_t_norm = np.linalg.norm(grad_c_t, axis=0)
    normals = grad_c_t / grad_c_t_norm

    # check that the normal vectors are well normalized
    assert np.allclose(np.linalg.norm(normals, axis=0), 1)

    # save the points and the normal vectors in filename
    x, y = c_t
    normals = normals.T
    with open(filename, "w") as f:
        for i in range(len(x)):
            f.write(f"{x[i]} {y[i]} {normals[i,0]} {normals[i,1]}\n")
        f.close()

    return filename


# read xy file
def read_xy_file(path):
    f = open(path, "r")
    s = f.readline()
    L = []
    n = []
    while s:
        t = s.split()
        L.append(np.array([float(t[0]), float(t[1])]))
        n.append(np.array([float(t[2]), float(t[3])]))
        s = f.readline()
    f.close()
    return np.array(L), np.array(n)


def run_shape2D(
    new_training=True, tlayers=[2, 3], file_name="testeik.pth", folder="networks/"
):
    n_bc_points = 10

    form = Bean()
    bound = form.bound_box

    if not Path("networks").exists():
        Path("networks").mkdir()

    filename = create_points_from_curve(
        form, filedir="networks/", n_bc_points=n_bc_points
    )

    bc_points, bc_normals = read_xy_file(filename)
    bc_points = torch.tensor(
        bc_points, dtype=torch.double, device=device, requires_grad=True
    )
    bc_normals = torch.tensor(bc_normals, dtype=torch.double, device=device)

    eik = EikonalPINNx(
        net=pinn_x.MLP_x,
        dim=2,
        bound=bound,
        bc_points=bc_points,
        bc_normals=bc_normals,
        layer_sizes=tlayers,
        activation_type="sine",
    )

    if new_training:
        (
            Path.cwd() / Path(TrainerEikonal.FOLDER_FOR_SAVED_NETWORKS) / file_name
        ).unlink(missing_ok=True)

    losses = EikonalLossesData(
        w_eik=100.0,
        w_dir=10000.0,
        w_neu=100.0,
        w_reg=1.0,
        adaptive_weights="annealing",
    )
    optimizers = training_tools.OptimizerData(learning_rate=0.007, decay=0.99)
    trainer = TrainerEikonal(
        eik=eik,
        file_name=file_name,
        losses=losses,
        optimizers=optimizers,
        batch_size=5000,
        FOLDER_FOR_SAVED_NETWORKS=folder,
    )

    if new_training:
        trainer.train(epochs=2, n_collocation=5)

    return eik, trainer


def run_laplacian2D():
    form = Bean()
    sd_function = SDEikonalLap()
    xdomain = domain.SpaceDomain(
        2, domain.SignedDistanceBasedDomain(2, form.bound_box, sd_function)
    )
    pde = Poisson2DSD(xdomain)

    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test_poisson.pth"

    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_x.MLP_x(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_x.PINNx(network, pde)

    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(learning_rate=0.007, decay=0.99)
    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=2, n_collocation=4, n_data=0)

    return pinn, trainer


def test_bean():
    run_shape2D()
    run_laplacian2D()


test_bean()
