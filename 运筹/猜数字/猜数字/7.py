"""
7个数字给2猜1有序，答案
验证正确性
"""
from typing import List

ma = {
    (1, 2): 0,
    (1, 3): 0,
    (1, 4): 0,
    (1, 5): 0,
    (1, 6): 0,
    (2, 3): 0,
    (2, 4): 0,
    (2, 5): 0,
    (2, 6): 0,
    (3, 4): 0,
    (0, 5): 3,
    (0, 6): 3,
    (5, 0): 4,
    (0, 4): 6,
    (6, 0): 5,
    (3, 2): 1,
    (4, 2): 1,
    (5, 2): 1,
    (2, 1): 6,
    (4, 1): 3,
    (3, 5): 1,
    (3, 1): 6,
    (5, 1): 4,
    (4, 6): 1,
    (6, 1): 5,
    (4, 3): 2,
    (5, 3): 2,
    (3, 6): 2,
    (4, 5): 2,
    (6, 4): 2,
    (6, 2): 5,
    (5, 4): 3,
    (6, 3): 4,
    (5, 6): 3,
    (6, 5): 4}
print(len(ma))


def choose(a: List[int], cnt: int):
    # 给定数组a，从中选择cnt个元素
    ans = []

    def go(ind, b):
        if len(b) == cnt:
            ans.append(b[:])
            return
        if ind >= len(a):
            return
        b.append(a[ind])
        go(ind + 1, b)
        b.pop()
        go(ind + 1, b)

    go(0, [])
    return ans


a = choose(list(range(7)), 3)
a = [tuple(i) for i in a]
b = []
for x, y in ma.items():
    z = list(x) + [y]
    z.sort()
    b.append(tuple(z))
a.sort()
b.sort()
print(a == b)
