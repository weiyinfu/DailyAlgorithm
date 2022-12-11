import sympy as sp

a, b, c, A, B, C = sp.symbols("a b c A B C")


def cos(a, b, c):
    return (a * a + b * b - c * c) / (2 * a * b)


f = [
    sp.Eq(sp.cos(A), cos(b, c, a)),
    sp.Eq(sp.cos(B), cos(a, c, b)),
    sp.Eq(sp.cos(C), cos(b, a, c)),
]
ans = sp.nonlinsolve(f, a, b, c)
print(ans)
