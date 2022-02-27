import numpy as np


def one():
    t = np.linspace(0, 4, 100)
    x = 4 / 3 * t ** 3
    y = 2 * t * t
    z = 2 * t
    dx = x[1:] - x[:-1]
    dy = y[1:] - y[:-1]
    dz = z[1:] - z[:-1]
    d = (dx * dx + dy * dy + dz * dz) ** 0.5
    ans = np.sum(d)
    print(ans)


one()
import sympy as sp


def two():
    # sympy 求积分有bug
    t = sp.symbols("t")
    dx = 4 * t * t
    dy = 4 * t
    dz = 2
    d = sp.sqrt(dx * dx + dy * dy + dz * dz)
    print(d)
    f = sp.integrate(d)
    print(f)
    print(f.evalf(subs={t: 0}) - f.evalf(subs={t: 4}))


two()
print(2 / 3 * 4 ** 3 + 4)
