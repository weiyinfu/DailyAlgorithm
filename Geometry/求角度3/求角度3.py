import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

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


def point2float(p):
    x = p[0].evalf() if type(p[0]) == sp.Expr else p[0]
    y = p[1].evalf() if type(p[1]) == sp.Expr else p[1]
    return x, y


A = (0, 0)
B = (1, 0)
AC = get_line(A, 60)
BC = get_line(B, -80)
C = get_cross(AC, BC)
AD = get_line(A, 80)
BD = get_line(B, -50)
D = get_cross(AD, BD)
ACD = get_angle(A, C, D)
# ACD = sp.trigsimp(ACD)
print(ACD, ACD.evalf(), sp.deg(ACD.evalf()).evalf())
points = [A, B, C, D]
points = np.array([point2float(i) for i in points])

plt.scatter(points[:, 0], points[:, 1])
for x, y, t in zip(points[:, 0], points[:, 1], "ABCD"):
    plt.text(x, y, t)
for i in range(len(points)):
    for j in range(i):
        plt.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]])
plt.show()
