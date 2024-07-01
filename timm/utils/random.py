import numpy as np
import torch
import secrets


def random_seed(seed=42, rank=0):
    torch.manual_seed(seed + rank)
    np.random.seed(seed + rank)
    secrets.SystemRandom().seed(seed + rank)
