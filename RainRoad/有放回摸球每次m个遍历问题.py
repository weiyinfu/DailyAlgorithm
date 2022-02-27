import numpy as np
from tqdm import tqdm
from scipy.special import comb

"""
袋子里面有n个球，有放回摸球，每次摸m个各不相同的球，期望摸多少次才能把所有球至少摸一遍？

100个球，有放回摸球每次摸5个各不相同的球，期望摸几把才能把所有球至少摸一遍？

期望摸102.51次
"""


def choose(n, cnt):
    # 从n个数字中随机选择cnt个数字
    a = np.arange(n)
    np.random.shuffle(a)
    return a[:cnt]


def wrong_solve(n, m, repeat=1000):
    # np.random.choice是每次摸到的求可能会有重复，这是不符合题意的。
    balls = np.arange(n)

    def go():
        a = np.zeros(n, dtype=bool)
        times = 0
        while np.count_nonzero(a) != len(a):
            a[np.random.choice(balls, m)] = True
            times += 1
        return times

    return np.mean([go() for _ in tqdm(range(repeat))])


def solve(n, m, repeat=1000):
    def go():
        a = np.zeros(n, dtype=bool)
        times = 0
        while np.count_nonzero(a) != len(a):
            a[choose(n, m)] = True
            times += 1
        return times

    return np.mean([go() for _ in tqdm(range(repeat))])


def c(n, m):
    return comb(n, m, exact=True)


def p(fetched, n, discover, m):
    """
    n个球每次摸m个，已经摸了fetched个，下一次摸摸到discover个新球的概率是多少
    :param fetched:
    :param n:
    :param discover:
    :param m:
    :return:
    """
    return c(n - fetched, discover) * c(fetched, m - discover) / c(n, m)


def solve2(n, m):
    """
    正向思路：当摸了k个球，摸到k+1个球需要付出多大的努力

    这种算法适用于所有的有向无环图随机游走问题，具有极其广泛的通用性。
    :param n:
    :param m:
    :return:
    """
    # f[x]表示拿了x个需要的步数
    f = np.ones(n + 1) * -1
    reach = np.zeros(n + 1)  # reach[x]表示到达x的概率
    f[0] = 0
    f[m] = 1
    reach[0] = 1
    reach[m] = 1

    for i in range(m + 1, n + 1):
        s = []
        for j in range(1, m + 1):
            if reach[i - j] == 0:
                continue
            p2 = p(i - j, n, j, m)  # 摸到j个新球的概率
            p1 = p(i - j, n, 0, m)  # 摸不到新球的概率
            pp = p2 / (1 - p1)  # 恰好从i-j摸到j个新球变成i的概率
            s.append([pp * reach[i - j], f[i - j] + 1 / (1 - p1)])
            reach[i] += reach[i - j] * pp
        up = 0
        down = 0
        for d, u in s:
            up += u * d
            down += d
        f[i] = up / down
    return f[-1]


def solve3(n, m):
    """
    逆向思路，当已经摸了n个球，距离目标还有多远？
    :param n:
    :param m:
    :return:
    """
    # f[x]表示已经拿了x个，剩余问题期望再拿f[x]次
    f = np.zeros(n + 1)
    f[n] = 0
    for i in range(n - 1, -1, -1):
        # f[x]=p0*(f[x]+1)+pi*(f[x+i]+1) x从1到m
        p0 = p(i, n, 0, m)
        s = sum([p(i, n, j, m) * (f[i + j] + 1) for j in range(1, m + 1) if i + j <= n])
        f[i] = (p0 + s) / (1 - p0)
    return f[0]


n = 15
m = 7
print(solve(n, m, repeat=1000))
# print(wrong_solve(n, m, repeat=1000))
print(solve2(n, m))
print(solve3(n, m))
