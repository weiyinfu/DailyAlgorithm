"""
给定一个n，构造一个图。
图中包括：
* 1个1度结点
* 2个2度结点
* 3个3度结点

要求这是一个连通图，且没有重边和环。
"""
n = int(input())
node_count = sum(range(1, n + 1))
a = [0] * node_count
target = []
for i in range(n):
    target.extend([i + 1] * (i + 1))
target = target[::-1]
ans = set()


def add(f, t):
    if (f, t) in ans:
        return
    ans.add((f, t))
    a[f] += 1
    a[t] += 1


j = 0
for i in range(node_count):
    if j <= i:
        j = i + 1
    while j < node_count and target[i] > a[i]:
        if a[j] < target[j]:
            add(i, j)
        j += 1
for i in range(node_count):
    j = i + 1
    while j < node_count and target[i] > a[i]:
        if a[j] < target[j]:
            add(i, j)
        j += 1


def output():
    s = []
    for f, t in ans:
        s.append(f"{f + 1} {t + 1}")
    print('\n'.join(s))


if a == target:
    output()
else:
    print(-1)
