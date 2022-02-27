"""
以底边中点为原点建系，第二种方法
"""
import sympy as sp

A = (-1, 0)
B = (1, 0)
C = (0, sp.tan(sp.rad(70)))
x = sp.symbols("x")


def get_line(p, theta):
    k = sp.tan(sp.rad(theta))
    return k * (x - p[0]) + p[1]


def get_cross(line1, line2):
    xx = sp.solve(sp.Eq(line1, line2), x)[0]
    yy = line1.subs({x: xx})
    return xx, yy


def get_dis(p, q):
    return sp.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def get_point(A, B, dis2A):
    ax, ay = A
    bx, by = B
    total = get_dis(A, B)
    p = 1 - dis2A / total
    return ax * p + bx * (1 - p), ay * p + by * (1 - p)


def get_angle(A, B, C):
    # 求角B
    c = get_dis(A, B)
    a = get_dis(B, C)
    b = get_dis(A, C)
    return sp.acos((a * a + c * c - b * b) / (2 * a * c))


left = get_line(A, 70)
right_half = get_line(B, -40)
D = get_cross(left, right_half)
d = get_dis(C, D)
E = get_point(B, C, d)
ans = get_angle(B, D, E)
print(ans)
print(ans.evalf())
