import numpy as np
from scipy.integrate import dblquad
from sympy import *
import sympy as sp

"""
一个边长为3，4，5的直角三角形，在它里面随机画一条射线，问射线与长度为5的边相交的概率是多少？
"""


def jifen():
    # 二微积分公式
    n = 1000
    eps = 1e-9
    a = []

    for x in np.linspace(eps, 3, n):
        for y in np.linspace(eps, 4 - 4 / 3 * x + eps, n):
            theta = np.arctan((3 - x) / y)
            alpha = np.arctan(x / (4 - y))
            p = (np.pi - theta + alpha) / (np.pi * 2)
            a.append(p)
    print(np.mean(a))


def use_sympy():
    # 如何使用sympy求解此问题
    x, y = symbols("x y")
    theta = sp.atan((3 - x) / y)
    alpha = sp.atan(x / (4 - y))
    p = (sp.pi - theta + alpha) / (sp.pi * 2)
    fx = sp.integrate(p, y)
    print(fx)


def standard():
    ans = dblquad(
        lambda y, x: 1.0 / 8 - (np.arctan2(4 - y, x) + np.arctan2(3 - x, y)) / (12 * np.pi), 0, 3,
        lambda x: 0, lambda x: -4 * x / 3 + 4)
    print(ans)


def bruteforce():
    a = np.random.random((10000000, 2))
    a[:, 0] *= 3
    a[:, 1] *= 4
    bad = np.argwhere(a[:, 1] > 4 - 4 / 3 * a[:, 0])
    mid = (3 / 2, 4 / 2)
    a[bad, 0] = mid[0] * 2 - a[bad, 0]
    a[bad, 1] = mid[1] * 2 - a[bad, 1]
    x = a[:, 0]
    y = a[:, 1]
    theta = np.arctan((3 - x) / y)
    alpha = np.arctan(x / (4 - y))
    p = (np.pi - theta + alpha) / (np.pi * 2)
    ans = np.mean(p)
    print(ans)
    return ans


use_sympy()
# jifen()
# bruteforce()
# standard()
