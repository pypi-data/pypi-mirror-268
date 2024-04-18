from pathlib import Path

import numpy as np
import torch
from scimba.generativenets import normalizingflows, simpleflows, trainer_likelihood
from scimba.nets import mlp
from sklearn import datasets
from torch.distributions import MultivariateNormal


class DatasetMoons:
    """two half-moons"""

    def sample(self, n):
        moons = datasets.make_moons(n_samples=n, noise=0.05)[0].astype(np.float32)
        return torch.tensor(moons)


def test_normalizingflow():
    data = DatasetMoons()
    x = data.sample(2)

    out_size = 2
    cond_size = 0
    prior = MultivariateNormal(torch.zeros(out_size), torch.eye(out_size))

    tlayers = [2, 3]
    flows = [
        simpleflows.RealNVPFlow(
            net=mlp.GenericMLP,
            dim=out_size,
            dim_conditional=cond_size,
            parity=i % 2,
            tlayers=tlayers,
        )
        for i in range(2)
    ]
    normalizedflow = normalizingflows.NormalizingFlow(prior, flows)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(trainer_likelihood.TrainerLikelihood.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    Trainer = trainer_likelihood.TrainerLikelihood(
        out_size=2,
        output_data=x,
        file_name=file_name,
        network=normalizedflow,
        learning_rate=7e-3,
        batch_size=2,
    )
    Trainer.train(epochs=2)
    normalizedflow.sample(x=torch.zeros(512, 0), num_samples=512)
    z0 = normalizedflow.sample_prior(num_samples=512)
    assert True


test_normalizingflow()
