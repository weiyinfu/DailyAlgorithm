import numpy as np

"""
袋子里面有n个球，有放回摸球，期望摸多少次才能把所有球至少摸一遍。
答案是：n*(1/1+1/2+1/3+...+1/n)
"""


def solve2(n):
    return sum(n / i for i in range(1, n + 1))


def solve3(n):
    # 残差为O(1/n)，这个表达式是1+1/2+1/3+...+1/n的逼近
    return n * np.log(n) + n * 0.5772 + 0.5


def solve(n):
    def go():
        a = np.zeros(n, dtype=bool)
        times = 0
        while np.count_nonzero(a) != len(a):
            a[np.random.randint(0, len(a))] = True
            times += 1
        return times

    return np.mean([go() for _ in range(1000)])


for n in np.arange(100, 200, 2):
    ans = []
    for f in (solve2, solve3):
        ans.append(f(n))
    print(ans)
    assert np.std(ans) < 0.001
