import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

"""
长为1m的路，半径为1cm的雨滴，雨滴在路上随机分布，问多少个雨滴才能把路淋湿？
答案应该在725附近。

关于这个问题，某剑桥大学数学博士给出了一种解法，见文档road_problem.
"""


def model_solve(n, m, ratio=10, times=1000):
    """
    使用蒙特卡洛方法求解此问题
    :param n:
    :param m:
    :param ratio:
    :return:
    """

    def go():
        # 路的长度为n，雨滴宽度为m,ratio表示一个雨滴的离散化长度
        nonlocal n, m
        n = n / (m / ratio)
        n = int(n)
        m = int(ratio)
        a = np.zeros(n, dtype=np.bool)
        drop = 0
        while np.count_nonzero(a) < n:
            x = np.random.randint(0, n)
            beg = x - m // 2
            end = x + m // 2
            end = min(n, end)
            beg = max(0, beg)
            a[beg:end] = True
            drop += 1
        return drop

    ans = [go() for _ in tqdm(range(times))]
    mu = np.mean(ans)
    sigma = np.std(ans)
    print(f"mu={mu} sigma={sigma}")
    plt.hist(ans, bins=100)
    plt.show()
    return mu


print(model_solve(1, 0.01, ratio=100, times=1000))
