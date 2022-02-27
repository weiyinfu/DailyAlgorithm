from sympy import *


def solve1():
    alpha, beta, gama, x = symbols("alpha beta gama x")

    def f(a, b, c):
        return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    cosalpha = f(4, 7, x)
    cosbeta = f(4, 9, x)
    cosgama = f(7, 9, sqrt(2) * x)
    sinalpha = sqrt(1 - cosalpha ** 2)
    sinbesta = sqrt(1 - cosbeta ** 2)
    singama = sqrt(1 - cosgama ** 2)
    cosall = cosalpha * cosbeta * cosgama - sinalpha * sinbesta * cosgama - sinalpha * cosbeta * singama - cosalpha * sinbesta * singama
    ans = solve(cosall - 1, x)
    print(ans)


def solve2():
    # sympy没有实现这个函数
    x = symbols("x")

    def f(a, b, c):
        return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    alpha = acos(f(4, 7, x))
    beta = acos(f(4, 9, x))
    gama = acos(f(7, 9, sqrt(2) * x))
    ans = solve(cos(alpha + beta + gama) - 1, x)
    print(ans)


def check():
    import numpy as np
    x = np.sqrt(65 + 28 * 2 ** 0.5)

    def f(a, b, c):
        return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

    alpha = np.arccos(f(4, 7, x))
    beta = np.arccos(f(4, 9, x))
    gama = np.arccos(f(7, 9, x * 2 ** 0.5))
    total = alpha + beta + gama
    print(alpha + beta + gama, alpha, beta, gama, np.cos(total))


# check()
solve2()
