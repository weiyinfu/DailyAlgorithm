from collections import Counter
import numpy as np
from tqdm.autonotebook import tqdm
"""
给定一个数组，它里面全部元素都只出现了两次，只有两个元素出现了一次，请找出这两个元素，并按大小排序返回
"""


def generate():
    # 生成一个问题
    a = np.random.randint(0, 100, 40)
    a = np.unique(a)
    b = a[:2].tolist() + a[2:].tolist() + a[2:].tolist()
    np.random.shuffle(b)
    return b


def use_counter(nums):
    a = Counter(nums)
    ans = []
    for k, v in a.items():
        if v == 1:
            ans.append(k)
    ans.sort()
    return ans


def fatastic(a):
    x = 0
    for i in a:
        x ^= i
    lowbit = 1
    while not x & lowbit:
        lowbit <<= 1
    y = 0
    for i in a:
        if i & lowbit:
            y ^= i
    ans = [y, x ^ y]
    ans.sort()
    return ans


def test():
    for _ in tqdm(range(1000)):
        p = generate()
        ans = set()
        for f in (use_counter, fatastic):
            ans.add(tuple(f(p)))
        if len(ans) != 1:
            print('bad', ans)
            p.sort()
            print(p)


test()
