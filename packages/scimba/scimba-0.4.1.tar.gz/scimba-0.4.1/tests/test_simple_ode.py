from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
from scimba.equations import ode_basic
from scimba.pinns import pinn_t, training_t
from scimba.sampling import sampling_ode, sampling_parameters, uniform_sampling


def test_simple_ode():
    ode = ode_basic.SimpleOde()
    t_usampler = sampling_ode.TSampler(
        sampler=uniform_sampling.UniformSampling, ode=ode
    )
    mu_usampler = sampling_parameters.MuSampler(
        sampler=uniform_sampling.UniformSampling, model=ode
    )
    sampler = sampling_ode.OdeCartesianSampler(t_usampler, mu_usampler)

    file_name = "simple_ode.pth"
    (
        Path.cwd()
        / Path(training_t.TrainerPINNTime.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    tlayers = [3, 2]
    network = pinn_t.MLP_t(ode=ode, layer_sizes=tlayers, activation_type="sine")
    pinn = pinn_t.PINNt(network, ode)

    losses = pinn_losses.PinnLossesData(init_loss_bool=True, w_res=1.0, w_init=10.0)
    optimizers = training_tools.OptimizerData(
        learning_rate=9e-3, decay=0.992, switch_to_LBFGS=True
    )
    trainer = training_t.TrainerPINNTime(
        ode=ode,
        network=pinn,
        sampler=sampler,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2000,
    )

    trainer.train(epochs=5, n_collocation=20, n_init_collocation=20)
    assert True


test_simple_ode()
