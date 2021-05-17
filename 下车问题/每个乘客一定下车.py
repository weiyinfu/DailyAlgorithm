import numpy as np
from tqdm import tqdm

N = 25
C = 10
"""
把N个球随机投入C个筐，求最终有球的筐的个数的期望？

这道题其实就是布隆过滤器，随机插入若干个元素之后，问有多少个bit为1
"""


def bruteforce(times=10000):
    def go():
        a = np.random.randint(0, C, N)
        a = np.unique(a)
        return len(a)

    return np.mean([go() for _ in tqdm(range(times))])


def smart():
    f = np.zeros(N + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, N + 1):
        f[i] = (f[i - 1] + 1) * (1 - f[i - 1] / C) + f[i - 1] / C * f[i - 1]
    return f[-1]


def best():
    return (1 - C) * (1 - 1 / C) ** (N - 1) + C


print(bruteforce())
print(smart())
print(best())
