from abc import ABC, abstractmethod
from typing import Union

import torch

import scimba.equations.domain as domain
import scimba.sampling.quad as quad

from .. import device


class AbstractODE(ABC):
    """
    Abstract class for ODE model used by PINNs/PINOs/NG

    Each ODE must provide two methods: "initial condition" and "residual"

    :param nb_unknowns: number of variables in the ODE
    :type nb_unknowns: int, optional
    :param time_domain: the bound of the time domain
    :type time_domain: list, optional
    :nb_parameters: number of physical parameters in the ode
    :type nb_parameters: int, optional
    :param parameter_domain: the bound of the time domain
    :type parameter_domain: list[list], optional
    :param data_construction: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    """

    def __init__(
        self,
        nb_unknowns: int = 1,
        time_domain: list = [0.0, 1.0],
        nb_parameters: int = 1,
        parameter_domain: list[list] = [],
        data_construction: str = "sampled",
    ):
        self.nb_unknowns = nb_unknowns
        self.time_domain = torch.tensor(time_domain)
        self.nb_parameters = nb_parameters
        self.parameter_domain = torch.tensor(parameter_domain)
        self.data_construction = data_construction

        self.file_name = self.name + ".pth"

        self.first_derivative = False
        self.second_derivative = False

        # functions to be included in the residual
        # e.g. to solve the equation
        # d^2(w^2)/dt^2 + d(w^3)/dt + alpha * w = t,
        # set f_t = lambda w: w**3 and f_tt = lambda w: w**2

        # by default, f_t and f_tt are identity functions
        self.f_t = None
        self.f_tt = None

        self.force_compute_1st_derivatives_in_residual = False
        self.force_compute_2nd_derivatives_in_residual = False

    def __init_subclass__(cls, *args, **kwargs):
        """
        TOO DOO victor
        This method is called when a subclass is created.
        It is used to add the default values to the
        functions f_t and f_tt to the class.
        """
        super().__init_subclass__(*args, **kwargs)

        def new_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)

            def f_id(w, t, mu):
                unknowns = self.get_variables(w)
                if self.nb_unknowns == 1:
                    return unknowns
                else:
                    return torch.cat(list(unknowns), axis=1)

            self.force_compute_1st_derivatives_in_residual = (
                False or self.force_compute_1st_derivatives_in_residual
            )
            self.force_compute_2nd_derivatives_in_residual = (
                False or self.force_compute_2nd_derivatives_in_residual
            )

            self.f_t_is_identity = self.f_t is None
            if self.f_t_is_identity:
                self.f_t = f_id
                self.force_compute_1st_derivatives_in_residual = True

            self.f_tt_is_identity = self.f_tt is None
            if self.f_tt_is_identity:
                self.f_tt = f_id
                self.force_compute_2nd_derivatives_in_residual = True

            if self.force_compute_2nd_derivatives_in_residual:
                self.first_derivative = True

        cls.__init__ = new_init

    def get_variables(
        self, w: dict, order: str = "w", label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the physical variables from the solution dictionary.

        :param w: the dictionary of physical variables
        :type w: dict
        :param order: the order of derivative that we want
        :type order: str
        :param label: label of the subdomain where we compute the data
        :type label:
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_unknowns == 1:
            return w[order][:, 0, None]
        else:
            return (w[order][:, i, None] for i in range(self.nb_unknowns))

    def prepare_variables(
        self, w: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of physical variables.

        :param w: the tensor of physical variables
        :type w: torch.Tensor
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_unknowns == 1:
            return w[:, 0, None]
        else:
            return (w[:, i, None] for i in range(self.nb_unknowns))

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_times(self, t: torch.Tensor) -> torch.Tensor:
        """
        Returns the time bach from the time tensor.

        :param time: the tensor of physical time
        :type time: torch.Tensor
        :return: the time tensor
        :rtype: torch.Tensor
        """
        return t[:, 0, None]

    @abstractmethod
    def initial_condition(self, mu: torch.Tensor, **kwargs) -> torch.Tensor:
        pass

    @abstractmethod
    def residual(
        self, w: dict, t: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    def make_data(self):
        pass

    @property
    def name(self):
        return type(self).__name__


class AbstractPDEx(ABC):
    """
    Abstract class for spatial PDE model used by PINNs/PINOs/NG

    Each PDE must provide two methods: "boundary_residual" and "residual"

    :param nb_unknowns: number of variables in the PDE
    :type nb_unknowns: int, optional
    :param space_domain: the spatial domain
    :type space_domain: Domain, optional
    :nb_parameters: number of physical parameters in the ode
    :type nb_parameters: int, optional
    :param parameter_domain: the bound of the time domain
    :type parameter_domain: list[list], optional
    :param data_construction: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    """

    def __init__(
        self,
        nb_unknowns: int = 1,
        space_domain: domain.AbstractDomain = None,
        nb_parameters: int = 1,
        parameter_domain: list[list] = [],
        data_construction: str = "sampled",
        compute_normals: bool = False,
    ):
        self.nb_unknowns = nb_unknowns
        self.dimension_x = space_domain.dim
        self.space_domain = space_domain
        self.nb_parameters = nb_parameters
        self.parameter_domain = torch.tensor(parameter_domain)
        self.data_construction = data_construction
        self.compute_normals = compute_normals

        self.file_name = self.name + ".pth"

        self.first_derivative = False
        self.second_derivative = False

        # functions to be included in the space derivative of the solution
        # e.g. to solve the 1D equation
        # d^2(u^2)/dx^2 + u = f,
        # set f_xx = lambda w, x, mu: self.get_variables(w)**2

        # by default, all functions are identity functions
        self.f_x = None
        self.f_y = None
        self.f_xx = None
        self.f_xy = None
        self.f_yy = None
        self.anisotropy_matrix = None

        self.force_compute_1st_derivatives_in_residual = False
        self.force_compute_2nd_derivatives_in_residual = False

    def __init_subclass__(cls, *args, **kwargs):
        """
        This method is called when a subclass is created.
        It is used to add the default values to the
        functions f_t and f_tt to the class.
        """
        super().__init_subclass__(*args, **kwargs)

        def new_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)

            self.force_compute_1st_derivatives_in_residual = (
                False or self.force_compute_1st_derivatives_in_residual
            )
            self.force_compute_2nd_derivatives_in_residual = (
                False or self.force_compute_2nd_derivatives_in_residual
            )

            self.f_x_is_identity = self.f_x is None
            self.f_y_is_identity = self.f_y is None
            if self.f_x_is_identity or self.f_y_is_identity:
                self.force_compute_1st_derivatives_in_residual = True

            self.f_xx_is_identity = self.f_xx is None
            self.f_xy_is_identity = self.f_xy is None
            self.f_yy_is_identity = self.f_yy is None
            if self.f_xx_is_identity or self.f_xy_is_identity or self.f_yy_is_identity:
                self.force_compute_2nd_derivatives_in_residual = True

            if self.force_compute_2nd_derivatives_in_residual:
                self.first_derivative = True

            self.no_anisotropy_matrix = self.anisotropy_matrix is None
            if not self.no_anisotropy_matrix:
                assert self.dimension_x == 2, "Anisotropy matrix is only defined in 2D"

        cls.__init__ = new_init

    def get_variables(
        self, w: dict, order: str = "w", label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the physical variables from the solution dictionary.

        :param w: the dictionary of physical variables
        :type w: dict
        :param order: the order of derivative that we want
        :type order: str
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[order][:, 0, None]
            else:
                return (w[order][:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[order][mask, 0, None]
                else:
                    return (w[order][mask, i, None] for i in range(self.nb_unknowns))

    def prepare_variables(
        self, w: torch.Tensor, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of physical variables.

        :param w: the tensor of physical variables
        :type w: torch.Tensor
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[:, 0, None]
            else:
                return (w[:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[mask, 0, None]
                else:
                    return (w[mask, i, None] for i in range(self.nb_unknowns))

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_coordinates(
        self, x: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the spatial points tensor.

        :param x: the tensor of the physical points
        :type x: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        return (x[:, i, None] for i in range(self.dimension_x))

    @abstractmethod
    def bc_residual(
        self, w: dict, x: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    @abstractmethod
    def residual(
        self, w: dict, x: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    def make_data(self):
        pass

    @property
    def name(self):
        return type(self).__name__


class AbstractPDExv(ABC):
    """
    Abstract class for stationnary kinetic PDE model used by PINNs/PINOs/NG

    Each PDE must provide two methods: "boundary_residual" and "residual"

    :param nb_unknowns: number of variables in the PDE
    :type nb_unknowns: int, optional
    :param space_domain: the spatial domain
    :type space_domain: Domain, optional
    :param velocity_domain: the velocity domain
    :type velocity_domain: Domain, optional
    :nb_parameters: number of physical parameters in the ode
    :type nb_parameters: int, optional
    :param parameter_domain: the bound of the time domain
    :type parameter_domain: list[list], optional
    :param data_construction: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    """

    def __init__(
        self,
        nb_unknowns: int = 1,
        space_domain: domain.AbstractDomain = None,
        velocity_domain: domain.AbstractDomain = None,
        nb_parameters: int = 1,
        parameter_domain: list[list] = [],
        data_construction: str = "sampled",
        compute_normals: bool = False,
    ):
        self.nb_unknowns = nb_unknowns
        self.dimension_x = space_domain.dim
        self.dimension_v = velocity_domain.dim
        self.space_domain = space_domain
        self.velocity_domain = velocity_domain
        self.nb_parameters = nb_parameters
        self.parameter_domain = torch.tensor(parameter_domain)
        self.data_construction = data_construction
        self.compute_normals = compute_normals

        self.file_name = self.name + ".pth"

        self.first_derivative_x = False
        self.second_derivative_x = False
        self.first_derivative_v = False
        self.second_derivative_v = False

    def get_variables(
        self,
        w: dict,
        order: str = "w",
        label: int = None,
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the physical variables from the solution dictionary.

        :param w: the dictionary of physical variables
        :type w: dict
        :param order: the order of derivative that we want
        :type order: str
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[order][:, 0, None]
            else:
                return (w[order][:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[order][mask, 0, None]
                else:
                    return (w[order][mask, i, None] for i in range(self.nb_unknowns))

    def prepare_variables(
        self, w: torch.Tensor, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of physical variables.

        :param w: the tensor of physical variables
        :type w: torch.Tensor
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[:, 0, None]
            else:
                return (w[:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[mask, 0, None]
                else:
                    return (w[mask, i, None] for i in range(self.nb_unknowns))

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_coordinates(
        self, x: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the spatial points tensor.

        :param v: the tensor of the physical points
        :type v: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        raise ValueError(
            "this should not be called anymore, call get_coordinates from SpaceTensor"
        )
        return (x[:, i, None] for i in range(self.dimension_x))

    def get_velocities(
        self, v: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the velocity points tensor.

        :param x: the tensor of the velocity points
        :type x: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        return (v[:, i, None] for i in range(self.dimension_v))

    @abstractmethod
    def bc_residual(
        self, w: dict, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    @abstractmethod
    def residual(
        self, w: dict, x: torch.Tensor, v: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    def make_data(self):
        pass

    @property
    def name(self):
        return type(self).__name__


class AbstractPDEtx(ABC):
    """
    Abstract class for stationnary kinetic PDE model used by PINNs/PINOs/NG

    Each PDE must provide three methods: "boundary_residual", "initial_condition" and "residual"

    :param nb_unknowns: number of variables in the PDE
    :type nb_unknowns: int, optional
    :param time_domain: the bound of the time domain
    :type time_domain: list, optional
    :param space_domain: the spatial domain
    :type space_domain: Domain, optional
    :nb_parameters: number of physical parameters in the ode
    :type nb_parameters: int, optional
    :param parameter_domain: the bound of the time domain
    :type parameter_domain: list[list], optional
    :param data_construction: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    """

    def __init__(
        self,
        nb_unknowns: int = 1,
        space_domain: domain.AbstractDomain = None,
        time_domain: list = [0.0, 1.0],
        nb_parameters: int = 1,
        parameter_domain: list[list] = [],
        data_construction: str = "sampled",
        compute_normals: bool = False,
    ):
        self.nb_unknowns = nb_unknowns
        self.dimension_x = space_domain.dim
        self.time_domain = torch.tensor(time_domain)
        self.space_domain = space_domain
        self.nb_parameters = nb_parameters
        self.parameter_domain = torch.tensor(parameter_domain)
        self.data_construction = data_construction
        self.compute_normals = compute_normals

        self.file_name = self.name + ".pth"

        self.first_derivative_t = False
        self.second_derivative_tt = False
        self.first_derivative_x = False
        self.second_derivative_xx = False

        # functions to be included in the space derivative of the solution
        # e.g. to solve the 1D equation
        # d^2(u^2)/dx^2 + u = f,
        # set f_xx = lambda w, x, mu: self.get_variables(w)**2

        # by default, all functions are identity functions
        self.f_t = None
        self.f_x = None
        self.f_y = None
        self.f_tt = None
        self.f_xx = None
        self.f_xy = None
        self.f_yy = None
        self.anisotropy_matrix = None

        self.force_compute_1st_derivatives_t_in_residual = True
        self.force_compute_2nd_derivatives_t_in_residual = True

        self.force_compute_1st_derivatives_x_in_residual = True
        self.force_compute_2nd_derivatives_x_in_residual = True

    def __init_subclass__(cls, *args, **kwargs):
        """
        This method is called when a subclass is created.
        It is used to add the default values to the
        functions f_t and f_tt to the class.
        """
        super().__init_subclass__(*args, **kwargs)

        def new_init(self, *args, init=cls.__init__, **kwargs):
            init(self, *args, **kwargs)

            # take care of time

            self.force_compute_1st_derivatives_t_in_residual = (
                False or self.force_compute_1st_derivatives_t_in_residual
            )
            self.force_compute_2nd_derivatives_t_in_residual = (
                False or self.force_compute_2nd_derivatives_t_in_residual
            )

            self.f_t_is_identity = self.f_t is None
            if self.f_t_is_identity:
                self.force_compute_1st_derivatives_t_in_residual = True

            self.f_tt_is_identity = self.f_tt is None
            if self.f_tt_is_identity:
                self.force_compute_2nd_derivatives_t_in_residual = True

            if self.first_derivative_t:
                self.force_compute_1st_derivatives_t_in_residual = True

            if self.second_derivative_tt:
                self.force_compute_1st_derivatives_t_in_residual = True
                self.force_compute_2nd_derivatives_t_in_residual = True

            # take care of space

            self.force_compute_1st_derivatives_x_in_residual = (
                False or self.force_compute_1st_derivatives_x_in_residual
            )
            self.force_compute_2nd_derivatives_x_in_residual = (
                False or self.force_compute_2nd_derivatives_x_in_residual
            )

            self.f_x_is_identity = self.f_x is None
            self.f_y_is_identity = self.f_y is None
            if self.f_x_is_identity or self.f_y_is_identity:
                self.force_compute_1st_derivatives_x_in_residual = True

            self.f_xx_is_identity = self.f_xx is None
            self.f_xy_is_identity = self.f_xy is None
            self.f_yy_is_identity = self.f_yy is None
            if self.f_xx_is_identity or self.f_xy_is_identity or self.f_yy_is_identity:
                self.force_compute_2nd_derivatives_x_in_residual = True

            if self.force_compute_2nd_derivatives_x_in_residual:
                self.first_derivative_x = True

            self.no_anisotropy_matrix = self.anisotropy_matrix is None
            if not self.no_anisotropy_matrix:
                assert self.dimension_x == 2, "Anisotropy matrix is only defined in 2D"

        cls.__init__ = new_init

    def get_variables(
        self,
        w: dict,
        order: str = "w",
        label: int = None,
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the physical variables from the solution dictionary.

        :param w: the dictionary of physical variables
        :type w: dict
        :param order: the order of derivative that we want
        :type order: str
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[order][:, 0, None]
            else:
                return (w[order][:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[order][mask, 0, None]
                else:
                    return (w[order][mask, i, None] for i in range(self.nb_unknowns))

    def prepare_variables(
        self, w: torch.Tensor, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of physical variables.

        :param w: the tensor of physical variables
        :type w: torch.Tensor
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[:, 0, None]
            else:
                return (w[:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[mask, 0, None]
                else:
                    return (w[mask, i, None] for i in range(self.nb_unknowns))

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_coordinates(
        self, x: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the spatial points tensor.

        :param v: the tensor of the physical points
        :type v: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        return (x[:, i, None] for i in range(self.dimension_x))

    def get_times(self, t: torch.Tensor) -> torch.Tensor:
        """
        Returns the time bach from the time tensor.

        :param time: the tensor of physical time
        :type time: torch.Tensor
        :return: the time tensor
        :rtype: torch.Tensor
        """
        return t[:, 0, None]

    @abstractmethod
    def initial_condition(
        self, x: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> torch.Tensor:
        pass

    @abstractmethod
    def bc_residual(
        self, w: dict, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    @abstractmethod
    def residual(
        self, w: dict, t: torch.Tensor, x: torch.Tensor, mu: torch.Tensor, **kwargs
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        pass

    @property
    def name(self):
        return type(self).__name__


class AbstractPDEtxv(ABC):
    """
    Abstract class for stationnary kinetic PDE model used by PINNs/PINOs/NG

    Each PDE must provide three methods: "boundary_residual", "initial_condition" and "residual"

    :param nb_unknowns: number of variables in the PDE
    :type nb_unknowns: int, optional
    :param time_domain: the bound of the time domain
    :type time_domain: list, optional
    :param space_domain: the spatial domain
    :type space_domain: Domain, optional
    :param velocity_domain: the spatial domain
    :type velocity_domain: Domain, optional
    :nb_parameters: number of physical parameters in the ode
    :type nb_parameters: int, optional
    :param parameter_domain: the bound of the time domain
    :type parameter_domain: list[list], optional
    :param data_construction: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    :param moment: if there are data. How this data are constructed: sampled or not
    :type data_construction: string, optional
    """

    def __init__(
        self,
        nb_unknowns: int = 1,
        time_domain: list = [0.0, 1.0],
        space_domain: domain.AbstractDomain = None,
        velocity_domain: domain.AbstractDomain = None,
        nb_parameters: int = 0,
        parameter_domain: list[list] = [],
        data_construction: str = "sampled",
        moment_quad: quad.AbstractQuad = None,
        compute_normals: bool = False,
    ):
        self.nb_unknowns = nb_unknowns
        self.dimension_x = space_domain.dim
        self.dimension_v = velocity_domain.dim
        self.dimension_a = velocity_domain.dim
        self.time_domain = torch.tensor(time_domain)
        self.space_domain = space_domain
        self.velocity_domain = velocity_domain
        self.nb_parameters = nb_parameters
        self.parameter_domain = torch.tensor(parameter_domain)
        self.data_construction = data_construction
        self.moment_quad = moment_quad
        self.file_name = self.name + ".pth"
        self.compute_normals = compute_normals

        self.first_derivative_t = False
        self.first_derivative_x = False
        self.first_derivative_v = False

    def get_variables(
        self,
        w: dict,
        order: str = "w",
        label: int = None,
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the physical variables from the solution dictionary.

        :param w: the dictionary of physical variables
        :type w: dict
        :param order: the order of derivative that we want
        :type order: str
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[order][:, 0, None]
            else:
                return (w[order][:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[order][mask, 0, None]
                else:
                    return (w[order][mask, i, None] for i in range(self.nb_unknowns))

    def prepare_variables(
        self, w: torch.Tensor, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of physical variables.

        :param w: the tensor of physical variables
        :type w: torch.Tensor
        :return: a list of tensor containing each variable batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if label is None:
            if self.nb_unknowns == 1:
                return w[:, 0, None]
            else:
                return (w[:, i, None] for i in range(self.nb_unknowns))
        else:
            mask = w["labels"] == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.nb_unknowns == 1:
                    return w[mask, 0, None]
                else:
                    return (w[mask, i, None] for i in range(self.nb_unknowns))

    def get_parameters(
        self, mu: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of parameters from the parameters tensor.

        :param mu: the tensor of physical parameters
        :type mu: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        if self.nb_parameters == 1:
            return mu[:, 0, None]
        else:
            return (mu[:, i, None] for i in range(self.nb_parameters))

    def get_coordinates_x(
        self, x: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the spatial points tensor.

        :param v: the tensor of the physical points
        :type v: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        return (x[:, i, None] for i in range(self.dimension_x))

    def get_coordinates_v(
        self, x: torch.Tensor
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
        Returns the list of coordinates from the spatial points tensor.

        :param v: the tensor of the physical points
        :type v: torch.Tensor
        :return: a list of tensor containing each parameter batch
        :rtype: Union[torch.Tensor, tuple[torch.Tensor]
        """
        return (x[:, i, None] for i in range(self.dimension_v))

    def get_times(self, t: torch.Tensor) -> torch.Tensor:
        """
        Returns the time bach from the time tensor.

        :param time: the tensor of physical time
        :type time: torch.Tensor
        :return: the time tensor
        :rtype: torch.Tensor
        """
        return t[:, 0, None]

    def make_data_from_simulation(self, n_data):
        pass

    def get_density(self, f, t, x, mu, nb_v):
        ### TOOOO DOOOO writte using quad
        v = torch.linspace(
            self.velocity_domain.bound[0][0],
            self.velocity_domain.bound[0][1],
            nb_v,
            device=device,
        )[:, None]

        dv = v[1][0] - v[0][0]

        X = x[None, None, :] * torch.ones_like(v)[:, None, None]
        T = t[None, None, :] * torch.ones_like(v)[:, None, None]
        MU = mu[None, None, :] * torch.ones_like(v)[:, None, None]
        V = torch.ones_like(x)[None, None, :] * v[:, None, None]

        m = x.size()[0] * nb_v
        X = torch.reshape(X, (m, x.size()[1]))
        T = torch.reshape(T, (m, t.size()[1]))
        MU = torch.reshape(MU, (m, mu.size()[1]))
        V = torch.reshape(V, (m, v.size()[1]))

        w = f(T, X, V, MU)
        w = torch.reshape(w, (nb_v, x.size()[0], 1))
        return dv * torch.sum(w, axis=0)

    @abstractmethod
    def residual(self, t, w, x, v, mu, a=None):
        pass

    @abstractmethod
    def initial_condition(self, x, mu, **kwargs):
        pass

    @abstractmethod
    def bc_residual(self, w, t, x, mu, **kwargs):
        pass

    @staticmethod
    def random(
        min_value,
        max_value,
        shape,
        requires_grad=False,
        device=device,
    ):
        random_numbers = torch.rand(
            shape,
            device=device,
            dtype=torch.double,
            requires_grad=requires_grad,
        )
        return min_value + (max_value - min_value) * random_numbers

    @property
    def name(self):
        return type(self).__name__
