import torch
from torch.utils.data import Dataset


class DataGenerate(Dataset):
    """
    A very simple dataset class for simulating ODEs
    """

    def __init__(self, true_model, T, num_time_batch=10, num_timestep_per_batch=10):
        """

        :param true_model: analytical solution or any other ground truth models
        :param T: total simulation time
        :param num_time_batch: number of time batches
        :param num_timestep_per_batch: number of timestep per batches
        """
        self.T = T
        self.tbatch = num_time_batch
        self.ts = []  ### [segment time][times]
        self.values = []  ### data.values [segment time][time, init_data,var]
        self.true_model = true_model
        self.nb_data_by_time_seg = num_timestep_per_batch

    def __len__(self):
        return len(self.ts)

    def create_dataset(self, num_samples):
        """

        :param num_samples: number of samples (e.g. trajectories in SIR)
        :return:
        """
        batch_length = self.T / self.tbatch
        x0 = self.true_model.generate_initial_conditions(num_samples)
        mu = self.true_model.generate_parameters(num_samples)

        time = torch.linspace(
            start=0, end=0.1, steps=self.nb_data_by_time_seg, requires_grad=False
        )
        self.true_model.time_scheme(x0, time, mu)

        self.mu = torch.empty(self.tbatch, *mu.shape)
        self.ts = torch.empty(self.tbatch, *time.shape)
        self.values = torch.empty(self.tbatch, *self.true_model.solution.shape)
        for i in range(self.tbatch):
            time = torch.linspace(
                start=i * batch_length,
                end=(i + 1) * batch_length,
                steps=self.nb_data_by_time_seg,
                requires_grad=False,
            )
            self.true_model.time_scheme(x0, time, mu)

            # take the solution of the last timestep of batch i as the initial conditions for the first timestep of batch i+1
            x0 = self.true_model.solution[-1, :, :]

            # time.requires_grad_(False)
            # sol =sol.detach()

            self.tmu = mu
            self.ts[i] = time
            self.values[i] = self.true_model.solution

    def print_data(self):
        time = torch.cat(self.ts, dim=0)  # concatenate all time steps
        data = torch.cat(self.values, dim=0)
        self.true_model.plot_data(time.detach().cpu(), data.detach().cpu())
