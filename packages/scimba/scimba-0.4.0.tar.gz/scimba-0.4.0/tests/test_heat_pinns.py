from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
from scimba.equations import domain, pde_1d_heat
from scimba.pinns import pinn_tx, training_tx
from scimba.sampling import (
    sampling_ode,
    sampling_parameters,
    sampling_pde,
    uniform_sampling,
)


def test_heat_equation():
    space_domain = domain.SpaceDomain(1, domain.SquareDomain(1, [[0.0, 2.0]]))

    pde = pde_1d_heat.HeatEquation(tdomain=[0.0, 0.03], xdomain=space_domain)

    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=pde)

    x_sampler = sampling_pde.XSampler(pde=pde)

    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )

    sampler = sampling_pde.PdeTXCartesianSampler(t_sampler, x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_tx.TrainerPINNSpaceTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [2, 3]

    network = pinn_tx.MLP_tx(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_tx.PINNtx(network, pde)

    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(learning_rate=9e-3, decay=0.99)
    trainer = training_tx.TrainerPINNSpaceTime(
        pde=pde,
        network=pinn,
        losses=losses,
        optimizers=optimizers,
        sampler=sampler,
        file_name=file_name,
        batch_size=400,
    )
    trainer.train(epochs=10, n_collocation=10, n_bc_collocation=0, n_data=0)

    assert True


def test_heat_equation_uniform_sampling():
    space_domain = domain.SpaceDomain(1, domain.SquareDomain(1, [[0.0, 2.0]]))
    pde = pde_1d_heat.HeatEquation(tdomain=[0.0, 0.03], xdomain=space_domain)
    t_sampler = sampling_ode.TSampler(sampler=uniform_sampling.UniformSampling, ode=pde)
    x_sampler = sampling_pde.XSampler(pde=pde)
    mu_sampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=pde
    )
    sampler = sampling_pde.PdeTXCartesianSampler(t_sampler, x_sampler, mu_sampler)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(training_tx.TrainerPINNSpaceTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [10, 5]
    network = pinn_tx.DisMLP_tx(pde=pde, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_tx.PINNtx(network, pde)

    losses = pinn_losses.PinnLossesData(
        bc_loss_bool=True, init_loss_bool=True, w_res=0.02, w_bc=1.0, w_init=1.0
    )
    optimizers = training_tools.OptimizerData(learning_rate=9e-3, decay=0.99)
    trainer = training_tx.TrainerPINNSpaceTime(
        pde=pde,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=3000,
    )

    trainer.train(
        epochs=10,
        n_collocation=10,
        n_bc_collocation=10,
        n_init_collocation=10,
        n_data=0,
    )

    assert True


test_heat_equation()
test_heat_equation_uniform_sampling()
