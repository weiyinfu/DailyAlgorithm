import numpy as np
import sympy as sp

Ax, Ay = sp.symbols("x y")
B = np.array([0, 0])
C = np.array([1, 0])
A = np.array([Ax, Ay])


def get_dis(A, B):
    return sp.sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


a, b, c = get_dis(B, C), get_dis(A, C), get_dis(A, B)
O = (a * A + b * B + c * C) / (a + b + c)
D = np.array([O[0], 0])
F = (Ax - Ay * (Ax - O[0]) / (Ay - O[1] * 2), 0)
f = F[0] - (1 - O[0])
print(f.simplify())
