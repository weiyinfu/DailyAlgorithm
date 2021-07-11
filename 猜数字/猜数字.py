"""

从52个数字中随机选择5个，你从中选择4个依次示人，让别人猜测剩余一个数字。

是否存在一个算法，你和别人的合作总是能够成功。

首先，5张牌4种花色，至少有一种花色有两张，取此花色放在4、5位置处。
其次，根据4可以推测出5的花色。
根据前三张牌的顺序可以确定1~6，6种数字。
4的数字和5的数字相差不会超过6.所以，直接用4加上前三张牌的顺序数就得到第5张牌的数字。

这种思路可以说是无敌巧妙。

随意给你5个数字，你可以选择其中的4个数字进行展示（一次性展示出来），展示之后让别人猜测你手中剩余牌的奇偶性。


如果是无序展示，则必须(k-1)!>=n-k+1才能保证有解。


我最初的思路：4张牌可以决定24种，只需要再确定一个奇偶性就可以了。给你5张牌，从中选出4张牌无序示人，令人猜测剩余牌的奇偶性。这种思路是错的。
"""
import itertools
import logging

import numpy as np


def generate(n, k):
    # 从0到n之间随机选择k个数字
    a = np.arange(n)
    np.random.shuffle(a)
    return a[:k]


def num2ind(n: int, a: int):
    b = list(itertools.permutations(list(range(n))))
    return b[a]


def ind2num(a):
    b = list(itertools.permutations(list(range(len(a)))))
    for ind, i in enumerate(b):
        if np.all(i == a):
            return ind
    raise Exception("error")


class Solver:
    def __init__(self):
        pass

    def encode(self, a):
        a = np.array(a)
        b = a // 13
        res = np.bincount(b)
        res = np.pad(res, (0, 4 - len(res)))
        a = list(a)
        a.sort(key=lambda x: (res[x // 13], x // 13))
        a = [(i, i % 13) for i in a]
        if (a[-1][1] + 13 - a[-2][1]) % 13 > 6:
            a[-2], a[-1] = a[-1], a[-2]
        else:
            pass
        lack = (a[-1][1] + 13 - a[-2][1]) % 13
        if lack > 6:
            logging.info(f"lack={lack} a[-1]={a[-1]} a[-2]={a[-2]}")
            raise Exception("asdf")
        pre = [a[i][0] for i in range(3)]
        pre.sort()
        ind = num2ind(3, lack - 1)
        logging.info(f"encode a={a} lack={lack} ind={ind}")
        x = [pre[i] for i in ind] + [a[-2][0]]
        return x, a[-1][0]

    def decode(self, a):
        a = np.array(a)
        b = a[:3]
        ind = np.argsort(b)
        ind = np.argsort(ind)
        add = ind2num(ind) + 1
        color = a[-1] // 13
        value = (a[-1] + add) % 13
        logging.info(f"decode add={add} ind={ind} color={color} value={value}")
        return color * 13 + value

    def test(self, a):
        x, y = self.encode(a)
        yy = self.decode(x)
        logging.info(f"a={a} x={x} y={y} yy={yy}")
        return y == yy


def test_num2ind():
    for i in range(6):
        ind = num2ind(3, i)
        num = ind2num(ind)
        print(i, ind, num)


# logging.root.level = logging.INFO


def test_many():
    s = Solver()
    for i in range(100000):
        p = generate(52, 5)
        logging.info(f"problem={p}")
        res = s.test(p)
        if not res:
            exit(-1)


def test_one():
    p = [45, 9, 42, 3, 20]
    s = Solver()
    print(s.test(p))


# test_one()
test_many()
