import copy
from pathlib import Path

import torch
from torch import nn

from .. import device
from . import mlp


class MassLoss(nn.modules.loss._Loss):
    """A loss based whoch implement

    $$
        sum_i^H (inputs - target)
    $$

    Encode a general MLP architecture
    ---
    Imposed inputs parameters
    - size_average (int): input of the mother class _loss
    - reduce: input of the mother class _loss
    - reduced (str): choose sum or average
    """

    __constants__ = ["reduction"]

    def __init__(self, size_average=None, reduce=None, reduction: str = "mean") -> None:
        super().__init__(size_average, reduce, reduction)

    def forward(self, input: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        if self.reduction == "mean":
            return torch.mean(input - target)
        else:
            return torch.sum(input - target)


class Trainer:
    """
        This class construct a trainer to solve a classical supervised problem`

        :param in_size: dimension of the inputs x
        :type out_size: int
        :param in_data: the sample of the inputs data
        :type in_data: torch.Tensor
        :param out_size: dimension of the outputs data y
        :type out_size: int
        :param output_data: the sample of the inputs data y
        :type output_data: torch.Tensor
        :param batch_size: the number of data in each batch
        :type batch_size: int
        :param network: the network used
        :type network: nn.Module
        :param file_name: the name of the file to save the network
        :type file_name: str 
        :param learning_rate: value of the learning rate
        :type learning_rate: float 
        :param decay: value of the decay for the learning rate
        :type decay: float 
    """

    DEFAULT_DECAY = 0.99
    DEFAULT_FILE_NAME = "network.pth"
    DEFAULT_LEARNING_RATE = 1e-3
    FOLDER_FOR_SAVED_NETWORKS = "networks"
    DEFAULT_BATCH_SIZE = 128

    def __init__(
        self,
        in_size: int,
        input_data: torch.Tensor,
        out_size: int,
        output_data: torch.Tensor,
        **kwargs,
    ):
        self.in_size = in_size
        self.input_data = input_data
        self.out_size = out_size
        self.output_data = output_data
        self.batch_size = kwargs.get("batch_size", self.DEFAULT_BATCH_SIZE)

        self.network = kwargs.get(
            "network",
            mlp.GenericMLP(
                in_size=self.input_data.shape[1], out_size=self.output_data.shape[1]
            ),
        )

        folder_for_saved_networks = Path.cwd() / Path(self.FOLDER_FOR_SAVED_NETWORKS)
        folder_for_saved_networks.mkdir(parents=True, exist_ok=True)

        file_name = kwargs.get("file_name", self.DEFAULT_FILE_NAME)
        self.file_name = folder_for_saved_networks / file_name

        self.learning_rate = kwargs.get("learning_rate", self.DEFAULT_LEARNING_RATE)
        self.decay = kwargs.get("decay", self.DEFAULT_DECAY)

        self.create_network()
        self.load(self.file_name)


    def __call__(self, input: torch.Tensor):
        """
            Call the network
        """
        return self.net(input)

    def create_network(self):
        """
            function import the network to the device and create the optimizer
        """
        self.net = self.network.to(device)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=self.learning_rate)
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.optimizer, step_size=20, gamma=self.decay
        )

    def load(self, file_name: str):
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

        except FileNotFoundError:
            self.to_be_trained = True
            print("network was not loaded from file: training needed")

    @staticmethod
    def save(
        file_name: str,
        epoch: int,
        net_state: dict,
        optimizer_state: dict,
        scheduler_state: dict,
        loss: float,
        loss_history: list,
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

        mse_cost_function = torch.nn.MSELoss()

        try:
            best_loss_value = self.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        epoch = 0

        for epoch in range(epochs):
            permutation = torch.randperm(self.input_data.size()[0])

            for i in range(0, self.input_data.size()[0], self.batch_size):
                indices = permutation[i : i + self.batch_size]

                batch_x, batch_y = self.input_data[indices], self.output_data[indices]
                self.optimizer.zero_grad()

                prediction = self(batch_x)
                self.loss = mse_cost_function(prediction, batch_y)

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
