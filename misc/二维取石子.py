"""
有两堆石子，左堆x个，右堆y个。两个人轮流取，每次只能从一堆里取，从左堆可以取1，2或3个，从右堆可以取1，4或8个。取完所有石子的人获胜。求什么样的x和y能够使得后手必胜。

x%4==[0,1,0,1,2,0,1,0,1,2,3,2][y%12]的时候，后手必胜
"""
import numpy as np
from matplotlib import pyplot as plt

a = np.empty((120, 120), dtype=np.int)
aa = np.empty_like(a)

ma = {}


def fast(x, y):
    p = np.concatenate([np.arange(i) for i in [2, 3, 2, 4]] + [[2]])
    first = p[y % len(p)]
    if x % 4 == first:
        return -1
    return 1


def solve(x, y):
    # 先手必胜，返回1，否则返回-1
    if x + y == 0:
        return -1
    if (x, y) in ma:
        return ma[(x, y)]
    mine = -1
    for nx, ny in ((x - 1, y), (x - 2, y), (x - 3, y), (x, y - 1), (x, y - 4), (x, y - 8)):
        if nx < 0 or ny < 0:
            continue
        mine = max(mine, -solve(nx, ny))
    ma[(x, y)] = mine
    return mine


for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        a[x][y] = solve(x, y)
        aa[x][y] = fast(x, y)

assert np.all(a == aa)
fig, axes = plt.subplots(1, 2)
one, two = axes
one.imshow(a)
two.imshow(aa)
plt.show()
