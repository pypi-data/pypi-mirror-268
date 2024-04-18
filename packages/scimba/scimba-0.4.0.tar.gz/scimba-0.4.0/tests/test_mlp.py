from pathlib import Path

import scimba.nets.mlp as mlp
import scimba.nets.training as training
import scimba.sampling.uniform_sampling as uniform_sampling
import torch

PI = 3.1415926535897932384


def g(x):
    x1 = x[:, 0]
    x2 = x[:, 1]
    return torch.sin(x1) * torch.sin(x2)


def train_ac(ac_type):
    sampler = uniform_sampling.UniformSampling(2, [[-2.0, 2.0], [-2.0, 2.0]])
    x = sampler.sampling(2)
    y = g(x)
    y = y[:, None]

    file_name = "test_mlp.pth"

    (Path.cwd() / Path(training.Trainer.FOLDER_FOR_SAVED_NETWORKS) / file_name).unlink(
        missing_ok=True
    )

    tlayers = [2, 4, 2]
    network = mlp.GenericMLP(2, 1, layer_sizes=tlayers, activation_type=ac_type)

    trainer = training.Trainer(
        in_size=2,
        input_data=x,
        out_size=1,
        output_data=y,
        network=network,
        file_name=file_name,
        learning_rate=1.2e-2,
        decay=0.99,
        batch_size=200,
    )

    trainer.train(epochs=3)


def test_act():
    train_ac("tanh")
    train_ac("adaptative_tanh")
    train_ac("sine")
    train_ac("cosin")
    train_ac("silu")
    train_ac("sigmoid")


test_act()
