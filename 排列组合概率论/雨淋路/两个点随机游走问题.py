"""
一个A点，一个B点，一个C点
A->B p2
A->A p1
A->C p3

在A点已经走了ga步，求到达B点的期望步数。

这是一道数学题，是有放回摸球每次摸m个问题的核心变换。

是DAG随机游走问题的核心问题。
"""
import numpy as np


def go(ga, p1, p2):
    steps = ga
    while 1:
        x = np.random.random()
        steps += 1
        if x < p1:
            continue
        elif x > p2 + p1:
            break
        else:
            return steps
    return None


a = []
ga, p1, p2 = 3, 0.1, 0.2
for i in range(10000):
    res = go(ga, p1, p2)
    if res is None:
        continue
    a.append(res)


def real_ans(ga, p1, p2):
    p = p2 / (1 - p1)
    s = p2 / (1 - p1) ** 2
    return (p * ga + s) / p


def real_ans3(ga, p1, p2):
    return ga + 1 / (1 - p1)


def real_ans2(ga, p1, p2):
    s = 0
    pp = 0
    for i in range(1, 10000):
        pp += p1 ** (i - 1) * p2
        s += p1 ** (i - 1) * p2 * (ga + i)
    return s / pp


print(np.mean(a), real_ans(ga, p1, p2), real_ans2(ga, p1, p2), real_ans3(ga, p1, p2))
