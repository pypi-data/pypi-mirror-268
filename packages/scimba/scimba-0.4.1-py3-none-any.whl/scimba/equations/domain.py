from abc import abstractmethod
from typing import Callable, Union

import torch

"""
We define some basic domains
- SquareDomain: allows to define n dimensional box domain
- DiskDomain: allows to define n dimensional sphere domain or a domain obtain by a regular map apply to the sphere
- ParametricCurveBasedDomain: allows to design boundary domain and manifold.
- SignedDistanceBasedDomain: allows to define domain by a SignedDistanceBasedDomain
- SpaceDomain: a class to generate spatial domain using the other classes
"""


def Id_domain(x):
    return x


class SpaceTensor:
    """
    Class for tensors representing space coordinates.

    :param dim: space dimension
    :type dim: int
    :param x: coordinates
    :type x: torch.Tensor
    :param labels: labels for the coordinates (e.g. labels for boundary conditions, etc.)
    :type labels: torch.Tensor
    :param boundary: boudary point or not. if yes the normals are computed
    :type boundary: torch.Tensor
    :param n: normals of coordinates x
    :type n: torch.Tensor
    """

    def __init__(
        self,
        x: torch.Tensor,
        labels: torch.Tensor,
        boundary: bool = False,
        n: torch.Tensor = None,
    ):
        self.x = x
        self.dim = x.shape[1]
        self.labels = labels
        self.shape = x.shape
        self.boundary = boundary
        self.n = n

    def __getitem__(self, key):
        """
            Overload the getitem [] operator.

            :param key: index where you want the data
            :type key:
            :return: the space tensor with the data only for the key
            :rtype: Spacetensor
        """
        if isinstance(key, int):
            if not self.boundary:
                return SpaceTensor(self.x[key, None], self.labels[key, None])
            else:
                SpaceTensor(
                    self.x[key, None], self.labels[key, None], True, self.n[key, None]
                )
        else:
            if not self.boundary:
                return SpaceTensor(self.x[key], self.labels[key])
            else:
                return SpaceTensor(self.x[key], self.labels[key], True, self.n[key])

    def __setitem__(self, key, value):
        """
            Overload the setitem [] operator.

            :param key: index where you want the data
            :type key:
            :param value: new values for the SpaceTensor associated to the given key
            :type value: SpaceTensor
        """
        self.x[key] = value.x
        self.labels[key] = value.labels
        if self.boundary:
            self.n[key] = value.n

    def repeat(self, size: torch.Size):
        """
            Overload the repeat function.

            :param size: the size of the repeat
            :type size: torch.Size
        """
        if not self.boundary:
            return SpaceTensor(
                torch.repeat_interleave(self.x, size, dim=0),
                torch.repeat_interleave(self.labels, size, dim=0),
            )
        else:
            return SpaceTensor(
                torch.repeat_interleave(self.x, size, dim=0),
                torch.repeat_interleave(self.labels, size, dim=0),
                True,
                torch.repeat_interleave(self.n, size, dim=0),
            )

    def get_coordinates(
        self, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
            Returns the physical coordinates from the current SpaceTensor.

            :param label: the label of the x that the users want
            :type label: int
            :return: the list of coordinates
            :rtype: Union[torch.Tensor, tuple[torch.Tensor]]
        """
        if label is None:
            if self.dim == 1:
                return self.x[:, 0, None]
            else:
                return (self.x[:, i, None] for i in range(self.dim))
        else:
            mask = self.labels == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.dim == 1:
                    return self.x[mask, 0, None]
                else:
                    return (self.x[mask, i, None] for i in range(self.dim))

    def get_normals(
        self, label: int = None
    ) -> Union[torch.Tensor, tuple[torch.Tensor]]:
        """
            Returns the physical coordinates from the current SpaceTensor.

            :param label: the label of the x that the users want
            :type label: int
            :return: the list of coordinates
            :rtype: Union[torch.Tensor, tuple[torch.Tensor]]
        """
        if label is None:
            if self.dim == 1:
                return self.n[:, 0, None]
            else:
                return (self.n[:, i, None] for i in range(self.dim))
        else:
            mask = self.labels == label
            if mask.sum() == 0:
                raise ValueError(f"No coordinates with label {label}")
            else:
                if self.dim == 1:
                    return self.n[mask, 0, None]
                else:
                    return (self.n[mask, i, None] for i in range(self.dim))

    def cat(self, other):
        """
            Function to concetenate two SpaceTensors.

            :param other: The second spaceTensor, to be concetenated
            :type other: SpaceTensor
            :return: the Spacetensor which contains the two previous space tensor
            :rtype: SpaceTensor
        """
        if not self.boundary:
            return SpaceTensor(
                torch.cat([self.x, other.x], dim=0),
                torch.cat([self.labels, other.labels], dim=0),
            )
        else:
            return SpaceTensor(
                torch.cat([self.x, other.x], dim=0),
                torch.cat([self.labels, other.labels], dim=0),
                True,
                torch.cat([self.n, other.n], dim=0),
            )

    def __str__(self) -> str:
        return f"SpaceTensor:\n x = {self.x}\n labels = {self.labels}"

    def detach(self):
        """
            Function to detach the space tensor.

            :param other: The second spaceTensor, to be concetenated
            :type other: SpaceTensor
            :return: the SpaceTensor where x is detach on CPU
            :rtype: SpaceTensor
        """
        if not self.boundary:
            return SpaceTensor(self.x.detach(), self.labels)
        else:
            return SpaceTensor(self.x.detach(), self.labels, self.n.detach())


class AbstractDomain:
    """
    Class for the domain

        :param dim: dimension of the domain
        :type dim: int
        :param domain_type: the type of the domain
     :type domain_type: str
    """

    def __init__(self, dim: int, domain_type: str):
        self.type = domain_type
        self.dim = dim


class ParametricCurveBasedDomain(AbstractDomain):
    """
        Class which describe a surfacic domain by parametric curve.

        :param dim: dimension of the domain
        :type dim: int
        :param parametric_domain: the domain of the parameter which define the curve
        :type center: list[list]
        :param surface: function which define the surface/curve
        :type surface: Callable[[torch.Tensor],torch.Tensor]
    """

    def __init__(
        self,
        dim: int,
        parametric_domain: list[list],
        surface: Callable[[torch.Tensor], torch.Tensor],
    ):
        super().__init__(dim, "parametric_curve_based")

        self.dim_parameters = self.dim - 1
        self.surface = surface
        self.parametric_domain = parametric_domain

    def compute_normals(
        self,
        t: torch.Tensor,
        mapping: Callable[[torch.Tensor], torch.Tensor] = Id_domain,
    ) -> torch.Tensor:
        """
            Compute the normal vector to the surface of the domain.

            :param t: the values of the parametric variables
            :type t: torch.Tensor
            :param mapping: the mapping function
            :type mapping: Callable[[torch.Tensor], torch.Tensor]
            :return: the normal vector
            :rtype: torch.Tensor
        """
        t.requires_grad_()
        y = mapping(self.surface(t))
        if self.dim == 2:
            ones = torch.ones_like(t)
            dy1_dt = torch.autograd.grad(y[:, 0, None], t, ones, retain_graph=True)[0]
            dy2_dt = torch.autograd.grad(y[:, 1, None], t, ones)[0]
            normal = torch.cat([dy2_dt, -dy1_dt], dim=1)
        elif self.dim == 3:
            ones = torch.ones_like(y[:, 0, None])
            dy1_dt = torch.autograd.grad(y[:, 0, None], t, ones, retain_graph=True)[0]
            dy2_dt = torch.autograd.grad(y[:, 1, None], t, ones, retain_graph=True)[0]
            dy3_dt = torch.autograd.grad(y[:, 2, None], t, ones)[0]
            dy_dt1 = torch.stack([dy1_dt[:, 0], dy2_dt[:, 0], dy3_dt[:, 0]], dim=1)
            dy_dt2 = torch.stack([dy1_dt[:, 1], dy2_dt[:, 1], dy3_dt[:, 1]], dim=1)
            normal = torch.cross(dy_dt1, dy_dt2, dim=1)
        norm = torch.norm(normal, dim=1)[:, None]
        return normal / norm


class SquareDomain(AbstractDomain):
    """
        Class which describe the domain square or mapped to square.

        :param dim: dimension of the domain
        :type dim: int
        :param bound: list of the square domain bound
        :type bound: list[list]
    """

    def __init__(
        self,
        dim: int,
        bound: list[list],
    ):
        super().__init__(dim, "square_based")
        self.bound = bound  # min max in each dimension
        self.list_bc_subdomains = []

    def add_bc_subdomain(self, subdomain: ParametricCurveBasedDomain):
        """
            Add the boundary subdomain in the list of boundary subdmains

            :param subdomain: the subdomain that we add
            :type subdomain: ParametricCurveBasedDomain
        """
        self.list_bc_subdomains.append(subdomain)

    def compute_normals(self, x: torch.Tensor, id: int) -> torch.Tensor:
        """
            Compute the normal vector to the surface of the domain.
            id lies between 0 and 2*self.dim-1;
            then id//2 is the dimension on which the edge lies
            and 2*(id%2)-1 is the direction of the edge (-1 or +1)

            :param x: the coordinates of the edge points
            :type x: torch.Tensor
            :param id: the id of the edge under consideration
            :type id: int
            :return: the normal vector
            :rtype: torch.Tensor
        """

        dim_id = id // 2
        edge_id = 2 * (id % 2) - 1

        normal = torch.zeros(self.dim)
        normal[dim_id] = float(edge_id)
        return normal[None, :] * torch.ones_like(x)


class DiskBasedDomain(AbstractDomain):
    """
        Class which describe the domain circle or mapped to circle.

        :param dim: dimension of the domain
        :type dim: int
        :param center: list of coordinate for the center
        :type center: list[list]
        :param radius: radius of the circle
        :type bound: float
        :param mapping: function to map the square on a more general domain
        :type mapping: Callable[[torch.Tensor],torch.Tensor], optional
        :param Jacobian: Jacobian of the mapping
        :type Jacobian: Callable[[torch.Tensor],torch.Tensor], optional
    """

    def __init__(
        self,
        dim: int,
        center: list,
        radius: float,
        mapping: Callable[[torch.Tensor], torch.Tensor] = Id_domain,
        Jacobian: Callable[[torch.Tensor], torch.Tensor] = None,
    ):
        super().__init__(dim, "disk_based")

        assert len(center) == dim

        self.center = center
        self.radius = radius
        self.mapping = mapping

        if self.mapping != Id_domain:
            assert (
                Jacobian is not None
            ), "Jacobian must be provided for non-identity maps"
            self.Jacobian = Jacobian

        self.list_bc_subdomains = []

    def add_bc_subdomain(self, subdomain: ParametricCurveBasedDomain):
        """
            Add the boundary subdomain in the list of boundary subdmains

            :param subdomain: the subdomain that we add
            :type subdomain: ParametricCurveBasedDomain
        """
        self.list_bc_subdomains.append(subdomain)

    def parameterization(self, t: torch.Tensor) -> torch.Tensor:
        """
            compute the points on the sphere using a tensor of parametric variables

            :param t: the parametric variables
            :type t: torch.Tensor
            :return: the coordinates of sphere points
            :rtype: torch.Tensor 
        """
        assert (
            self.dim in [2, 3]
        ), "Only disks (2D) and spheres (3D) are supported in DiskBasedDomain parameterization"

        if self.dim == 2:
            return torch.cat((torch.cos(t), torch.sin(t)), dim=1)
        elif self.dim == 3:
            theta = t[:, 0, None]
            phi = t[:, 1, None]
            return torch.cat(
                (
                    torch.sin(phi) * torch.cos(theta),
                    torch.sin(phi) * torch.sin(theta),
                    torch.cos(phi),
                ),
                dim=1,
            )

    def compute_normals(
        self,
        t: torch.Tensor,
        mapping: Callable[[torch.Tensor], torch.Tensor] = Id_domain,
    ) -> torch.Tensor:
        """
            Compute the normal vector to the surface of the domain.

            :param mapping: the mapping function
            :type mapping: Callable[[torch.Tensor], torch.Tensor]
            :param t: the coordinates
            :type t: torch.Tensor
            :return: the normal vector
            :rtype: torch.Tensor
        """
        y = mapping(self.parameterization(t))
        if self.dim == 2:
            ones = torch.ones_like(t)
            dy1_dt = torch.autograd.grad(y[:, 0, None], t, ones, retain_graph=True)[0]
            dy2_dt = torch.autograd.grad(y[:, 1, None], t, ones)[0]
            normal = torch.cat([dy2_dt, -dy1_dt], dim=1)
        elif self.dim == 3:
            ones = torch.ones_like(y[:, 0, None])
            dy1_dt = torch.autograd.grad(y[:, 0, None], t, ones, retain_graph=True)[0]
            dy2_dt = torch.autograd.grad(y[:, 1, None], t, ones, retain_graph=True)[0]
            dy3_dt = torch.autograd.grad(y[:, 2, None], t, ones)[0]
            dy_dt1 = torch.stack([dy1_dt[:, 0], dy2_dt[:, 0], dy3_dt[:, 0]], dim=1)
            dy_dt2 = torch.stack([dy1_dt[:, 1], dy2_dt[:, 1], dy3_dt[:, 1]], dim=1)
            normal = torch.cross(dy_dt1, dy_dt2, dim=1)
        norm = torch.norm(normal, dim=1)[:, None]
        return normal / norm


class SignedDistance:
    """
        Class for the signed Distance function. Approximative or exact Signed distance function.

        :param dim: dimension of the domain
        :type dim: int
        :param threshold: threshold to determinate how we sample inside the domain. We use signedDistance(x)<threshold
        :type threshold: float
    """

    def __init__(self, dim: int, threshold: float = 0.0):
        self.dim = dim
        self.threshold = threshold

    @abstractmethod
    def sdf(self, x: SpaceTensor) -> torch.Tensor:
        pass


class PolygonalApproxSignedDistance(SignedDistance):
    """
        Class for the  approximate signed Distance function for polygonal following the paper
        Ref : "Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks", N. Sukumar, Ankit Srivastava

        :param dim: dimension of the domain
        :type dim: int
        :param threshold: threshold to determinate how we sample inside the domain. We use signedDistance(x)<threshold
        :type threshold: float
        :param point: coordinates of  thevertices of the polygone
        :type point: list[list]
    """

    def __init__(self, dim: int, points: list[list], threshold: float = 0.01):
        super().__init__(dim, threshold)
        self.points = torch.tensor(points)

    def vectorial_product(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """
            Returns the vectorial product between two batched vectors

            :param x: left tensor
            :type x: torch.Tensor
            :param y: right tensor
            :type y: torch.Tensor
            :return; the vectorial product between x and yy
            :rtype: torch.Tensor
        """
        if self.dim == 2:
            res = x[:, 0] * y[:, 1] - y[:, 0] * x[:, 1]
        return res

    def dot_product(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """
            Returns the scalar product between two batched vectors

            :param x: left tensor
            :type x: torch.Tensor
            :param y: right tensor
            :type y: torch.Tensor
            :return; the dot product between x and yy
            :rtype: torch.Tensor
        """
        if self.dim == 2:
            res = x[:, 0] * y[:, 0] + y[:, 1] * x[:, 1]
        return res

    def vect_x_to_xi(self, x: torch.Tensor, i: int):
        """
            Returns the batched vector x-xi with xi vertices of the polygonal

            :param x: left tensor
            :type x: torch.Tensor
            :param i: the number of the polygonal point
            :type i: int
            :return: the batched vector x -xi
            :rtype: torch.Tensor
        """
        n = x.shape[0]
        xi = self.points[i, :].repeat((n, 1))
        return xi - x

    def dist(self, y: torch.Tensor) -> torch.Tensor:
        """
            Returns the batched distance of a batched tensor of vector

            :param y: the tensor
            :type y: torch.Tensor
            :return; the batched norm of y
            :rtype: torch.Tensor
        """
        return torch.norm(y, dim=1)

    def phi(self, x: torch.Tensor) -> torch.Tensor:
        """
            Returns the batched function phi for a polygonal

            :param x: the tensor
            :type x: torch.Tensor
            :return: the value of phi at the point x
            :rtype: torch.Tensor
        """
        res = torch.zeros_like(x[:, 0])
        for i in range(0, len(self.points)):
            j = (i + 1) % len(self.points)
            ri = self.vect_x_to_xi(x, i)
            rj = self.vect_x_to_xi(x, j)
            di = self.dist(ri)
            dj = self.dist(rj)
            ti = self.vectorial_product(ri, rj) / (self.dot_product(ri, rj) + di * dj)
            res = res + (1.0 / di + 1.0 / dj) * ti
        return res[:, None]

    def sdf(self, data: SpaceTensor) -> torch.Tensor:
        """
            Returns the batched approximated signed distance for a polygonal

            :param data: the SpaceTensor
            :type data: SpaceTensor
            :return: the value of the sdf at the points of data
            :rtype: SpaceTensor
        """
        return self.dim / self.phi(data.x)


class SignedDistanceBasedDomain(AbstractDomain):
    """
        Class for the sphere domain in any dimension

        :param dim: the physical dimension
        :type dim: int
        :param sd_function: a object of the SignedDistance class which will describe the domain
        :type sd_function: SignedDistance
        :param bound: bound of the square domain where we sample for the reject algorithm
        :type bound: list[list]
        :param mapping: function to map the square on a more general domain
        :type mapping: Callable[[torch.Tensor],torch.Tensor], optional
    """

    def __init__(
        self,
        dim: int,
        bound,
        sd_function: SignedDistance,
        mapping: Callable[[torch.Tensor], torch.Tensor] = Id_domain,
    ):
        super().__init__(dim, "sd_based")
        self.sdf = sd_function.sdf
        self.threshold = sd_function.threshold
        self.surrounding_domain = SquareDomain(dim, bound)
        self.list_bc_subdomains = []
        self.mapping = mapping

    def add_bc_subdomain(self, subdomain: ParametricCurveBasedDomain):
        """
            Add the boundary subdomain in the list of boundary subdmains

            :param subdomain: the subdomain that we add
            :type subdomain: ParametricCurveBasedDomain
        """
        self.list_bc_subdomains.append(subdomain)

    def is_inside(self, x: SpaceTensor) -> torch.Tensor:
        """
        Compute boolean to see if element is in the domain

            :param x: elements sampled in the box
            :type x: torch.Tensor
            :return: the tensor containing the boolean
            :rtype: torch.torch.Tensor
        """
        return self.sdf(x) < -self.threshold

    def is_outside(self, x: SpaceTensor) -> torch.Tensor:
        """
        Compute boolean to see if element is in the domain

            :param x: elements sampled in the box
            :type x: torch.Tensor
            :return: the tensor containing the boolean
            :rtype: torch.torch.Tensor
        """
        return self.sdf(x) > 0.0

    def on_border(self, x: SpaceTensor) -> torch.Tensor:
        """
            Compute boolean to see if element is in the border

            :param x: elements sampled in the box
            :type x: torch.Tensor
            :return: the tensor containing the boolean
            :rtype: torch.torch.Tensor
        """
        tol = 1e-4
        phi = self.sdf(x)
        return torch.abs(phi) < tol


class SpaceDomain(AbstractDomain):
    """
        Class which describe a general domain with
        multiples boundary subdomains, holes and insider subdomains.

        :param dim: dimension of the domain
        :type dim: int
        :param large_domain: the bigger domain
        :type large_domain: AbstractDomain
    """

    def __init__(
        self,
        dim: int,
        large_domain: AbstractDomain,
    ):
        super().__init__(dim, "general")

        self.dim = dim
        self.large_domain = large_domain
        self.list_bc_subdomains = []
        self.list_subdomains = []
        self.list_holes = []
        self.full_bc_domain = True
        # if true there is no sub boundary domain and all the boundary is sampled
        # in one time

    def add_bc_subdomain(self, subdomain: ParametricCurveBasedDomain):
        """
            Add a parametricCurve Domain to a list of BC subdmain.
            If a bc subdomain is add the boundary will not sample in one time

            :param subdomain: the subdomain that we add to the list:
            :type subdomain: ParametricCurveBasedDomain
        """
        self.large_domain.add_bc_subdomain(subdomain)
        # self.list_bc_subdomains.append(subdomain)
        self.full_bc_domain = False

    def add_subdomain(self, subdomain: SignedDistanceBasedDomain):
        """
            Add a Domain based on signed distance to a list of subdmain.

            :param subdomain: the subdomain that we add to the list:
            :type subdomain: SignedDistanceBasedDomain
        """
        self.list_subdomains.append(subdomain)

    def add_hole(self, subdomain: SignedDistanceBasedDomain):
        """
            Add a Domain based on signed distance to a list of holes.

            :param subdomain: the subdomain that we add to the list:
            :type subdomain: SignedDistanceBasedDomain
        """
        self.list_holes.append(subdomain)


if __name__ == "__main__":
    import scimba.equations.tests as tests

    tests.test_domain.test_domain()
    tests.test_domain.test_parameteric_sphere_normals()
