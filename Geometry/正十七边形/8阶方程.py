import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

"""
8阶方程的最后一个根
"""
x = sp.symbols("x")
yy = x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1
ans = sp.solve(yy, x)
print(ans)
x = np.linspace(-10, 10, 1000)
yy = x ** 8 - 4 * x ** 7 - 10 * x ** 6 + 10 * x ** 5 + 15 * x ** 4 - 6 * x ** 3 - 7 * x ** 2 + x + 1
plt.plot(x, yy)
plt.ylim(-3, 3)
plt.hlines([0], np.min(x), np.max(x))
plt.show()
