"""
下车问题：
一辆机场大巴车从机场出发，载客25人，路径10个车站。每个乘客以相同的概率p=1/10在各个车站下车。若某站有客人要下车，则大巴在该站停车。每个客人下车的行为是互相独立的。设大巴停车次数为X，求X的数学期望。

情况一：每个乘客一定下车
情况二：每个乘客不一定下车

需要分类讨论给出每种答案。
f[n][c]=0人下车，1人下车，2人下车
"""
import numpy as np
from scipy.special import comb

N = 25
C = 10
P = 1 / 10
f = -np.ones((N + 1, C), dtype=np.float)


def solve(n, c):
    if c == C:
        return 0
    if n == 0:
        return 0
    if f[n][c] > 0:
        return f[n][c]
    s = 0
    for i in range(n + 1):
        # 当前站有i个人下车的概率
        s += (solve(n - i, c + 1) + (1 if i else 0)) * comb(n, i) * P ** i * (1 - P) ** (n - i)
    f[n][c] = s
    return s


ans = solve(N, 0)
print(ans)
