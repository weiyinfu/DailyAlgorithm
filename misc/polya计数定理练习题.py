from collections import Counter

import numpy as np
from tqdm import tqdm

n = 4

"""
polya定理练习题：n行n列，只考虑旋转等价性（4种变换），把这个二维方格使用黑白两色涂色，问有多少种各不相同的方格。
"""


def rotate(a):
    b = np.empty_like(a)
    for x in range(n):
        for y in range(n):
            b[x][y] = a[y][n - 1 - x]
    return b


def bruteforce():
    se = set()

    def tos(a):
        return ''.join(str(i) for i in a.reshape(-1))

    def add(a):
        b = []
        for i in range(4):
            b.append(tos(a))
            a = rotate(a)
        b.sort()
        se.add(b[0])

    for i in tqdm(range(2 ** (n * n))):
        a = np.empty((n, n), dtype=np.int)
        for x in range(n):
            for y in range(n):
                a[x][y] = 1 if (i & (1 << (x * n + y))) else 0
        add(a)
    return len(se)


def get_ring(s):
    fa = [-1] * len(s)

    def find(x):
        if fa[x] == -1:
            return x
        f = find(fa[x])
        fa[x] = f
        return f

    for i in range(len(s)):
        fx = find(i)
        fy = find(s[i])
        if fx != fy:
            fa[fx] = fy
    fa = [find(i) for i in range(len(s))]
    return len(Counter(fa).values())


def polya():
    a = np.arange(n * n).reshape((n, n))
    b = []
    for i in range(4):
        b.append(a)
        a = rotate(a)
    b = [i.reshape(-1) for i in b]
    s = 0
    for i in b:
        r = get_ring(i.copy())
        s += 2 ** r
    return s // 4


# ans = bruteforce()
# print(ans)
ans = polya()
print(ans)
