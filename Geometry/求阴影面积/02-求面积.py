import sympy as sp

x, y = sp.symbols("x y")
one = sp.Eq(x * x + y * y, sp.Rational(1, 2) ** 2)
two = sp.Eq(x * x + (y + 1 / sp.sqrt(2)) ** 2, 1)
ans = sp.nonlinsolve([one, two], x, y)
ans = list(ans)
xx, yy = ans[1]
y1 = sp.sqrt(sp.Rational(1, 2) ** 2 - x * x)
y2 = sp.sqrt(1 - x * x) - 1 / sp.sqrt(2)
f = sp.integrate(y1 - y2)
area = (f.subs({x: xx}) - f.subs({x: 0})) * 2
print(area)
print(area.evalf())
