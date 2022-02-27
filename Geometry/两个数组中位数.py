import numpy as np

n = np.random.randint(3, 23)
a = np.random.randint(0, 100, n)
ind = np.random.randint(1, n - 1)
b, c = a[:ind], a[ind:]
b.sort()
c.sort()


def real(b, c):
    a = np.concatenate([b, c])
    a.sort()
    return a[len(a) // 2]


def solve(b, c):
    i = 0
    j = 0
    sz = len(b) + len(c)
    want = sz // 2
    while 1:
        lack = want - (i + j + 1)
        if lack == 0:
            break
        move = lack // 2
        if move == 0:
            move = 1
        ii = min(i + move, len(b) - 1)
        jj = min(j + move, len(c) - 1)
        if b[ii] < c[jj] and ii != i:
            i = ii
        else:
            j = jj
    return max(b[i], c[j])


print(solve(b, c), real(b, c))
