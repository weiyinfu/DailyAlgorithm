import numpy as np
from scipy import signal
from numpy import fft

"""
不太正确
"""
def generate_problem():
    x, y = np.random.randint(1, 300, (2, 100))
    z = x * y
    return x, y, z


def toa(x):
    return [int(i) for i in str(x)]


def go(x, y):
    x = toa(x)
    y = toa(y)
    m = max(len(x), len(y))
    if len(x) < m:
        x += [0] * (m - len(x))
    if len(y) < m:
        y += [0] * (m - len(y))
    a = fft.fft(x)
    b = fft.fft(y)
    c = [0] * m
    for i in range(len(c)):
        c[i] = a[i] * b[i]
    z = fft.ifft(c)
    print(x, y)
    print(a, b)
    print(z)


x, y, z = generate_problem()
for i, j, k in zip(x, y, z):
    print(i, j, k)
    assert go(i, j) == k
