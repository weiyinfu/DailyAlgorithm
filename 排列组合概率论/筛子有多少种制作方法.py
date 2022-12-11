"""
骰子有6个面，要求13，24，56两两相对，问有多少种制作方法。

首先筛子有24种放置方法，现在用六种颜色为它涂色，只涂上前右三个面。
上面有6种，前面有4种，右面有2种，所以一共有48种涂色方案，除以24种放置方法，只有两种等价类。
"""
import numpy as np


def rotate(a, face):
    b = np.array(a).copy()
    for i in range(len(face)):
        b[face[i]] = a[face[(i + 1) % len(face)]]
    return b


def down(a):
    return rotate(a, [0, 2, 4, 5])


def right(a):
    return rotate(a, face=[1, 2, 3, 5])


def hash(a):
    q = [a]
    had = set()
    i = 0

    def push(x):
        x = tuple(x)
        if x not in had:
            had.add(tuple(x))
            q.append(x)

    while i < len(q):
        now = q[i]
        push(right(now))
        push(down(now))
        i += 1
    q.sort()
    return tuple(q[0])


def get_another(x):
    a = [(0, 4), (1, 3), (2, 5)]
    b = {}
    for k, v in a:
        b[k] = v
        b[v] = k
    return b[x]


def match(a):
    for i in range(3):
        if a[get_another(i)] != get_another(a[i]):
            return False
    return True


from itertools import permutations

a = np.arange(6)
cnt = 0
total = set()
for i in permutations(a):
    if not match(i):
        continue
    cnt += 1
    total.add(hash(i))
print('全部', cnt)
print(len(total))
