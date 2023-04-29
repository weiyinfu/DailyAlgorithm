import numpy as np

"""
期望随机选择多少个(0,1)随机数，才能使得总和大于1.
答案是e。 
"""


def get(n, s):
    a = np.random.uniform(0, 1, (10000, n))
    b = np.sum(a, axis=1)
    ans = np.count_nonzero(b > s) / len(b)
    return ans


def main():
    s = 0
    ans = 0
    for i in range(100):
        p = get(i, 1) - s
        s += p
        ans += i * p
    print(ans)


main()
