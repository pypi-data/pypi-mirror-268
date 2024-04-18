import copy
from pathlib import Path

import torch
from torch.distributions import MultivariateNormal

from .. import device, nets
from . import normalizingflows, simpleflows


class TrainerLikelihood:
    """
        This class construct a trainer to optimize likehihood
        associated to a targer distribution :math:`p(y)` or :math:`p(y\mid x)`

        :param out_size: dimension of the distribution data y
        :type out_size: int
        :param output_data: the sample of the target distribution  y
        :type output_data: torch.Tensor
        :param batch_size: the number of data in each batch
        :type batch_size: int
        :param conditional: if there is or not conditional data
        :type conditiona: boolean
        :param cond_size: dimension of the conditional data x
        :type cond_size: int
        :param cond_data: the sample of the conditiona distribution x
        :type cond_data: torch.Tensor

    """
    DEFAULT_DECAY = 0.99
    DEFAULT_FILE_NAME = "normalizingflow.pth"
    DEFAULT_LEARNING_RATE = 1e-3
    FOLDER_FOR_SAVED_NETWORKS = "networks"
    DEFAULT_BATCH_SIZE = 128

    def __init__(self, out_size, output_data, **kwargs):
        self.out_size = out_size
        self.output_data = output_data.to(device)
        self.batch_size = kwargs.get("batch_size", self.DEFAULT_BATCH_SIZE)
        self.conditional = kwargs.get("conditional", False)
        self.cond_size = kwargs.get("cond_size", 0)
        self.cond_data = kwargs.get("cond_data", torch.zeros(0, 0))

        prior = MultivariateNormal(torch.zeros(out_size), torch.eye(out_size))
        flows = [
            simpleflows.AffineConstantFlow(
                net=nets.mlp.GenericMLP, dim=out_size, dim_conditional=self.cond_size
            )
            for _ in range(4)
        ]
        normalizingflow = normalizingflows.NormalizingFlow(prior, flows)
        self.network = kwargs.get("network", normalizingflow)

        folder_for_saved_networks = Path.cwd() / Path(self.FOLDER_FOR_SAVED_NETWORKS)
        folder_for_saved_networks.mkdir(parents=True, exist_ok=True)

        file_name = kwargs.get("file_name", self.DEFAULT_FILE_NAME)
        self.file_name = folder_for_saved_networks / file_name

        self.learning_rate = kwargs.get("learning_rate", self.DEFAULT_LEARNING_RATE)
        self.decay = kwargs.get("decay", self.DEFAULT_DECAY)

        self.create_network()
        self.load(self.file_name)

        self.to_be_trained = kwargs.get("to_be_trained", self.to_be_trained)

    def create_network(self):
        """
            function import the network to the device and create the optimizer
        """
        self.net = self.network.to(device)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=self.learning_rate)
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.optimizer, step_size=20, gamma=self.decay
        )

    def load(self, file_name):
        """
            function which load a network and training data (loss history etc)

            :param file_name: the name of the file with the data
            :type file_name: str
        """
        self.loss_history = []

        try:
            try:
                checkpoint = torch.load(file_name)
            except RuntimeError:
                checkpoint = torch.load(file_name, map_location=torch.device("cpu"))

            self.net.load_state_dict(checkpoint["model_state_dict"])
            self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            self.scheduler.load_state_dict(checkpoint["scheduler_state_dict"])
            self.loss = checkpoint["loss"]

            try:
                self.loss_history = checkpoint["loss_history"]
            except KeyError:
                pass

            self.to_be_trained = False
            # print("network loaded successfully")

        except FileNotFoundError:
            self.to_be_trained = True
            print("network was not loaded from file: training needed")

    @staticmethod
    def save(
        file_name:str,
        epoch:int,
        net_state: dict,
        optimizer_state:dict,
        scheduler_state:dict,
        loss:float,
        loss_history:list,
    ):
        """
            function which save a network and training data (loss history etc)

            :param file_name: the name of the file where the data are saved
            :type file_name: str
            :param epoch: the current epoch
            :type epoch: int
            :param net_state: the current network
            :type net_state: dict 
            :param optimizer_state: the current state of the optimizer
            :type optimizer_state: dict
            :param scheduler_state: the current sate of scheduler
            :type scheduler_state: dict
            :param loss: the current value of the loss
            :type loss: float
            :param loss_history: all the loss values
            :type loss_history: list
        """
        torch.save(
            {
                epoch: epoch,
                "model_state_dict": net_state,
                "optimizer_state_dict": optimizer_state,
                "scheduler_state_dict": scheduler_state,
                "loss": loss,
                "loss_history": loss_history,
            },
            file_name,
        )

    def train(self, **kwargs):
        """
            Function to train the model

            :param epochs: the number of epoch
            :type: int
        """
        epochs = kwargs.get("epochs", 500)

        try:
            best_loss_value = self.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        epoch = 0

        for epoch in range(epochs):
            permutation = torch.randperm(self.output_data.size()[0])

            for i in range(0, self.output_data.size()[0], self.batch_size):
                self.optimizer.zero_grad()
                indices = permutation[i : i + self.batch_size].to(device)

                if self.conditional:
                    batch_x, batch_y = (
                        self.cond_data[indices],
                        self.output_data[indices],
                    )
                else:
                    batch_y = self.output_data[indices]
                    batch_x = torch.zeros((self.batch_size, 0))

                self.loss = self.net(batch_y, batch_x)

                self.loss.backward(retain_graph=True)
                self.optimizer.step()
                self.scheduler.step()

                self.loss_history.append(self.loss.item())

            if epoch % 50 == 0:
                print(f"epoch {epoch: 5d}: current loss = {self.loss.item():5.2e}")

            if self.loss.item() < best_loss_value:
                print(f"epoch {epoch: 5d}: best loss = {self.loss.item():5.2e}")
                best_loss = self.loss.clone()
                best_loss_value = best_loss.item()
                best_net = copy.deepcopy(self.net.state_dict())
                best_optimizer = copy.deepcopy(self.optimizer.state_dict())
                best_scheduler = copy.deepcopy(self.scheduler.state_dict())

        print(f"epoch {epoch: 5d}: current loss = {self.loss.item():5.2e}")

        try:
            self.save(
                self.file_name,
                epoch,
                best_net,
                best_optimizer,
                best_scheduler,
                best_loss,
                self.loss_history,
            )
            print("load best network")
            self.load(self.file_name)
        except UnboundLocalError:
            pass
