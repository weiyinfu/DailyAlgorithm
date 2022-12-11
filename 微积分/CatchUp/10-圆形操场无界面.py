from math import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

"""
用猜测的方式估计轨迹
"""

def get(r, v1, v2):
    a = (0, 0)
    b = (r, 0)
    dt = 0.001
    t = 0
    eps = 1e-1
    w = v2 / r
    while 1:
        b = (r * cos(w * t), r * sin(w * t))
        dir = (b[0] - a[0], b[1] - a[1])
        dir = (dir[0] / hypot(dir[0], dir[1]), dir[1] / hypot(dir[0], dir[1]))
        a = (a[0] + v1 * dir[0] * dt, a[1] + v1 * dir[1] * dt)
        t += dt
        if hypot(a[0] - b[0], a[1] - b[1]) < eps:
            break
    return t


def r_():
    # v1和v2固定情况下，t与r成正比
    x = np.arange(0.1, 4, 0.1)
    y = []
    for v1 in [0.2, 0.25, 0.3]:
        y.clear()
        for r in x:
            t = get(r, v1, 0.15)
            y.append(t)
        plt.plot(x, y)
    plt.legend([0.15, 0.2, 0.25, 0.3])
    plt.show()


def f(x, p):
    k, b = p
    return k * x + b


def residual(p, y, x):
    return y - f(x, p)


def v1_(r):
    x = np.arange(0.11, 0.4, 0.01)
    y = []
    xx = []
    for v1 in x:
        t = get(r, v1, 0.1)
        mine = v1 / 0.1 / sqrt(v1 ** 2 - 0.1 ** 2)
        # print(mine, t)
        xx.append(mine)
        y.append(t)
    xx = np.array(xx)
    y = np.array(y)
    ans = leastsq(residual, [0, 0], args=(y, xx))
    return ans[0]
    # plt.plot(xx, y)
    # plt.plot(xx,f(xx,ans[0]),color='r')
    # print(ans[0])
    # plt.legend(['original','model'])
    # plt.show()


def getParam():
    rr = np.arange(1, 4, 0.1)
    yy = []
    zz = []
    for i in rr:
        an = v1_(i)
        yy.append(an[0])
        zz.append(an[1])
        print(an[0], an[1])
    yyy = leastsq(residual, [0, 0], args=(yy, rr))
    zzz = leastsq(residual, [0, 0], args=(zz, rr))
    print(yyy, zzz)
    plt.plot(rr, yy)
    plt.plot(rr, zz)
    plt.legend(['ans[0]', 'ans[1]'])
    plt.show()


def test():
    for r, v1, v2 in [(1, 0.3, 0.1), (3, 0.3, 0.1), (3.5, 0.3, 0.1)]:
        x = v1 / v2 / sqrt(v1 ** 2 - v2 ** 2)
        k = 1.79014164 * r - 0.66277605
        b = -15.33251214 * r + 6.69277129
        mine = k * x + b
        print(get(r, v1, v2), mine)


test()
