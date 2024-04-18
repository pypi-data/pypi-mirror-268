from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
import scimba.pinns.training_xv as training_xv
import scimba.sampling.sampling_parameters as sampling_parameters
import scimba.sampling.sampling_pde as sampling_pde
import scimba.sampling.sampling_pde_txv as sampling_pde_tvx
import scimba.sampling.uniform_sampling as uniform_sampling
from scimba.equations import domain, pde_1d_laplacian_xv
from scimba.pinns import pinn_xv

PI = 3.14159265358979323846


def test_poisson_xv1D():
    xdomain = domain.SpaceDomain(1, domain.SquareDomain(1, [[0.0, 1.0]]))
    vdomain = domain.SquareDomain(1, [[0.0, 1.0]])
    pde = pde_1d_laplacian_xv.Lap1D_xv(xdomain, vdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    v_sampler = sampling_pde_tvx.VSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde_tvx.PdeXVCartesianSampler(x_sampler, v_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_xv.TrainerPINNSpaceVel.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]
    network = pinn_xv.MLP_xv(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_xv.PINNxv(network, pde)

    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(
        learning_rate=5.2e-2, decay=0.99, switch_to_LBFGS=True
    )
    trainer = training_xv.TrainerPINNSpaceVel(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=6000,
    )

    trainer.train(epochs=10, n_collocation=10)


test_poisson_xv1D()
