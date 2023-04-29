import sympy as sp

"""
本程序求一个复杂的四重积分
"""
x, y, z, t = sp.symbols("x y z t")


def get(xx, yy, zz, tt):
    st = sp.integrate(1, (t, tt[0], tt[1]))
    sz = sp.integrate(st, (z, zz[0], zz[1]))
    sy = sp.integrate(sz, (y, yy[0], yy[1]))
    sx = sp.integrate(sy, (x, xx[0], xx[1]))
    return sx


def main():
    g1 = get((0, 1), (1 - x, 1), (0, 2 - x - y), (0, 2 - x - y - z))
    g2 = get((0, 1), (0, 1 - x), (0, 1 - x - y), (0, 1))
    g3 = get((0, 1), (0, 1 - x), (1 - x - y, 1), (0, 2 - x - y - z))
    ans = g1 + g2 + g3
    print(ans)


main()
