from sympy import *

a = symbols("a")
t = tan(a)
tt = 2 * t / (1 - t ** 2)
ttt = (tt + t) / (1 - tt * t)
res = solve(ttt * 7 - 15 * tt, [a])
print(res)
