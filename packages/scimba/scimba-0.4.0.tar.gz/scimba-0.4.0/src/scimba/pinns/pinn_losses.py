import torch

from ..nets.training_tools import OptimizerData


class PinnLossesData:
    DEFAULT_W_DATA = 0.0
    DEFAULT_W_RES = 1.0
    DEFAULT_W_INIT = 1.0
    DEFAULT_W_BC = 1.0
    DEFAULT_W_CONSTRAINTS = 1.0
    """
        Class to create optimize and store the Losses of PINNs

        :param init_loss_bool: activate or not intial condition loss
        :type init_loss_bool: bool
        :param bc_loss_bool: activate or not bc condition loss
        :type bc_loss_bool: bool
        :param data_loss_bool: activate or not data loss
        :type data_loss_bool: bool
        :param constrtains_loss_bool: activate or not loww on weights constraints
        :type constraints_loss_bool: bool

        :param residual_f_loss: the loss used to compute the residue (exemple MSE)
        :type residual_loss_bool: torch.nn._Loss
        :param init_f_loss: the loss used to compute the initiation condition (exemple MSE)
        :type init_loss_bool: torch.nn._Loss
        :param bc_f_loss: the loss used to compute BC condition (exemple MSE)
        :type bc_loss_bool: torch.nn._Loss
        :param data_f_loss: the loss used to compute the data error (exemple MSE)
        :type data_loss_bool: torch.nn._Loss
        :param constraints_f_loss: the loss used to compute the constraints (exemple MSE)
        :type constraints_loss_bool: torch.nn._Loss

        :param w_res: weights for the residual loss
        :type w_res: float
        :param w_init: weights for the init loss
        :type w_init: float
        :param w_bc: weights for the bc loss
        :type w_bc: float
        :param w_data: weights for the data loss
        :type w_data: float
        :param w_constraints: weights for the constraints loss
        :type w_constraints: float

        :param adaptive_weights: whether to adapt the weights
        :type adaptive_weights: Union[str, None]
        :param epochs_adapt: epoch between two adaptation
        :type epochs_adapt: int
    """

    def __init__(self, **kwargs):
        self.init_loss_bool = kwargs.get("init_loss_bool", False)
        self.bc_loss_bool = kwargs.get("bc_loss_bool", False)
        self.data_loss_bool = kwargs.get("data_loss_bool", False)
        self.constraints_loss_bool = kwargs.get("constraints_loss_bool", False)

        self.residual_f_loss = kwargs.get("residual_f_loss", torch.nn.MSELoss())
        self.init_f_loss = kwargs.get("init_f_loss", torch.nn.MSELoss())
        self.bc_f_loss = kwargs.get("bc_f_loss", torch.nn.MSELoss())
        self.data_f_loss = kwargs.get("data_f_loss", torch.nn.MSELoss())
        self.constraints_f_loss = kwargs.get("constraints_f_loss", None)

        self.adaptive_weights = kwargs.get("adaptive_weights", None)
        self.epochs_adapt = kwargs.get("epochs_adapt", 20)
        self.w_res = kwargs.get("w_res", self.DEFAULT_W_RES)
        self.w_data = kwargs.get("w_data", self.DEFAULT_W_DATA * self.data_loss_bool)
        self.w_init = kwargs.get("w_init", self.DEFAULT_W_INIT * self.init_loss_bool)
        self.w_bc = kwargs.get("w_bc", self.DEFAULT_W_BC * self.bc_loss_bool)
        self.w_constraints = kwargs.get(
            "w_constraints", self.DEFAULT_W_CONSTRAINTS * self.constraints_loss_bool
        )

        self.alpha_lr_annealing = kwargs.get("alpha_lr_annealing", 0.9)
        self.epochs_adapt = kwargs.get("epochs_adapt",10)
        if self.adaptive_weights is not None:
            self.w_res_history = [self.w_res]
            self.w_data_history = [self.w_data]
            self.w_init_history = [self.w_init]
            self.w_bc_history = [self.w_bc]
            self.w_constraints_history = [self.w_constraints]

        self.loss_history = []
        self.data_loss_history = []
        self.residual_loss_history = []
        self.init_loss_history = []
        self.bc_loss_history = []
        self.constraints_loss_history = []

    def try_to_load(self, checkpoint, string):
        try:
            return checkpoint[string]
        except KeyError:
            return None

    def load(self, checkpoint):
        """
        Load the losses history of a file.

        :param checkpoint: name of the .pth file containing the losses history
        :type checkpoint: str
        """
        self.loss = self.try_to_load(checkpoint, "loss")
        self.loss_history = self.try_to_load(checkpoint, "loss_history")
        self.data_loss_history = self.try_to_load(checkpoint, "data_loss_history")
        self.residual_loss_history = self.try_to_load(
            checkpoint, "residual_loss_history"
        )
        self.init_loss_history = self.try_to_load(checkpoint, "init_loss_history")
        self.bc_loss_history = self.try_to_load(checkpoint, "bc_loss_history")
        self.constraints_loss_history = self.try_to_load(
            checkpoint, "constraints_loss_history"
        )

    def init_losses(self):
        """
        initialize all the sublosses at zero
        """
        self.loss = torch.tensor(0.0)
        self.residual_loss = torch.tensor(0.0)
        self.data_loss = torch.tensor(0.0)
        self.init_loss = torch.tensor(0.0)
        self.bc_loss = torch.tensor(0.0)
        self.constraints_loss = torch.tensor(0.0)

    def learning_rate_annealing(self, optimizers: OptimizerData):
        """
        Annealing of the learning rate
        """
        self.residual_loss.backward(create_graph=False, retain_graph=True)
        grad_residual = optimizers.get_first_opt_gradients()
        max_grad_residual = torch.max(torch.abs(grad_residual))
        self.w_res = 1.0

        if self.data_loss_bool:
            self.data_loss.backward(create_graph=False, retain_graph=True)
            grad_data = optimizers.get_first_opt_gradients()
            mean_grad_data = torch.mean(torch.abs(grad_data))
            self.w_data = (
                self.alpha_lr_annealing * max_grad_residual / mean_grad_data
                + (1 - self.alpha_lr_annealing) * self.w_data
            )
            self.w_data_history.append(self.w_data)

        if self.init_loss_bool:
            self.init_loss.backward(create_graph=False, retain_graph=True)
            grad_init = optimizers.get_first_opt_gradients()
            mean_grad_init = torch.mean(torch.abs(grad_init))
            self.w_init = (
                self.alpha_lr_annealing * max_grad_residual / mean_grad_init
                + (1 - self.alpha_lr_annealing) * self.w_init
            )
            self.w_init_history.append(self.w_init)

        if self.bc_loss_bool:
            self.bc_loss.backward(create_graph=False, retain_graph=True)
            grad_bc = optimizers.get_first_opt_gradients()
            mean_grad_bc = torch.mean(torch.abs(grad_bc))
            self.w_bc = (
                self.alpha_lr_annealing * max_grad_residual / mean_grad_bc
                + (1 - self.alpha_lr_annealing) * self.w_bc
            )
            self.w_bc_history.append(self.w_bc)

        if self.constraints_loss_bool:
            self.constraints_loss.backward(create_graph=False, retain_graph=True)
            grad_constraints = optimizers.get_first_opt_gradients()
            mean_grad_constraints = torch.mean(torch.abs(grad_constraints))
            self.w_constraints = (
                self.alpha_lr_annealing * max_grad_residual / mean_grad_constraints
                + (1 - self.alpha_lr_annealing) * self.w_constraints
            )
            self.w_constraints_history.append(self.w_constraints)

        self.alpha_lr_annealing *= 0.999

    def update_residual_loss(self, value: torch.Tensor):
        """
        update the value fo the residual loss

        :param value: the current value of the residual loss
        :type value: torch.Tensor
        """
        self.residual_loss = value

    def update_data_loss(self, value: torch.Tensor):
        """
        update the value fo the data loss

        :param value: the current value of the data loss
        :type value: torch.Tensor
        """
        self.data_loss = value

    def update_init_loss(self, value: torch.Tensor):
        """
        update the value fo the init loss

        :param value: the current value of the init loss
        :type value: torch.Tensor
        """
        self.init_loss = value

    def update_bc_loss(self, value: torch.Tensor):
        """
        update the value fo the bc loss

        :param value: the current value of the bc loss
        :type value: torch.Tensor
        """
        self.bc_loss = value

    def update_constraints_loss(self, value: torch.Tensor):
        """
        update the value fo the constraints loss

        :param value: the current value of the constraints loss
        :type value: torch.Tensor
        """
        self.contrains_loss = value

    def compute_full_loss(self, optimizers: OptimizerData, epoch:int):
        """
        compute the full loss as the combination of all the losses
        """
        if (self.adaptive_weights is not None) and (epoch % self.epochs_adapt):
            if self.adaptive_weights == "annealing":
                self.learning_rate_annealing(optimizers)
            else:
                raise ValueError(
                    f"adaptive_weights {self.adaptive_weights} not recognized"
                )

        self.loss = (
            self.w_res * self.residual_loss
            + self.w_data * self.data_loss
            + self.w_init * self.init_loss
            + self.w_bc * self.bc_loss
            + self.w_constraints * self.constraints_loss
        )

    def update_histories(self):
        """
        Add all the current loss values in the histories
        """
        self.loss_history.append(self.loss.item())
        self.residual_loss_history.append(self.residual_loss.item())
        if self.data_loss_bool:
            self.data_loss_history.append(self.data_loss.item())
        if self.init_loss_bool:
            self.init_loss_history.append(self.init_loss.item())
        if self.bc_loss_bool:
            self.bc_loss_history.append(self.bc_loss.item())
        if self.constraints_loss_bool:
            self.constraints_loss_history.append(self.constraints_loss.item())

    def dict_for_save(self, best_loss: torch.Tensor) -> dict:
        """
        Compute the dictionary for the losses which will be save by the trainer

        :param best_loss: the current value of best full loss
        :type value: torch.Tensor
        :return: dictionary of all data svaed for the losses
        :rtype: dict
        """
        dic = {
            "loss": best_loss,
            "loss_history": self.loss_history,
            "residual_loss_history": self.residual_loss_history,
        }
        if self.data_loss_bool:
            dic["data_loss_history"] = self.data_loss_history
        if self.init_loss_bool:
            dic["init_loss_history"] = self.init_loss_history
        if self.bc_loss_bool:
            dic["bc_loss_history"] = self.bc_loss_history
        if self.constraints_loss_bool:
            dic["constraints_loss_history"] = self.constraints_loss_history
        return dic

    def plot(self, ax):
        """
        Gives the axe contains the plot of the loss histories

        :params ax: the axe which containts the plot
        :type ax: plt.Axes
        :return: the axe which containts the plot
        :type ax: plt.Axes
        """

        ax.semilogy(self.loss_history, label="total loss")
        ax.semilogy(self.residual_loss_history, label="residual")
        if self.data_loss_bool:
            ax.semilogy(self.data_loss_history, label="data")
        if self.init_loss_bool:
            ax.semilogy(self.init_loss_history, label="init")
        if self.bc_loss_bool:
            ax.semilogy(self.bc_loss_history, label="bc")
        if self.constraints_loss_bool:
            ax.semilogy(self.constraints_loss_history, label="contrains")
        ax.set_title("loss history")
        ax.legend()
        return ax
