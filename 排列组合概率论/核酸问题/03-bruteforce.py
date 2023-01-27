import numpy as np
from tqdm import tqdm

"""
使用暴力方法计算概率
"""


def solve(x, bad_pipe, n=100000):
    # x个人是阳性的时候,有sick_count管是阳性的概率
    s = [0] * 101
    a = np.zeros(1000)
    a[:x] = 1
    for _ in range(n):
        np.random.shuffle(a)
        b = np.reshape(a, (100, 10))
        c = b.sum(axis=1)
        d = int(np.count_nonzero(c))
        s[d] += 1
    return s[bad_pipe] * 1.0 / n


def main():
    a = []
    bad_pipe = 13
    for i in tqdm(range(bad_pipe, bad_pipe * 2)):
        a.append((i, solve(i, bad_pipe)))
    ma = a[0]
    print(a)
    for i in a:
        if i[1] > ma[1]:
            ma = i
    print(ma)


def why():
    n = 10000
    bad_pipe = 13
    print(solve(13, bad_pipe, n))
    print(solve(14, bad_pipe, n))


main()
# why()
