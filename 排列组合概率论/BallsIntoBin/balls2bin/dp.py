import math

from scipy.special import comb

"""
动态规划算法：
n个不同的球放入m个不同的箱子，总的方案数为n^m

定义f(n,m,k)为球最多的箱子球数为k的方案数。则最终答案为
ans=\sum_{1}^{m} f(n,m,k)/(n^m)*k

关键在于求f(n,m,k)，把n个球放入m个箱子，球最多的箱子球数为k。

"""

ma = {}


def f(n, m, k):
    if n == 0 and m == 0:
        if k == 0:
            return 1
        else:
            return 0
    if k > n:
        return 0
    if m == 0:
        if k > 0:
            return 0
        return 1
    if k < math.ceil(n / m):
        return 0
    kk = (n, m, k)
    if kk in ma:
        return ma[kk]
    s = 0
    # 最后一个箱子不够k个，只有i个；前面的箱子够k个
    for i in range(k):
        if i > n:
            break
        s += comb(n, i) * f(n - i, m - 1, k)
    # 最后一个箱子够k个，其它箱子随意；枚举其它箱子中最多球数
    if k <= n:
        for i in range(k + 1):
            s += f(n - k, m - 1, i) * comb(n, k)
    ma[kk] = s
    return s


def solve(n, m):
    s = 0
    for i in range(n + 1):
        s += i * f(n, m, i) / (m ** n)
    return s
