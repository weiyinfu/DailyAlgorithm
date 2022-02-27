import sympy as sp

A = sp.symbols("Ax Ay")
B = sp.symbols("Bx By")
C = sp.symbols("Cx Cy")
O = sp.symbols("x y")


def get(A, B, C):
    v1 = (B[0] - C[0], B[1] - C[1])
    v2 = (A[0] - O[0], A[1] - O[1])
    return v1[0] * v2[0] + v1[1] * v2[1]


f = [
    get(A, B, C),
    get(B, C, A),
    get(C, A, B),
]
ans = sp.solve(f, O[0], O[1])
x, y = ans.values()
x=x.simplify()
y=y.simplify()
print(x.expand())
print(y.expand())

