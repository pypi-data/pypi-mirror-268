import scimba.nets.activation as activation
import torch


class ResidualConnection(torch.nn.Module):
    def __init__(
        self, dim: int, activation_type, use_layer_normalization: bool, **kwargs
    ):
        super().__init__()
        self.activation_type = activation_type
        self.use_layer_normalization = use_layer_normalization

        self.lay1 = torch.nn.Linear(dim, dim)
        self.lay2 = torch.nn.Linear(dim, dim)

        if use_layer_normalization:
            self.norm = torch.nn.LayerNorm([dim])

        self.activation_fn = activation.ActivationFunction(
            self.activation_type, **kwargs
        )

    def forward(self, x):
        x_ = self.activation_fn(self.lay1(x))
        x_ = self.activation_fn(self.lay2(x_))
        y = x_ + x
        if self.use_layer_normalization:
            y = self.norm(y)
        return y


class MiniResNet(torch.nn.Module):
    def __init__(
        self,
        dim_in,
        width: int,
        depth: int,
        activation_type,
        use_layer_normalization: bool,
        layer_normalize_only_last_layer: bool,
        **kwargs,
    ):
        super().__init__()

        self.lay_preprocess = torch.nn.Linear(dim_in, width)
        self.lays = torch.nn.ModuleList()
        for i in range(depth):
            add_normalization = use_layer_normalization and (
                (layer_normalize_only_last_layer and i == depth - 1)
                or (not layer_normalize_only_last_layer)
            )
            self.lays.append(
                ResidualConnection(width, activation_type, add_normalization, **kwargs)
            )

    def forward(self, X):
        X = self.lay_preprocess(X)
        for i, lay in enumerate(self.lays):
            X = lay(X)
        return X


class Tnet(torch.nn.Module):
    def __init__(
        self, dim, width, depth: int, activation_type, use_layer_normalization: bool
    ):
        # TODO: la pénalisation orthogonale (si on veut faire tout pareille que dans le vrai PointNet)
        super().__init__()
        self.dim = dim
        self.block_before = MiniResNet(
            dim,
            width,
            depth,
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=True,
        )
        self.block_after = MiniResNet(
            width,
            width,
            depth,
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=False,
        )
        self.lay_to_matrix = torch.nn.Linear(width, dim * dim)

    def forward(self, x):
        assert (
            len(x.shape) == 3
        )  # x.shape =(batch_size,n_sensor,dim). dim peut être dim_u ou un dim_feature plus grand
        batch_size, n_sensor, dim = x.shape
        assert dim == self.dim
        xx = x
        xx = self.block_before(xx)  # (batch_size,n_sensor,width)
        y, _ = torch.max(xx, dim=1)  # (batch_size,width)
        y = self.block_after(y)  # (batch_size,width)

        M = self.lay_to_matrix(y)
        M = torch.reshape(M, [batch_size, dim, dim])
        #   sum_k x_ijk M_ikl
        return torch.sum(x[:, :, :, None] * M[:, None, :, :], dim=2)


# C'est le premier modèle codé. Très élémentaire.
class Maxnet(torch.nn.Module):
    def __init__(
        self,
        dim_x: int,
        dim_u: int,
        dim_alpha: int,
        *,
        activation_type="tanh",
        width01=(100, 30),
        depth01=(3, 3),
        use_layer_normalization01=(True, False),
    ):
        super().__init__()
        self.dim_x = dim_x  # dimension of points x of Omega
        self.dim_u = dim_u  # dimension of the solution u
        self.width = width01

        self.lay_preprocess_x = torch.nn.Linear(self.dim_x, width01[0])
        self.lay_preprocess_u = torch.nn.Linear(self.dim_u, width01[0])

        self.lay_before = torch.nn.ModuleList()
        for i in range(depth01[0]):
            # On effectue la layer normalization qu'à la dernière couche. Car ça rallentit beaucoup.
            layer_normalization = use_layer_normalization01[0] and i == depth01[0] - 1
            # layer_normalization=use_layer_normalization[0]# variante où on la fait partout
            self.lay_before.append(
                ResidualConnection(
                    2 * width01[0],
                    activation_type,
                    use_layer_normalization=layer_normalization,
                )
            )

        self.lay_ajust = torch.nn.Linear(2 * width01[0], width01[1])

        self.lay_after = torch.nn.ModuleList()
        for _ in range(depth01[1]):
            self.lay_after.append(
                ResidualConnection(
                    width01[1], activation_type, use_layer_normalization01[1]
                )
            )

        self.lay_final = torch.nn.Linear(width01[1], dim_alpha)

    def forward(self, x, u):
        batch_size_x, nb_input_sensor_x, dim_x = x.shape
        assert dim_x == self.dim_x
        batch_size_u, nb_input_sensor_u, dim_u = u.shape
        assert dim_u == self.dim_u
        assert batch_size_u == batch_size_x

        x = self.lay_preprocess_x(x)
        u = self.lay_preprocess_u(u)

        xu = torch.cat([x, u], dim=2)  # (b,nb_input_sensor,2*width0)

        for lay in self.lay_before:
            xu = lay(xu)  # (b,nb_input_sensor,2*width0)

        xu = self.lay_ajust(xu)  # (b,nb_input_sensor,width1)

        xu_max, _ = torch.max(xu, dim=1)  # (b,width1)
        z = xu_max

        for lay in self.lay_after:
            z = lay(z)  # (b,2*width1)

        return self.lay_final(z)  # (b,dim_alpha)


