"""
n个相同的球放入m个不同的盒子，每个盒子最多k个球，最少可以为空，有多少种方法？

13个相同的球随机放入100个不同的盒子，每个盒子最多10个球，最少可以为空。这13个球恰好占据13个盒子的概率是多少？

0.478672
0.397526


这种思路的错误之处在于：

2个球放入3个盒子，一共有6种情况：
002
011
020
101
110
200

其中2个球在一个盒子里面和2个球在两个盒子里面的情况个数是相同的，都是3.
但是2个球在一个盒子里面这件事发生的概率为1/3，2个球在不同盒子里面的概率为2/3。

不能用情况作为事情发生的概率。
"""
from scipy.special import comb
import numpy as np

ma = {}


def f(n, m, k):
    kk = (n, m, k)
    if kk in ma:
        return ma[kk]
    if n == 0:
        return 1
    if m == 0:
        return 0
    ans = 0
    for i in range(min(k + 1, n + 1)):
        ans += f(n - i, m - 1, k)
    ma[kk] = ans
    return ans


def g(n, m, k, t):
    # n个球放入m个盒子，每个盒子最多有k个球，不为空的盒子数恰好为t
    kk = (n, m, k, t)
    if kk in ma:
        return ma[kk]
    if n == 0:
        return 1 if t == 0 else 0
    if m == 0:
        return 0
    ans = 0
    for i in range(min(k + 1, n + 1)):
        ans += g(n - i, m - 1, k, t - 1 if i else t)
    ma[kk] = ans
    return ans


def solve(bad):
    """
    如果有
    """
    up = g(bad, 100, 10, 13)
    down = f(bad, 100, 10)
    print(up, down)
    return up / down


def can_empty(n, m):
    print("can empty")
    return comb(n + m - 1, m - 1, exact=True)


def why1():
    ans = f(13, 100, 12)
    print(can_empty(13, 100))
    print(ans)


def bru(x, n=100000):
    # x个人是阳性的时候,有sick_count管是阳性的概率
    s = [0] * (x + 1)
    a = np.zeros(1000)
    a[:x] = 1
    for _ in range(n):
        np.random.shuffle(a)
        b = np.reshape(a, (100, 10))
        c = b.sum(axis=1)
        d = int(np.count_nonzero(c))
        s[d] += 1
    return (np.array(s) / np.sum(s)).tolist()


def why2():
    ans = [0] * 20
    sick_count = 2
    for i in range(14):
        ans[i] = g(sick_count, 100, 10, i)
    print(ans)
    print(sum(ans))
    print(f(sick_count, 100, 10))
    s = f(sick_count, 100, 10)
    print([i / s for i in ans])
    print(bru(sick_count))


def why3():
    print(g(2, 3, 10, 2))


# print(solve(13))
why3()
