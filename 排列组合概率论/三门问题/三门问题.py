import numpy as np
import random

"""
三门问题

一开始随机选中一个门的概率为1/3，后面如果不换，则中奖的概率一直是1/3。

如果换，则中奖的概率为1-1/3，等于2/3。
"""


def choose(a):
    return np.random.randint(0, len(a))


def generate():
    a = [0, 0, 1]
    random.shuffle(a)
    return a


def one():
    # 生成一个随机问题，返回不换门中奖的概率
    a = generate()
    # 让用户从中选择一个
    ind = choose(a)
    # 主持人随机推开一个空门
    empty = []
    for i, v in enumerate(a):
        if i == ind:
            continue
        elif v == 0:
            empty.append(i)
    # 主持人推开的门的下标
    rm = np.random.randint(0, len(empty))
    # 场上剩余的门
    left = [v for i, v in enumerate(a) if i != rm]

    # 不换门
    return a[ind]


def main():
    s = 0
    n = 10000
    for i in range(n):
        s += one()
    print('如果不换门的概率为', s / n)
    print('换门中奖的概率', 1 - s / n)


main()
