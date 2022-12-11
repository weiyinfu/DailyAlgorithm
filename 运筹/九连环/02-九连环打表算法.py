from typing import Tuple

import numpy as np


def flip(a, ind):
    nex = np.copy(a)
    nex[ind] = 1 - nex[ind]
    return nex


def get(a):
    # 获取一个结点所能到达的其它节点
    ans = []
    for i in range(len(a) - 1):
        if a[i] == 1:
            ans.append((flip(a, i + 1), i + 1))
            break
    ans.append((flip(a, 0), 0))
    return ans


def build_graph(n: int):
    # 给定一个n，生成一个图
    a = np.ones(n, dtype=np.int)
    q = [a]
    g = {}
    i = 0
    while i < len(q):
        now = q[i]
        i += 1
        nex = get(now)
        g[tuple(now)] = [(tuple(j), op) for j, op in nex]
        for j, op in nex:
            jj = tuple(j)
            if jj not in g:
                q.append(j)
    return g


def build_table(n: int, target: Tuple):
    # 给定一个n，生成每个结点的最优操作路径，目标是到达target。使用广度优先方法进行搜索
    table = {target: []}
    g = build_graph(n)
    q = [target]
    i = 0
    while i < len(q):
        now = q[i]
        i += 1
        for nex, op in g[now]:
            if nex not in table:
                table[nex] = table[now] + [op + 1]
                q.append(nex)
    for k, v in table.items():
        table[k] = v[::-1]
    return table


def solve(a, build=False):
    """
    解决一个谜题
    :param a: 谜题数组
    :param build: 是想组装还是想拆开，如果是想组装，则build=True，target为全1；如果build=False，target为全0
    :return:
    """
    target = tuple([1] * len(a) if build else [0] * len(a))
    table = build_table(len(a), target)
    return table[tuple(a)]


def max_steps():
    # 打印N连环最优解所需要的步数
    for i in range(1, 20):
        print(i, len(solve([1] * i)))


def solve_problem():
    print(len(solve([1] * 9)))
    ans = solve([0, 0, 0, 1, 1, 1, 1, 1, 1])
    for i in range(0, len(ans), 5):
        print(ans[i:i + 5])


def grey(n):
    return n ^ (n >> 1)


def print_path(n):
    ans = solve([1] * n)
    a = [1] * n
    x = (1 << n) - 1
    for ind, i in enumerate(ans):
        a[i - 1] = 1 - a[i - 1]
        x ^= 1 << (i - 1)
        g = grey(len(ans) - 1 - ind)
        print(a, bin(x), bin(g))


print_path(6)
