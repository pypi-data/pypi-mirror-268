from pathlib import Path

import scimba.nets.mlp as mlp
import torch
from scimba.generativenets import (
    gaussian_mixtures,
    normalizingflows,
    simpleflows,
    trainer_likelihood,
)
from torch import distributions


class TimeGaussian:
    def __init__(self, mu_0, sig2_0):
        self.mu_0 = mu_0
        self.sig2_0 = sig2_0

    def sample(self, t, n):
        comp = distributions.Normal(
            torch.tensor([self.mu_0]), torch.tensor([self.sig2_0 * (1.0 + t)])
        )
        return comp.sample((n,))

    def density(self, x, t):
        comp = distributions.Normal(
            torch.tensor([self.mu_0]), torch.tensor([self.sig2_0 * 2 * (1.0 + t)])
        )
        return torch.exp(comp.log_prob(x))


def test_conditional_normalizingflow():
    data = TimeGaussian(0.5, 0.1)

    nt = 2
    nx = 2
    tab_t = torch.linspace(0.01, 1.0, nt)
    x = data.sample(0.0, nx)
    t_data = torch.zeros(nx)
    for t in tab_t:
        x0 = data.sample(t, nx)
        x = torch.cat([x, x0], axis=0)
        t_loc = torch.ones(nx) * t
        t_data = torch.cat([t_data, t_loc], axis=0)
    t_data = t_data[:, None]

    out_size = 1
    cond_size = 1
    prior = distributions.Normal(torch.tensor([0.5]), torch.tensor([1.0]))
    tlayers = [2, 3]

    flows = [
        simpleflows.AffineConstantFlow(
            net=mlp.GenericMLP,
            dim=out_size,
            dim_conditional=cond_size,
            tlayers=tlayers,
            activation_type="tanh",
        )
        for i in range(2)
    ]
    normalizedflow = normalizingflows.NormalizingFlow(prior, flows)

    file_name = "cond_normalizingflow.pth"
    (
        Path.cwd()
        / Path(trainer_likelihood.TrainerLikelihood.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    Trainer = trainer_likelihood.TrainerLikelihood(
        out_size=1,
        output_data=x,
        conditional=True,
        cond_size=1,
        cond_data=t_data,
        file_name=file_name,
        network=normalizedflow,
        learning_rate=2e-4,
        batch_size=8,
    )

    Trainer.train(epochs=2)

    assert True


def test_conditional_gaussianmixture():
    data = TimeGaussian(0.5, 0.1)

    nt = 2
    nx = 2
    tab_t = torch.linspace(0.01, 1.0, nt)
    x = data.sample(0.0, nx)
    t_data = torch.zeros(nx)
    for t in tab_t:
        x0 = data.sample(t, nx)
        x = torch.cat([x, x0], axis=0)
        t_loc = torch.ones(nx) * t
        t_data = torch.cat([t_data, t_loc], axis=0)
    t_data = t_data[:, None]

    out_size = 1
    cond_size = 1
    mixture = gaussian_mixtures.ConditionalGaussianMixtures(
        net=mlp.GenericMLP, dim=out_size, dim_conditional=cond_size, nb_gaussians=1
    )

    file_name = "cond_gaussianmixture.pth"
    (
        Path.cwd()
        / Path(trainer_likelihood.TrainerLikelihood.FOLDER_FOR_SAVED_NETWORKS)
        / file_name
    ).unlink(missing_ok=True)

    Trainer = trainer_likelihood.TrainerLikelihood(
        out_size=1,
        output_data=x,
        conditional=True,
        cond_size=1,
        cond_data=t_data,
        file_name=file_name,
        network=mixture,
        learning_rate=2e-4,
        batch_size=8,
    )

    Trainer.train(epochs=2)

    assert True


test_conditional_normalizingflow()
test_conditional_gaussianmixture()
