# Copyright par Vincent Vigon

import torch
from pointnet import PointNet

"""
On crée un couple encoder-decoder qui permet de représenter des
fonction "f" (dans une famille donnée) en des vecteurs "alpha" de la manière suivante

Encodage:
    f_i   #des fonctions
    x_ij  #des points
    u_ij = f_i(x_ij) : #des évaluations
    alpha_i = Encoder(x_i:,u_i:) #l'encodage

Décodage:
    x'_ij  #d'autres points
    u'_ij = Decoder (alpha_i, x'_ij ) #on utilise le décodeur pour évaluer.
    On aura:
    u'_ij proche de f_i(x'_ij)

L'encodeur utilise un PointNet
Le décodeur un DeepONet

On fera un K-test très simple:
dim_x=1
dim_u=1
les fonctions f sont des séries de fouriers avec des coefficients aléatoires
"""


def ContinuousAE(net, **kwargs):
    class ContinuousAE(torch.nn.Module):
        def __init__(self, dim, nb_functions, dim_latent_space, **kwargs):
            super().__init__()
            self.dim = dim
            self.nb_functions = nb_functions
            self.dim_latent_space = dim_latent_space
            self.activation_type = kwargs.get("activayion_type", "tanh")
            self.width01 = kwargs.get("width", (100, 30))
            self.depth01 = kwargs.get("depth", (3, 3))
            self.use_layer_normalization = kwargs.get("pointnet_layer_norm", False)
            self.add_Tnet01 = kwargs.get("pointnet_tnet01", (False, False))

            self.encoder = PointNet(self.dim, self.nb_functions, self.dim_latent_space)
            self.decoder = net(
                in_size=self.dim + self.dim_latent_space,
                out_size=self.nb_functions,
                **kwargs,
            )

        def forward_encoder(
            self, vec_x: torch.Tensor, vec_f: torch.Tensor
        ) -> torch.Tensor:
            return self.encoder(vec_x, vec_f)

        def forward_decoder(self, z: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
            return self.decoder(torch.cat([z, x], axis=1))

        def forward(
            self, vec_x: torch.Tensor, vec_f: torch.Tensor, x: torch.Tensor
        ) -> torch.Tensor:
            z = self.forward_encoder(vec_x, vec_f)
            return self.forward_decoder(z, x)
