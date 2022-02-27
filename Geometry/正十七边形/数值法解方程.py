import scipy.optimize as o
import numpy as np

"""
数值法解方程需要指明的初始值足够接近才行
"""
def f(x):
    return x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1


ans = o.fsolve(f, np.array(5))
print(ans)
