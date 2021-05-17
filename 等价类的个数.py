from collections import Counter

import numpy as np
"""
求非置换群的等价类，只能使用dfs或者并查集。

求置换群的等价类，则可以使用伯恩赛德定理。伯恩赛德定理的使用前提是：全部变换构成置换群。如果变换无法形成置换群，使用伯恩赛德定理是错误的。
"""

def get_problem(n=4):
    a = np.arange(n)
    np.random.shuffle(a)
    return a


def get_ring(s):
    # 并查集方法求等价类
    fa = [-1] * len(s)

    def find(x):
        if fa[x] == -1:
            return x
        f = find(fa[x])
        fa[x] = f
        return f

    for i in range(len(s)):
        fx = find(i)
        fy = find(s[i])
        if fx != fy:
            fa[fx] = fy
    fa = [find(i) for i in range(len(s))]
    return len(Counter(fa).values())


def get_ring3(a):
    s = 0
    vis = set()

    def dfs(x):
        if x in vis:
            return 0
        vis.add(x)
        return 1 + dfs(a[x])

    for i in range(len(a)):
        s += 1 if dfs(a[i]) else 0
    return s


def main():
    for _ in range(100):
        a = get_problem()
        print(get_ring(a), get_ring3(a), a)


if __name__ == '__main__':
    main()
