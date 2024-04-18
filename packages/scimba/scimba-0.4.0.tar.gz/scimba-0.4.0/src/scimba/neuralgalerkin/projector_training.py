import torch

from .. import device


def zero_projector(x, mu, u):
    return torch.zeros_like(u)


class Projector_x:
    DEFAULT_LEARNING_RATE = 1e-3
    DEFAULT_DECAY = 0.99
    FOLDER_FOR_SAVED_NETWORKS = "networks"

    def __init__(self, net, sampler, **kwargs):
        self.network = net
        self.sampler = sampler
        self.f = kwargs.get("w0", zero_projector)

        self.learning_rate = kwargs.get("learning_rate", self.DEFAULT_LEARNING_RATE)
        self.decay = kwargs.get("decay", self.DEFAULT_DECAY)

        self.create_network()
        self.x_collocation = None
        self.mu_collocation = None

    def __call__(self, x: torch.Tensor, mu: torch.Tensor) -> torch.Tensor:
        return self.net(x, mu)

    def create_network(self):
        self.net = self.network.to(device)
        self.Adam_optimizer = torch.optim.Adam(
            self.net.parameters(), lr=self.learning_rate
        )
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.Adam_optimizer, step_size=20, gamma=self.decay
        )

    def train(self, **kwargs):
        epochs = kwargs.get("epochs", 500)
        n_collocation = kwargs.get("n_collocation", 1_000)
        mse_cost_function = torch.nn.MSELoss()

        epoch = 0
        self.loss = torch.tensor(0.0)

        for epoch in range(epochs):

            def closure():
                self.Adam_optimizer.zero_grad()

                self.loss = torch.tensor(0.0)
                self.x_collocation, self.mu_collocation = self.sampler.sampling(
                    n_collocation
                )
                y_pred = self.network.get_w(self.x_collocation, self.mu_collocation)
                y = self.f(self.x_collocation, self.mu_collocation, y_pred)
                self.loss = mse_cost_function(y_pred, y)

                self.loss.backward(retain_graph=True)
                return self.loss

            closure()
            self.Adam_optimizer.step()
            self.scheduler.step()
            print("current loss", self.loss.item())


class Projector_xv:
    DEFAULT_LEARNING_RATE = 1e-3
    DEFAULT_DECAY = 0.99
    FOLDER_FOR_SAVED_NETWORKS = "networks"

    def __init__(self, net, sampler, **kwargs):
        self.network = net
        self.sampler = sampler
        self.f = kwargs.get("w0", zero_projector)

        self.learning_rate = kwargs.get("learning_rate", self.DEFAULT_LEARNING_RATE)
        self.decay = kwargs.get("decay", self.DEFAULT_DECAY)

        self.create_network()
        self.x_collocation = None
        self.mu_collocation = None
        self.v_collocation = None

    def __call__(
        self, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor
    ) -> torch.Tensor:
        return self.net(x, v, mu)

    def create_network(self):
        self.net = self.network.to(device)
        self.Adam_optimizer = torch.optim.Adam(
            self.net.parameters(), lr=self.learning_rate
        )
        self.scheduler = torch.optim.lr_scheduler.StepLR(
            self.Adam_optimizer, step_size=20, gamma=self.decay
        )

    def train(self, **kwargs):
        epochs = kwargs.get("epochs", 500)
        n_collocation = kwargs.get("n_collocation", 1_000)
        mse_cost_function = torch.nn.MSELoss()

        epoch = 0
        self.loss = torch.tensor(0.0)

        for epoch in range(epochs):

            def closure():
                self.Adam_optimizer.zero_grad()

                self.loss = torch.tensor(0.0)
                (
                    self.x_collocation,
                    self.v_collocation,
                    self.mu_collocation,
                ) = self.sampler.sampling(n_collocation)
                y_pred = self.network.get_w(
                    self.x_collocation, self.v_collocation, self.mu_collocation
                )
                y = self.f(
                    self.x_collocation, self.v_collocation, self.mu_collocation, y_pred
                )
                self.loss = mse_cost_function(y_pred, y)

                self.loss.backward(retain_graph=True)
                return self.loss

            closure()
            self.Adam_optimizer.step()
            self.scheduler.step()
            print("current loss", self.loss.item())
