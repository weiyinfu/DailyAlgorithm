import sympy as sp

a, b, c = sp.symbols("a b c")
A = sp.symbols("x1 y1")
B = sp.symbols("x2 y2")
C = sp.symbols("x3 y3")
O = sp.symbols("x y")


def get(A, B, C):
    return sp.det(sp.Matrix([
        [A[0], A[1], 1],
        [B[0], B[1], 1],
        [C[0], C[1], 1],
    ]))


f = [
    get(A, B, O) / c,
    get(C, A, O) / b,
    get(B, C, O) / a,
]
SYS = [f[0] - f[1], f[1] - f[2]]
ans = sp.solve(SYS, O[0], O[1])
print(ans)
