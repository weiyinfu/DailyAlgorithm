"""
x个阳性在1000人里面恰好分在13个管子里面的概率

0.478672
0.397526
"""

import numpy as np
from scipy.special import comb
from tqdm import tqdm

ma = {}


def dp(sick_people, total_pipe, k, bad_pipe):
    # n个球放入m个盒子，每个盒子最多有k个球，不为空的盒子数恰好为t
    kk = (sick_people, total_pipe, k, bad_pipe)
    if kk in ma:
        return ma[kk]
    if sick_people == 0:
        return 1 if bad_pipe == 0 else 0
    if total_pipe == 0:
        return 0
    ans = 0
    for i in range(min(k + 1, sick_people + 1)):
        ans += dp(sick_people - i, total_pipe - 1, k, bad_pipe - 1 if i else bad_pipe) * comb(sick_people, i) * comb(k * total_pipe - sick_people, k - i) / comb(k * total_pipe, k)
    ma[kk] = ans
    return ans


def bruteforce(sick_people, total_pipe, k, bad_pipe, n=100000):
    # x个人是阳性的时候,有sick_count管是阳性的概率
    s = [0] * (total_pipe + 1)
    a = np.zeros(k * total_pipe)
    a[:sick_people] = 1
    for _ in range(n):
        np.random.shuffle(a)
        b = np.reshape(a, (total_pipe, k))
        c = b.sum(axis=1)
        d = int(np.count_nonzero(c))
        s[d] += 1
    return s[bad_pipe] * 1.0 / n


def smart(bad_pipe, n=100):
    # 指数方法计算sick管阳性时，预期有多少人阳性
    x = (1 - bad_pipe / n) ** (1 / 10)
    return 1000 * (1 - x)


def find(bad_pipe):
    ans = []
    remind = int(smart(bad_pipe))
    for i in range(remind - 5, remind + 5):
        ans.append((i, dp(i, 100, 10, bad_pipe)))
    ma = ans[0]
    for i in ans:
        if ma[1] < i[1]:
            ma = i
    return ma


def main():
    for i in tqdm(range(1, 100)):
        x = smart(i)
        y = find(i)
        if int(x) != y[0]:
            print("找到了====")
        print(i, x, y)


def why():
    n = int(10000000)
    print(bruteforce(53, 100, 10, 42, n=n))
    print(bruteforce(52, 100, 10, 42, n=n))
    # print(dp(53, 100, 10, 42))
    # print(dp(52, 100, 10, 42))


# main()
why()
# print(find(100))
