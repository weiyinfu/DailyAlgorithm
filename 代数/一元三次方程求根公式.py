import sympy as sp

x, a, b, c = sp.symbols("x a b c")
f = x ** 3 + a * x * x + b * x + c
ans = sp.solve(f, x)
print(ans)

"""
一元四次方程求根公式
"""
x, a, b, c, d = sp.symbols("x a b c d")
f = x ** 4 + a * x ** 3 + b * x * x + c * x + d
print(sp.solve(f, x))

"""
一元五次方程求根公式
"""
x, a, b, c, d, e = sp.symbols("x a b c d e")
f = x ** 5 + a * x ** 4 + b * x ** 3 + c * x * x + d * x + e
print(sp.solve(f, x))
