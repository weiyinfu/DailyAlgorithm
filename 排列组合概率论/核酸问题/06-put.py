"""
2个球随机放入3个盒子，有两个2盒子有球的概率是多少。

在一个盒子里面的概率为1/3

在两个盒子里面的概率为2/3
"""
import numpy as np


def brute():
    a = np.random.randint(0, 3, (100000, 2))
    b = a[:, 0] == a[:, 1]
    one = np.count_nonzero(b.reshape(-1))
    return 1 - one / len(a)


print(brute())
