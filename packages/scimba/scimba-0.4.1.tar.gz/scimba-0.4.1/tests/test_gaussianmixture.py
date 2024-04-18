from pathlib import Path

import numpy as np
import scimba.generativenets as gn
import torch
from sklearn import datasets


class DatasetMoons:
    """two half-moons"""

    def sample(self, n):
        moons = datasets.make_moons(n_samples=n, noise=0.05)[0].astype(np.float32)
        return torch.tensor(moons)


def test_normalizingflow():
    data = DatasetMoons()
    x = data.sample(32)

    out_size = 2
    mixture = gn.gaussian_mixtures.GaussianMixtures(dim=out_size, nb_gaussians=10)

    file_name = "test.pth"
    (
        Path.cwd()
        / Path(gn.trainer_likelihood.TrainerLikelihood.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    Trainer = gn.trainer_likelihood.TrainerLikelihood(
        out_size=2,
        output_data=x,
        file_name=file_name,
        network=mixture,
        learning_rate=7e-3,
        batch_size=8,
    )
    Trainer.train(epochs=5)
    z = mixture.sample(num_samples=512)
    assert True


test_normalizingflow()
