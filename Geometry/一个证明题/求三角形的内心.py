import sympy as sp

Ax, Ay, Bx, By, Cx, Cy, Ox, Oy = sp.symbols("Ax Ay Bx By Cx Cy Ox Oy")
A = (Ax, Ay)
B = (Bx, By)
C = (Cx, Cy)
O = (Ox, Oy)
x = sp.symbols("x")

"""
sympy比较垃圾，求三角形内心求不出来
"""


def point2line_square(O, A, B):
    # O点到直线AB的距离的平方
    return sp.det(sp.Matrix([
        [A[0], A[1], 1],
        [B[0], B[1], 1],
        [O[0], O[1], 1],
    ])) ** 2 / ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


oAB = point2line_square(O, A, B)
oBC = point2line_square(O, B, C)
oAC = point2line_square(O, A, C)
SYS = [oAB - oBC, oAB - oAC]


def one():
    print(SYS)
    Ox_value = sp.solve(SYS[0], Ox)[0]
    print("Ox:", Ox_value)
    second = SYS[1].subs({Ox: Ox_value})
    second = sp.simplify(second)
    print(sp.expand(second))
    print(second)
    Oy_value = sp.solve(second, Oy)
    print(Oy_value)


def two():
    ans = sp.nonlinsolve(SYS, Ox, Oy)
    print(ans)


two()
