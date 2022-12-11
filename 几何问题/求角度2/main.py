import sympy as sp

"""
建立平面直角坐标系
"""
x = sp.symbols("x")


def get_line(p, theta):
    k = sp.tan(theta)
    return k * (x - p[0]) + p[1]


one = get_line((-1, 0), sp.rad(40))
two = get_line((1, 0), sp.rad(-50))
three = sp.tan(sp.rad(70))
xie = 1 / sp.cos(sp.rad(70))
cross = sp.solve(one - two, x)[0]


def dis(f, t):
    return sp.sqrt((f[0] - t[0]) ** 2 + (f[1] - t[1]) ** 2)


A = (1, 0)
C = (0, three)
B = (cross, one.subs({x: cross}))
a = dis(B, C)
b = dis(A, C)
c = dis(A, B)
# get C
ans = sp.acos((a * a + b * b - c * c) / (2 * a * b))
print(ans.simplify())
ans_f = ans.evalf()
print(ans_f, sp.deg(ans_f))
