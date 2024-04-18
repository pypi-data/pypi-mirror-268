import torch

################# General comments ##################
# This file implement differents activation layers and adaptive activation layers.
# all the activation functions take **kwargs for the constructeur to have the same signature for all activation functions
#####################################################


class AdaptativeTanh(torch.nn.Module):
    """
    Class for tanh activation function with adaptive parameter.

    :param mu: the mean of the Gaussian law
    :type mu: int, optional
    :param sigma: std of the Gaussian law
    :type sigma: float, optional

    :Learnable Parameters:
    * *a* (``float``)
        the parameter of the tanh
    """

    def __init__(self, **kwargs):
        super().__init__()
        mu = kwargs.get("mu", 0.0)
        sigma = kwargs.get("sigma", 0.1)
        self.a = torch.nn.Parameter(torch.randn(()) * sigma + mu)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        exp_p = torch.exp(self.a * x)
        exp_m = 1 / exp_p
        return (exp_p - exp_m) / (exp_p + exp_m)


class Sine(torch.nn.Module):
    """
    Class for Sine activation function

    :param freq: the frequency of the sinus
    :type freq: float, optional
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.freq = kwargs.get("freq", 1.0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return torch.sin(self.freq * x)


class Cosin(torch.nn.Module):
    """
    Class for Cosine activation function

    :param freq: the frequency of the sinus
    :type freq: float, optional
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.freq = kwargs.get("freq", 1.0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return torch.cos(self.freq * x)


class Heaviside(torch.nn.Module):
    """
    Class for Regularized Heaviside activation function

    .. math::
        H_k(x)= 1/(1+e^{-2 k x})
    .. math::
        k >> 1,  \quad H_k(x) = H(x)

    :param k: the regularization parameter
    :type k: float, optional
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.k = kwargs.get("k", 100.0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return 1.0 / (1.0 + torch.exp(-2.0 * self.k * x))


class Tanh(torch.nn.Module):
    """
    Tanh activation function
    """

    def __init__(self, **kwargs):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return torch.tanh(x)


class Id(torch.nn.Module):
    """
    Id activation function

    """

    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return x


class SiLU(torch.nn.Module):
    """
    SiLU activation function

    """

    def __init__(self, **kwargs):
        super().__init__()
        self.ac = torch.nn.SiLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return self.ac.forward(x)


class Sigmoid(torch.nn.Module):
    """
    Sidmoid activation function

    """

    def __init__(self, **kwargs):
        super().__init__()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        return torch.sigmoid(x)


class Wavelet(torch.nn.Module):
    pass


class RbfSinus(torch.nn.Module):
    pass


#### Activation function non local to the dimension (we not apply the same transformation at each dimension)


class IsotropicRadial(torch.nn.Module):
    """
    Isotropic radial basis activation of the form: :math:`\phi(x,m,\sigma)`
    with m the center of the function and sigma the shape parameter.

    Currently implemented:
        -  :math:`\phi(x,m,\sigma)= exp^{-\mid x-m \mid^2 \sigma^2}`
        -  :math:`\phi(x,m,\sigma)= 1/\sqrt(1+(\mid x-m\mid \sigma^2)^2)`

    we use the Lp norm.

    :param in_size: size of the inputs
    :type in_size: int
    :param min_x: minimal  bound of the random initialization for each direction of :math:`\mu`
    :type min_x: float, optional
    :param max_x: maximal bound of the random initialization for each direction of :math:`\mu`
    :type max_x: float, optional
    :param norm: number of norm
    :type norm: int, optional

    :Learnable Parameters:
    * *mu* (``list``)
        the list of the center of the radial basis function (size= in_size)
    * *sigma* (``float``)
        the shape parameter of the radial basis function
    """

    def __init__(self, in_size=1, **kwargs):
        super().__init__()
        self.dim = in_size
        self.min_x = kwargs.get("min_x", 0)
        self.max_x = kwargs.get("max_x", 1)
        self.norm = kwargs.get("norm", 2)
        self.m = torch.nn.Parameter(
            (
                0.5 * (self.min_x + self.max_x)
                + torch.randn((self.dim)) * 0.3 * (self.max_x - self.min_x)
            )
        )
        self.sig = torch.nn.Parameter(torch.abs(10 * torch.randn(()) * 0.1 + 0.2))
        self.type_rbf = kwargs.get("type_rbf", "gaussian")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        norm = torch.norm(x - self.m, p=self.norm, dim=1) ** self.norm
        norm = norm[:, None]
        if self.type_rbf == "gaussian":
            exp_m = torch.exp(-norm / self.sig**2)
        else:
            exp_m = 1.0 / (1.0 + (norm * self.sig**2) * 2.0) ** 0.5
        return exp_m


class AnisotropicRadial(torch.nn.Module):
    """
    Anistropic radial basis activation of the form: :math:`\phi(x,m,\sigma)`
    with m the center of the function and :math:`\Sigma=A A^t + 0.01 I_d` the matrix shape parameter.

    Currently implemented:
        -  :math:`\phi(x,m,\Sigma)= exp^{- ((x-m),\Sigma(x-m))}`
        -  :math:`\phi(x,m,\Sigma)= 1/\sqrt(1+((x-m,\Sigma(x-m)))^2)`

    we use the Lp norm.

    :param in_size: size of the inputs
    :type in_size: int
    :param min_x: minimal  bound of the random initialization for each direction of :math:`\mu`
    :type min_x: float, optional
    :param max_x: maximal bound of the random initialization for each direction of :math:`\mu`
    :type max_x: float, optional
    :param norm: number of norm
    :type norm: int, optional

    :Learnable Parameters:
    * *mu* (``list``)
        the list of the center of the radial basis function (size= in_size)
    * *A* (``float``)
        the shape matrix of the radial basis function (size= in_size*in_size)
    """

    def __init__(self, in_size=1, **kwargs):
        super().__init__()
        self.dim = in_size
        self.min_x = kwargs.get("min_x", 0)
        self.max_x = kwargs.get("max_x", 1)
        self.m = torch.nn.Parameter(
            (
                0.5 * (self.min_x + self.max_x)
                + torch.randn((self.dim)) * 0.2 * (self.max_x - self.min_x)
            )
        )
        self.A = torch.nn.Parameter((torch.rand((self.dim, self.dim))))
        self.type_rbf = kwargs.get("type_rbf", "gaussian")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the tanh function
        :rtype: tensor
        """
        sid = 0.01 * torch.eye(self.dim, self.dim)
        sig2 = torch.matmul(torch.transpose(self.A, 0, 1), self.A) + sid
        norm = torch.linalg.vecdot(torch.mm(x - self.m, sig2), x - self.m, dim=1)
        norm = norm[:, None]
        if self.type_rbf == "gaussian":
            exp_m = torch.exp(-norm)
        else:
            exp_m = 1.0 / (1.0 + norm**2) ** 0.5
        return exp_m


class Rational(torch.nn.Module):
    """
    Class for a rational activation function with adaptive parameters.
    The function takes the form P(x) / Q(x),
    with P a degree 3 polynomial and Q a degree Q polynomial.
    It is initialized as the best approximation of the ReLU function on [- 1, 1].
    The polynomials take the form:
        -  :math:`P(x) = p0 + p1*x + p2*x^2 + p3*x^3`
        -  :math:`Q(x) = q0 + q1*x + q2*x^2`

    :Learnable Parameters:
    * *p0* (``float``)
        degree 0 coefficient of P
    * *p1* (``float``)
        degree 1 coefficient of P
    * *p2* (``float``)
        degree 2 coefficient of P
    * *p3* (``float``)
        degree 3 coefficient of P
    * *q0* (``float``)
        degree 0 coefficient of Q
    * *q1* (``float``)
        degree 1 coefficient of Q
    * *q2* (``float``)
        degree 2 coefficient of Q
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.p0 = torch.nn.Parameter(0.0218)
        self.p1 = torch.nn.Parameter(0.5)
        self.p2 = torch.nn.Parameter(1.5957)
        self.p3 = torch.nn.Parameter(1.1915)
        self.q0 = torch.nn.Parameter(1.0)
        self.q1 = torch.nn.Parameter(0.0)
        self.q2 = torch.nn.Parameter(2.3830)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply the activation function to a tensor x.

        :param x: input tensor
        :type x: tensor
        :return: the tensor after the application to the rational function
        :rtype: tensor
        """
        P = self.p0 + x * (self.p1 + x * (self.p2 + x * self.p3))
        Q = self.q0 + x * (self.q1 + x * self.q2)
        return P / Q


def ActivationFunction(ac_type: str, in_size: int = 1, **kwargs):
    """
    Function to choose the activation function

    :param ac_type: the name of the activation function
    :type ac_type: str
    :param in_size: the dimension (useful for radial basis)
    :type in_size: int
    :return: the activation function
    :rtype: object
    """
    if ac_type == "adaptative_tanh":
        return AdaptativeTanh(**kwargs)
    elif ac_type == "sine":
        return Sine(**kwargs)
    elif ac_type == "cosin":
        return Cosin(**kwargs)
    elif ac_type == "silu":
        return SiLU(**kwargs)
    elif ac_type == "tanh":
        return Tanh(**kwargs)
    elif ac_type == "isotropic_radial":
        return IsotropicRadial(in_size, **kwargs)
    elif ac_type == "anisotropic_radial":
        return AnisotropicRadial(in_size, **kwargs)
    elif ac_type == "sigmoid":
        return Sigmoid(**kwargs)
    elif ac_type == "rational":
        return Rational(**kwargs)
    else:
        return Id()
