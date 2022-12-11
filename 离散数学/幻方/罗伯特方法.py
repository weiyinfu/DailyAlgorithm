n = 2
nn = n * 2 + 1


def mo(x):
    return (x % nn + nn) % nn


def f(p):
    r = p // nn
    c = p % nn
    x = mo(n + 1 + r + c)
    y = mo(n - r + c)
    rr = x - y - 1
    cc = x + y - 1 - 2 * n
    while rr % 2 != 0 or rr < 0:
        rr += nn
    while cc % 2 != 0 or cc < 0:
        cc += nn
    rr //= 2
    cc //= 2
    print(p, x, y, r, c, rr, cc)
    return x, y


a = [[0] * nn for _ in range(nn)]
for i in range(0, nn * nn):
    x, y = f(i)
    a[x][y] = i
from pprint import pprint

pprint(a)
