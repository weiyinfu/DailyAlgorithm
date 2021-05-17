from collections import defaultdict
from typing import List

"""
给定一个数组a，求它的所有子数组中，不同元素个数等于K的子数组的个数？
"""


class Ma:
    def __init__(self):
        self.ma = defaultdict(lambda: 0)
        self.cnt = 0

    def add(self, x):
        self.ma[x] += 1
        if self.ma[x] == 1:
            self.cnt += 1

    def remove(self, x):
        self.ma[x] -= 1
        if self.ma[x] == 0:
            self.cnt -= 1

    def get(self):
        return self.cnt


def solve(a: List[int], K):
    j = 0
    k = 0
    x = Ma()
    y = Ma()
    ans = 0
    for i in range(len(a)):
        x.add(a[i])
        y.add(a[i])
        while x.get() > K:
            x.remove(a[j])
            j += 1
        while y.get() >= K:
            y.remove(a[k])
            k += 1
        ans += k - j
    return ans


print(solve([1, 2, 3, 4, 5, 6], 3))
