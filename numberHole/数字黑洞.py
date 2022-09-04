from collections import Counter
from tqdm import tqdm

"""
4位数6174，卡不列克常数
3位数495
"""
def go(x, n):
    a = list(str(x))
    a = ['0'] * (n - len(a)) + a
    a = sorted(a)
    v = int(''.join(a))
    vv = int(''.join(a[::-1]))
    return vv - v


def handle(x, n):
    last = 0
    for i in range(10000):
        if last == x:
            return x
        last = x
        x = go(x, n)
    return -1


def try_four():
    # 只要数字不全相同，则最终结果为6174
    ans = []
    for i in range(1000, 10000):
        ans.append(handle(i, 4))
    print(Counter(ans))


def try_three():
    ans = []
    for i in range(100, 1000):
        ans.append(handle(i, 3))
    print(Counter(ans))


def try_n(n):
    ans = []
    for i in tqdm(range(10 ** n, 10 ** (n + 1))):
        ans.append(handle(i, n + 1))
    print(Counter(ans))


try_four()
try_three()
try_n(3)
try_n(2)
try_n(1)
try_n(4)
