from pathlib import Path

from scimba.equations import domain, pde_1d_laplacian
from scimba.pinns import pinn_x, training_x
from scimba.sampling import sampling_parameters, sampling_pde, uniform_sampling


def test_laplacian_1d():
    xdomain = domain.SpaceDomain(1, domain.SquareDomain(1, [[0.0, 1.0]]))
    pde = pde_1d_laplacian.LaplacianSine(k=1, domain=xdomain)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeXCartesianSampler(x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_x.TrainerPINNSpace.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    network = pinn_x.RBFNet_x(pde=pde, nb_gaussian=2)
    pinn = pinn_x.PINNx(network, pde)

    trainer = training_x.TrainerPINNSpace(
        pde=pde,
        network=pinn,
        sampler=sampler,
        file_name=file_name,
        bc_loss_bool=False,
        learning_rate=1e-2,
        decay=0.99,
        batch_size=10,
        w_data=0,
        w_res=1,
        w_bc=0,
    )

    trainer.train(epochs=4, n_collocation=5, n_init_collocation=5, n_data=5)

    assert True


test_laplacian_1d()
