import numpy as np


def check(n):
    a = [np.linspace(0.0001, np.pi / 2, 10000) for _ in range(n - 1)]
    a.append(np.arctan(2 / np.prod(np.tan(a), axis=0)))
    a = np.array(a)
    z = np.sum(np.cos(a), axis=0)
    ind = np.argmax(z)
    print(a[:, ind])
    return z[ind]


def f(n):
    return max(n / (3 ** 0.5), n - 1)


for i in range(2, 6):
    print(f(i), check(i))
