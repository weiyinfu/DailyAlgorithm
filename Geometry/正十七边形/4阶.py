import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

"""
实验证明，根在8阶方程中，他在1，10区间上有两个解
"""
x = sp.symbols("x")
y = x ** 4 + 4 * x ** 3 - 4 * x ** 2 - x + 1
yy = x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1
yyy = 1 - 1 / (2 * x) - 32 / x ** 2 + 168 / x ** 4 - 336 / x ** 6 + 330 / x ** 8 - 176 / x ** 10 + 52 / x ** 12 - 8 / x ** 14 + 1 / (2 * x ** 16)

standard = 1 / 2 / np.cos(np.pi * 8 / 17)
res = y.evalf(subs={x: standard})
print(res)
res = yy.evalf(subs={x: standard})
print(res)
res = yyy.evalf(subs={x: standard})
print(res)

x = np.linspace(1, 10, 100)
y = x ** 4 + 4 * x ** 3 - 4 * x ** 2 - x + 1
yy = x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1
yyy = 1 - 1 / (2 * x) - 32 / x ** 2 + 168 / x ** 4 - 336 / x ** 6 + 330 / x ** 8 - 176 / x ** 10 + 52 / x ** 12 - 8 / x ** 14 + 1 / (2 * x ** 16)
plt.plot(x, yyy, label='16')
plt.plot(x, yy, label='8')
plt.plot(x, y, label='4')
plt.vlines([standard], np.min(yyy), np.max(yyy))
plt.hlines([0], np.min(x), np.max(x))
plt.legend()
plt.ylim(-3, 3)
plt.show()
