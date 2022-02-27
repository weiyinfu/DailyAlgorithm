import numpy as np
import scipy.optimize as o

"""
数值法解方程需要指明的初始值足够接近才行
"""


def f(x):
    return x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1


def solve(f, n):
    ans = []
    for i in range(n):
        def ff(x):
            up = f(x)
            down = 1
            for i in ans:
                down *= (x - i)
            if down == 0:
                down = 1e-14
            return up / down

        now = o.fsolve(ff, np.random.random(1))
        ans.append(now[0])
    ans.sort()
    return ans


print(solve(f, 8))
