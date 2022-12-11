from math import *
import numpy as np


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


with open('rv1v2.txt', 'w') as f:
    for r in np.arange(1, 5, 0.1):
        for v1 in np.arange(0.1, 0.7, 0.01):
            for v2 in np.arange(0.1, v1, 0.01):
                ans = get(r, v1, v2)
                f.write('{} {} {} {}\n'.format(r, v1, v2,ans))
