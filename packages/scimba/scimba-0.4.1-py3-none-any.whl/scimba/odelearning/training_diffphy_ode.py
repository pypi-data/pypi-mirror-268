# ---- libraries ----
import random as rand

import torch


# ---- classes and functions ----
class Trainer_DF_ODE_with_data:
    DEFAULT_DECAY = 0.99
    DEFAULT_FILE_NAME = "network.pth"
    DEFAULT_LEARNING_RATE = 1e-3
    FOLDER_FOR_SAVE_WEIGHTS = "weights"
    DEFAULT_BATCH= 10

    def __init__(self,
                 model,
                 data,
                 loss_f,
                 **kwargs):
        self.model = model
        self.loss_function = loss_f
        self.data = data

        self.learning_rate = kwargs.get("learning_rate", self.DEFAULT_LEARNING_RATE)
        self.decay = kwargs.get("decay", self.DEFAULT_DECAY)
        self.nb_batch = kwargs.get("nb_batch", self.DEFAULT_BATCH)

        self.create_optimizer()
        self.loss_history = []
        self.loss = 0

        self.file_name = kwargs.get("file_name", self.DEFAULT_FILE_NAME)
        self.folder_name = kwargs.get("folder_name", self.FOLDER_FOR_SAVE_WEIGHTS)

    def create_optimizer(self):
        self.optimizer = torch.optim.Adam(self.model.flux.parameters(), lr=self.learning_rate)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=20, gamma=self.decay)

    def train_one_epoch(self):

        # ---- initialize running loss ----
        running_loss = 0.

        nb_total_time_batch = self.data.values.shape[0]
        nb_total_init_batch = self.data.values.shape[2]
        batch_size_init = min(int(self.data.values.shape[2]/self.nb_batch),nb_total_init_batch)

        # ---- extract batch indices ----
        batch_indices = Trainer_DF_ODE_with_data.get_random_integers(start=0, end=len(self.data.ts)-1)
        permutation = torch.randperm(self.data.values.shape[2])
        # batch_indices = torch.randperm(len(self.data.ts)-1)

        for t_batch in batch_indices:
            for i_batch in range(0, nb_total_init_batch, batch_size_init):
                indices = permutation[i_batch : i_batch + batch_size_init]
                # 1- initialize gradients of all optimized tensors before each iteration
                self.optimizer.zero_grad()

                # ---- get batch data ----
                times_batch, states_batch,mu_batch = self.data.ts[t_batch,:], self.data.values[t_batch,:,indices,:], self.data.tmu[indices,:]
                initial_state_batch =  self.data.values[t_batch,0,indices,:]

            # ---- 2- forward pass on batch data ----
                self.model.time_scheme(initial_data=initial_state_batch, t=times_batch,mu=mu_batch)
                prediction_batch = self.model.solution
                prediction_batch.requires_grad_(True)

            # ---- 3- compute loss and gradients via backpropagation ----
                self.loss = self.loss_function.apply(prediction_batch, states_batch,times_batch,mu_batch)
                self.loss.backward(retain_graph=True)

            # ---- 4- one step of gradient descent (weight update) ----
                self.optimizer.step()
                self.scheduler.step()

                running_loss += self.loss.item()
        return running_loss/len(batch_indices)

    def train(self, **kwargs):
        epochs = kwargs.get("epochs", 100)

        try:
            best_loss_value = self.loss.item()
        except AttributeError:
            best_loss_value = 1e10

        for epoch in range(epochs):
            epoch_loss = Trainer_DF_ODE_with_data.train_one_epoch(self)
            self.loss_history.append(epoch_loss)

            if epoch % 1 == 0:
                print(f"epoch {epoch: 5d}: current loss = {epoch_loss:5.2e}")

            # if epoch_loss < best_loss_value:
            # to be corrected
            #     print(f"epoch {epoch: 5d}: best loss = {self.loss.item():5.2e}")
            #     best_loss = self.loss.clone()
            #     best_loss_value = best_loss.item()
            #     # best_net = copy.deepcopy(self.net.state_dict())
            #     best_optimizer = copy.deepcopy(self.optimizer.state_dict())
            #     best_scheduler = copy.deepcopy(self.scheduler.state_dict())

    @staticmethod
    def get_random_integers(start: int, end: int):
        return rand.sample(range(start, end + 1), k=end - start + 1)
