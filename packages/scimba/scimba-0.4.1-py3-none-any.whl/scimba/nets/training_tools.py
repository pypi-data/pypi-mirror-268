import copy

import torch


class OptimizerData:
    """
    Class to store and create the Optimizer parameters

    :param learning_rate: value of the learning rate
    :type learning_rate: float
    :param decay: value of the decay for the learning rate
    :type decay: float
    :param step_size: number of gradient step between two decay
    :type step_size: int

    """

    def __init__(self, **kwargs):
        self.learning_rate = kwargs.get("learning_rate", 1e-3)
        self.decay = kwargs.get("decay", 0.99)
        self.step_size = kwargs.get("step_size", 20)

        self.switch_to_LBFGS = kwargs.get("switch_to_LBFGS", False)
        self.LBFGS_history_size = kwargs.get("LBFGS_history_size", 15)
        self.LBFGS_max_iter = kwargs.get("LBFGS_max_iter", 5)
        self.LBFGS_switch_ratio = kwargs.get("LBFGS_switch_ratio", 500)
        self.LBFGS_switch_plateau = kwargs.get(
            "LBFGS_switch_plateau", [50, 10]
        )  # check for a plateau after 50 iterations, on the last 10 iterations

    def create_second_opt(self, parameters: list[torch.nn.Parameter]):
        """
        create the second optimizer using the parameters of the network.
        This second optimize can replace the first one during the training

        :params parameters: the parameters of the network
        :type parameters: list[Parameter]
        """
        self.second_opt = torch.optim.LBFGS(
            parameters,
            history_size=self.LBFGS_history_size,
            max_iter=self.LBFGS_max_iter,
            line_search_fn="strong_wolfe",
        )
        self.second_opt_activated = True

    def create_first_opt(self, parameters: list[torch.nn.Parameter]):
        """
        create the main optimizer using the parameters of the network.

        :params parameters: the parameters of the network
        :type parameters: list[Parameter]
        """
        self.first_opt = torch.optim.Adam(parameters, lr=self.learning_rate)
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.first_opt, step_size=self.step_size, gamma=self.decay
        )
        self.second_opt = None
        self.second_opt_activated = False

    def load(self, parameters: list[torch.nn.Parameter], checkpoint: str):
        """
        Load the network and optimizers from a file.

        :params parameters: the parameters of the network
        :type parameters: list[Parameter]
        :params checkpoint: the file containing the saved data
        :type checkpoint: str
        """

        try:
            self.first_opt.load_state_dict(checkpoint["first_optimizer_state_dict"])
            self.scheduler.load_state_dict(checkpoint["scheduler_state_dict"])

            if checkpoint["second_optimizer_state_dict"] is not None:
                self.create_second_opt(parameters)
                self.second_opt.load_state_dict(
                    checkpoint["second_optimizer_state_dict"]
                )
            print("jsbdbshd")
        except FileNotFoundError:
            print("optimizer was not loaded from file: training needed")

    def test_activation_second_opt(
        self,
        parameters: list[torch.nn.Parameter],
        loss_history: list,
        loss_value: torch.Tensor,
        init_loss: torch.Tensor,
    ):
        """
        Decide to activate or the not the second optimize and
        if yes create the second optimizer

        :params parameters: the parameters of the network
        :type parameters: list[Parameter]
        :params loss_history: the list of the loss value
        :type loss_history: list
        :params loss_value: the current value of the loss
        :type loss_value: torch.Tensor
        :params init_loss: the initial value of the loss
        :type init_loss: torch.Tensor
        """
        LBFGS_activated = self.second_opt_activated
        n1, n2 = self.LBFGS_switch_plateau
        if self.switch_to_LBFGS and not LBFGS_activated and len(loss_history) > n1:
            if LBFGS_activated := (
                (loss_value < init_loss / self.LBFGS_switch_ratio)
                and (sum(loss_history[-n2:-1]) - sum(loss_history[-n1 : -n1 + n2]) > 0)
            ):
                self.create_second_opt(parameters)

    def update_best_opt(self):
        """
        Update the best optimizer value
        """
        self.best_first_optimizer = copy.deepcopy(self.first_opt.state_dict())
        self.best_scheduler = copy.deepcopy(self.scheduler.state_dict())

        if self.second_opt_activated:
            self.best_second_optimizer = copy.deepcopy(self.second_opt.state_dict())
        else:
            self.best_second_optimizer = None

    def dict_for_save(self) -> dict:
        """
        Save the network and optimizers to a file.

        :return: the dictionary of best optimizer values for save
        :rtype: dict
        """
        return {
            "first_optimizer_state_dict": self.best_first_optimizer,
            "scheduler_state_dict": self.best_scheduler,
            "second_optimizer_state_dict": self.best_second_optimizer,
        }

    def get_first_opt_gradients(self) -> torch.Tensor:
        """
        Get the gradients of the network parameters
        """
        grads = torch.tensor([])
        for p in self.first_opt.param_groups[0]["params"]:
            if p.grad is not None:
                grads = torch.cat((grads, p.grad.flatten()[:, None]), 0)
        return grads
