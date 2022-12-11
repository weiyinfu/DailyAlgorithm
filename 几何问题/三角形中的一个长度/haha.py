import sympy as sp

"""
似乎是只能找到七个条件。因此无解
"""
ALL = sp.symbols("Ay Bx Cx Ex Fx Fy Dx Dy")
Ay, Bx, Cx, Ex, Fx, Fy, Dx, Dy = ALL
A = (0, Ay)
B = (Bx, 0)
C = (Cx, 0)
F = (Fx, Fy)
D = (Dx, Dy)
E = (Ex, 0)


def get_dis(p, q):
    return sp.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def get_angle(A, B, C):
    # 求角B
    c = get_dis(A, B)
    a = get_dis(B, C)
    b = get_dis(A, C)
    return sp.acos((a * a + c * c - b * b) / (2 * a * c))


def chuizhi(A, B, C, D):
    AB = (A[0] - B[0], A[1] - B[1])
    CD = (C[0] - D[0], C[1] - D[1])
    return AB[0] * CD[0] + AB[1] * CD[1]


def pingxing(A, B, C, D):
    AB = (A[0] - B[0], A[1] - B[1])
    CD = (C[0] - D[0], C[1] - D[1])
    return AB[0] * CD[1] - AB[1] * CD[0]


def point2float(p):
    x = p[0].evalf() if type(p[0]) == sp.Expr else p[0]
    y = p[1].evalf() if type(p[1]) == sp.Expr else p[1]
    return x, y


system = [
    get_angle(A, B, C) - get_angle(B, A, E) - get_angle(B, C, D),  # B=1+2
    chuizhi(E, F, A, B),  # EF垂直AB
    pingxing(B, F, B, A),  # F在AB上
    pingxing(B, D, B, A),  # D在BA上
    pingxing(B, E, B, C),  # E在BC上
    get_dis(A, E) - get_dis(C, D),  # AE=CD
    get_dis(B, F) - sp.Rational(4, 3),  # BF=4/23
]
print(system)
res = sp.solve(system, ALL)
print(res)
