from collections import defaultdict
from itertools import permutations
from typing import List, Tuple

import numpy as np
import scipy.sparse as sparse
from scipy.optimize import linear_sum_assignment


def choose(a: List[int], cnt: int):
    # 给定数组a，从中选择cnt个元素
    ans = []

    def go(ind, b):
        if len(b) == cnt:
            ans.append(b[:])
            return
        if ind >= len(a):
            return
        b.append(a[ind])
        go(ind + 1, b)
        b.pop()
        go(ind + 1, b)

    go(0, [])
    return ans


def generate_rows(a: List[Tuple[Tuple, int]]):
    # 给定一个组合列表，展示k个求最后一个，无序
    rows = []
    for i in a:
        row = []
        for j in range(len(i)):
            x = tuple(i[:j] + i[j + 1:])
            y = i[j]
            row.append((x, y))
        rows.append(row)

    return rows


def generate_rows_permutate(a: List[List[int]]):
    # 给定一个组合列表，展示k个求最后一个，有序
    rows = []
    for i in a:
        row = []
        for j in range(len(i)):
            x = tuple(i[:j] + i[j + 1:])
            y = i[j]
            for xx in permutations(x):
                row.append((tuple(xx), y))
        rows.append(row)

    return rows


def can_guess(rows: List[List[Tuple[Tuple, int]]]):
    # 对于组合，暴力枚举结果
    def go(ma, ind):
        if ind == len(rows):
            return True
        for x, y in rows[ind]:
            if x in ma:
                continue
            ma[x] = y
            if go(ma, ind + 1):
                return True
            del ma[x]
        return False

    ma = {}
    ans = go(ma, 0)
    if ans:
        print(ma)
    return ans


def build_matrix(rows: List[List[Tuple]]):
    # 给定若干行，用矩阵表示，每行每列只能选择一个
    x2id = {}
    new_rows = []
    for row in rows:
        new_row = []
        for x, y in row:
            if x not in x2id:
                x2id[x] = len(x2id)
            new_row.append(x2id[x])
        new_rows.append(new_row)
    a = np.zeros((len(rows), len(x2id)))
    for x, y in enumerate(new_rows):
        a[x, y] = 1
    return a


def build_matrix_sparse(rows: List[List[Tuple]]):
    x2id = {}
    new_rows = []
    for row in rows:
        new_row = []
        for x, y in row:
            if x not in x2id:
                x2id[x] = len(x2id)
            new_row.append(x2id[x])
        new_rows.append(new_row)
    xs = []
    ys = []
    for x, yy in enumerate(new_rows):
        for y in yy:
            xs.append(x)
            ys.append(y)
    print(np.min(xs), np.max(xs), np.min(ys), np.max(ys))
    ans = sparse.csr_matrix((np.ones(len(xs)), (xs, ys)), shape=(len(rows), len(x2id)))
    return ans


def build_graph(rows: List[List]) -> List[List[int]]:
    # 返回一个图
    node2id = {}
    new_rows = []
    for row in rows:
        new_row = []
        for x, y in row:
            k = f"{x}=>{y}"
            if k not in node2id:
                node2id[k] = len(node2id)
            new_row.append(node2id[k])
        new_rows.append(new_row)
    x2id = defaultdict(lambda: [])
    for row in rows:
        for x, y in row:
            k = f"{x}=>{y}"
            id_ = node2id[k]
            x2id[x].append(id_)
    all_ids = set(node2id.values())
    # g表示每个结点不能去的地方
    g = [[] for i in all_ids]
    new_rows.extend(x2id.values())
    for row in new_rows:
        for i in range(len(row)):
            for j in range(i + 1):
                x, y = row[i], row[j]
                g[x].append(y)
                g[y].append(x)
    # 用all_ids减去不能去的地方，构建一个正经的图
    for i in range(len(g)):
        g[i] = list(all_ids - set(g[i]))
    return g


def bfs(g: List[List[int]]):
    # 广度优先求深度
    f = [-1] * len(g)
    q = [0]
    f[0] = 0
    i = 0
    while i < len(q):
        now = q[i]
        i += 1
        for to in g[now]:
            if f[to] != -1:
                continue
            f[to] = f[now] + 1
            q.append(to)
    return max(f)


def dfs(g: List[List[int]]):
    # 深度优先求深度
    ans = 0
    has = set()

    def go(x, depth):
        nonlocal ans
        ans = max(ans, depth)
        has.add(x)
        for i in g[x]:
            if i in has:
                continue
            has.add(i)
            go(i, depth + 1)

    go(0, 0)
    return ans


def slow_method():
    a = choose(list(range(8)), 3)
    print(len(a))
    rows = generate_rows_permutate(a)
    print(len(rows))
    print(can_guess(rows))


def error_method():
    # 尝试把问题归结为图，实际上并不是深度和广度
    a = choose(list(range(8)), 3)
    print('元素个数', len(a))
    rows = generate_rows_permutate(a)
    print('rows', len(rows))
    g = build_graph(rows)
    print('graph', len(g))
    print('每个结点的边数', len(g[0]))
    edge = bfs(g)
    print('bfs', edge)
    edge = dfs(g)
    print('dfs', edge)


def good_method():
    a = choose(list(range(8)), 3)
    print('元素个数', len(a))
    rows = generate_rows_permutate(a)
    print('rows', len(rows))
    g = build_matrix(rows)
    """
    g是一个矩阵
    把问题转化为矩阵，每行每列只能选择一个数字
    每行，每列构建结点，如果g[i][j]有边，则边的权重为1
    问题转化为二分图的最大匹配问题。
    """
    print(g.shape)
    print(np.count_nonzero(g, axis=0))
    x, y = linear_sum_assignment(g, maximize=True)
    ans = np.sum(g[x, y])
    print(ans)
    print('可解', ans == len(rows))


def hungary(g: sparse.csr_matrix):
    # scipy.optimize不支持稀疏矩阵，自己实现一个稀疏矩阵
    linker = [-1] * g.shape[1]
    ans = 0
    used = []

    def dfs(x):
        nonlocal used
        for v in g[x].indices:
            if not used[v]:
                used[v] = True
                if linker[v] == -1 or dfs(linker[v]):
                    linker[v] = x
                    return True
        return False

    for i in range(g.shape[0]):
        used = [False] * g.shape[1]
        if dfs(i):
            ans += 1
    return ans


def good_method_sparse():
    # scipy.optimize.linear_sum_assinment cannot use sparse matrix
    a = choose(list(range(27)), 4)
    print('元素个数', len(a))
    rows = generate_rows_permutate(a)
    print('rows', len(rows))
    g = build_matrix_sparse(rows)
    """
    g是一个矩阵
    把问题转化为矩阵，每行每列只能选择一个数字
    每行，每列构建结点，如果g[i][j]有边，则边的权重为1
    问题转化为二分图的最大匹配问题。
    """
    print(g.shape)
    ans = hungary(g)
    print(ans)
    print('可解', ans == len(rows))


# good_method_sparse()
good_method()
