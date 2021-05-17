n = 1
nn = 2 * n + 1


def f(x, y):
    rr = x - y - 1
    cc = x + y - 1 - 2 * n
    while rr % 2 != 0 or rr < 0:
        rr += nn
    while cc % 2 != 0 or cc < 0:
        cc += nn
    return rr // 2 * nn + cc // 2


a = [[0] * nn for _ in range(nn)]
for i in range(nn):
    for j in range(nn):
        a[i][j] = f(i, j)
from pprint import pprint

pprint(a)
