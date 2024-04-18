from pathlib import Path

import scimba.nets.training_tools as training_tools
import scimba.pinns.pinn_losses as pinn_losses
from scimba.equations import pde_1x1v_transport
from scimba.pinns import pinn_txv
from scimba.pinns.training_txv import TrainerPinnKinetic


def test_kinetic_constant_transport():
    pde = pde_1x1v_transport.ConstantInX()

    network = pinn_txv.MLP_txv(pde=pde, layer_sizes=[20, 20])
    pinn = pinn_txv.PINNtxv(network, pde)

    file_name = "testkinetic.pth"
    (
        Path.cwd() / Path(TrainerPinnKinetic.FOLDER_FOR_SAVED_NETWORKS) / file_name
    ).unlink(missing_ok=True)

    losses = pinn_losses.PinnLossesData(w_res=1.0)
    optimizers = training_tools.OptimizerData(learning_rate=1e-2, decay=0.99)
    trainer = TrainerPinnKinetic(
        pde=pde,
        network=pinn,
        losses=losses,
        optimizers=optimizers,
        file_name=file_name,
        batch_size=2500,
    )

    trainer.train(
        # epochs=input_conf["NN"]["epochs"],
        # n_collocation=input_conf["NN"]["n_collocation"],
        # n_data=input_conf["NN"]["n_data"],
        epochs=10,
        n_collocation=5,
        n_data=0,
    )

    assert True


test_kinetic_constant_transport()
