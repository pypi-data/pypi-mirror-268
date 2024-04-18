class ReducedEllitpicNeuralGalerkin:
    def __init__(self, pde_x, x_sampler, f_sampler, AE, projector=None):
        self.pde = pde_x
        self.x_sampler = x_sampler
        self.f_sampler = f_sampler
        self.network = AE

    def compute_inital_data(self, f0):
        pass
        # We use the points of the f sampling used for the data test (fixed points for deepOnet not necessary for the rest)
        # we use en encoder to find the initialization of reduced parameters

    def mass_matrix(self, n_points):
        pass
        # compute the mass matrix using gradient compare to reduced parameters

    def rhs(self, n_points):
        pass
        # compute the mass matrix using gradient compare to reduced parameters

    def one_step(self, n_points):
        pass

    def iterative_method(self, n_points, max_iter):
        pass

    def plot(self):
        pass
