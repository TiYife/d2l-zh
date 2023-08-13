import torch

x = torch.arange(12)
print(x)
print(x.shape)
print(x.numel())

a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a)
print(b)
print(a + b)
