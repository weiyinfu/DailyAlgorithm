from collections import defaultdict

import sympy as sp


def standard(m, n):
    z = tuple([0] * m)
    q = [z]
    ma = defaultdict(lambda: 0)
    ma[z] = 1
    vis = set()
    vis.add(z)
    i = 0
    while i < len(q):
        now = q[i]
        now_p = ma[now]
        ss = sum(now)
        for j in range(m):
            nex = list(now)
            nex[j] += 1
            nex = tuple(nex)
            ma[nex] += now_p * 1 / m
            if ss < n:
                if nex not in vis:
                    vis.add(nex)
                    q.append(nex)
        i += 1
    ans = 0
    for pattern, count in ma.items():
        if sum(pattern) == n:
            ans += max(pattern) * count
    return ans


def standard2(m, n):
    # n个球放入m个盒子，使用sympy精确计算分数
    z = tuple([0] * m)
    q = [z]
    from collections import defaultdict
    ma = defaultdict(lambda: 0)
    ma[z] = 1
    vis = set()
    vis.add(z)
    i = 0
    while i < len(q):
        now = q[i]
        now_p = ma[now]
        ss = sum(now)
        for j in range(m):
            nex = list(now)
            nex[j] += 1
            nex = tuple(nex)
            ma[nex] = ma[nex] + now_p * sp.Rational(1, m)
            if ss < n:
                if nex not in vis:
                    vis.add(nex)
                    q.append(nex)
        i += 1
    ans = 0
    for pattern, count in ma.items():
        if sum(pattern) == n:
            ans += max(pattern) * count
    return ans