class PointNet(torch.nn.Module):
    def __init__(
        self,
        dim_x: int,
        dim_u: int,
        dim_alpha: int,
        activation_type="tanh",
        width01=(100, 30),
        depth01=(3, 3),
        use_layer_normalization=False,
        add_Tnet01=(False, False),
    ):
        super().__init__()
        self.dim_x = dim_x  # dimension of points x of Omega
        self.dim_u = dim_u  # dimension of the solution u
        self.width = width01
        self.add_Tnet01 = add_Tnet01

        # depth=2 est arbitraire, on pourrait le paramétrer en mettant un  paramétre depth012 (un triplet)
        self.block_preprocess_x = MiniResNet(
            dim_x,
            width01[0],
            2,
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=True,
        )
        self.block_preprocess_u = MiniResNet(
            dim_u,
            width01[0],
            2,
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=True,
        )
        # ici il y aura une concaténation
        self.block_before = MiniResNet(
            2 * width01[0],
            width01[1],
            depth01[0],
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=True,
        )
        # ici il y aura le max sur les sensors
        self.block_after = MiniResNet(
            width01[1],
            width01[1],
            depth01[1],
            activation_type,
            use_layer_normalization,
            layer_normalize_only_last_layer=False,
        )
        self.lay_final = torch.nn.Linear(width01[1], dim_alpha)

        """
        Remarque:
        On pourrait aussi appliquer un tnet:
        * sur l'union de xu donc dim=dim_x+dum_u
        * ou sur un preprocess  xu qu'on ajouterait avant le block_before
        Dans l'architecture du PointNet il n'y a pas de tnet après le maxPooling
        (si on veut l'ajouter, il faut modifier notre class Tnet qui n'accepte que des tenseurs de dimension 3).
        """
        if add_Tnet01[0]:
            self.tnet_x = Tnet(dim_x, 32, 2, activation_type, use_layer_normalization)
            self.tnet_u = Tnet(dim_u, 32, 2, activation_type, use_layer_normalization)
        if add_Tnet01[1]:
            self.tnet_feature = Tnet(
                width01[1], 32, 2, activation_type, use_layer_normalization
            )

    def forward(self, x, u):
        batch_size_x, nb_input_sensor_x, dim_x = x.shape
        assert dim_x == self.dim_x
        batch_size_u, nb_input_sensor_u, dim_u = u.shape
        assert dim_u == self.dim_u
        assert batch_size_u == batch_size_x

        if self.add_Tnet01[0]:
            x = self.tnet_x(x)
            u = self.tnet_u(u)

        x = self.block_preprocess_x(x)  # (b,nb_input_sensor,width0)
        u = self.block_preprocess_u(u)  # (b,nb_input_sensor,width0)
        xu = torch.cat([x, u], dim=2)  # (b,nb_input_sensor,2*width0)
        xu = self.block_before(xu)  # (b,nb_input_sensor,width1)

        if self.add_Tnet01[1]:
            xu = self.tnet_feature(xu)

        y, _ = torch.max(xu, dim=1)  # (b,width1)
        y = self.block_after(y)  # (b,width1)
        return self.lay_final(y)  # (b,dim_alpha)
