import torch


def cos_arctan(x):
    return (1 + x**2).sqrt()


def cos_tanh_pi(x):
    return torch.cos(torch.pi * torch.tanh(x))


def sin_tanh_pi(x):
    return torch.sin(torch.pi * torch.tanh(x))
