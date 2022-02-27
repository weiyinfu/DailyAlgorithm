import numpy as np

"""
圆内随机选择n个点，这些点落在同一个半圆的概率是多少。
"""


def same(x: np.ndarray):
    x.sort()
    for i in range(len(x)):
        src, des = i, (i + 1) % len(x)
        dis = x[des] - x[src]
        if dis < 0:
            dis += np.pi * 2
        if dis >= np.pi:
            return True
    return False


def fast(k):
    return 2 * k / 2 ** k


def test(n, k):
    a = np.random.random((n, k)) * np.pi * 2
    b = np.zeros(len(a), dtype=np.bool)
    for i in range(len(a)):
        b[i] = same(a[i])
    ans = np.count_nonzero(b) / len(b)
    print(ans, fast(k))
    return ans


for i in range(3, 16):
    test(100000, i)
