
"""
一道非常难的映射找规律题目：来自leetcode
"""
N = 1000
f = [-1] * N
q = [0]
f[0] = 0


def lowbit(x):
    return x & (-x)


def push(x, now):
    if x < N:
        if f[x] == -1:
            f[x] = f[now] + 1
            q.append(x)


while q:
    now = q.pop(0)
    x = now ^ 1
    push(x, now)
    y = (lowbit(now) << 1) ^ now
    push(y, now)
f = f[:100]

print(f)

import math


def get(b, e, n, ord):
    print(f"begin={b} end={e} which={n}")
    if b == e:
        return b
    m = (b + e) // 2
    first = (b, m)
    second = (m + 1, e)
    if n >= (e - b + 1) // 2:
        nex = not ord
        next_n = n - (e - b + 1) // 2
        if ord:
            use = second
        else:
            use = first
    else:
        nex = ord
        next_n = n
        if ord:
            use = first
        else:
            use = second
    return get(use[0], use[1], next_n, nex)


def solve(n):
    if n <= 1:
        return n
    bit = int(math.floor(math.log2(n)))
    return get(2 ** bit, 2 ** (bit + 1) - 1, n - 2 ** bit, False)


for i in range(len(f)):
    print(i, f[i],solve(i))
# print(solve(5))
