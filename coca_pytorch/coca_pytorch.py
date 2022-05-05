import torch
from torch import nn, einsum
from einops import rearrange

class CoCa(nn.Module):
    def __init__(
        self,
        dim = 512
    ):
        super().__init__()

    def forward(self, x):
        return x
