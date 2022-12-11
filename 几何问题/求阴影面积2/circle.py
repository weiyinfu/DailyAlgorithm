import numpy as np
import sympy as sp

x = sp.symbols("x")
u = sp.Rational(1, 2) + sp.sqrt(sp.Rational(1, 4) - x * x)
d = sp.sqrt(1 - (x - 1) ** 2)
cross = sp.solve(sp.Eq(u, d), x, simplify=False)[0]
y = sp.integrate(u - d, x)
A = (2 * sp.pi * (sp.Rational(1, 2)) ** 2 - 1) / 4
B = sp.pi / 8
C = y.subs(x, cross) - y.subs(x, 0)  # 使用subs进行符号替换
ans = B - A - C
print(ans, ans.evalf())  # 使用evalf进行浮点数运算


def his():
    print(3 / 4 * np.arcsin(1 / np.sqrt(5)) - 1 / 4)


his()
