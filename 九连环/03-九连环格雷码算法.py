import math

"""
使用格雷码求解九连环
"""


def grey(n):
    return n ^ (n >> 1)


def solve(a):
    n = int(''.join(str(i) for i in a), base=2)
    ans = []
    current = 2 ** len(a) - 1 - n
    while a.count(0) < len(a):
        nex = current + 1
        v = grey(current) ^ grey(nex)
        op = int(math.log2(v))
        a[op] = 1 - a[op]
        ans.append(op + 1)
        current = nex
    return ans


ans = solve([1] * 9)
print(len(ans))
print(solve([1] * 6))
