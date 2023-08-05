"""
查询区间min、max等。
sum和异或和可以通过前缀和进行处理，min、max却无法通过前缀和进行处理。


区间最值查询问题，即RMQ（Range Minimum/Maximum Query）

常见解法有朴素算法——O(n)预处理、O(n)查询，总体复杂度O(n+nq)

线段树——O(nlogn)预处理、O(logn)查询，总体复杂度O((n+q)logn)

ST算法——O(nlogn)预处理、O(1)查询，总体复杂度O(nlogn+q)

ST算法的查询为什么可以是O(1)呢？ 直接min(dp[f][dis],dp[t-dis/2][dis])
"""
import math

import numpy as np


class Brute:
    def __init__(self, p):
        self.p = p

    def solve(self, f, t):
        s = self.p[f]
        for i in range(f, t + 1):
            s = min(s, self.p[i])
        return s


class ST:
    def __init__(self, p):
        self.p = p
        self.ta = [[0] * 32 for _ in range(len(p))]
        for i in range(len(p)):
            self.ta[i][0] = p[i]
        for i in range(1, 32):
            for j in range(len(p)):
                self.ta[j][i] = min(self.ta[j][i - 1], self.ta[min(j + int(2 ** (i - 1)), len(p) - 1)][i - 1])

    def solve_slow(self, f, t):
        ans = self.p[f]
        while f != t + 1:
            dis = int(math.log(t - f + 1, 2))
            ans = min(ans, self.ta[f][dis])
            f += 2 ** dis
        return ans

    def solve(self, f, t):
        dis = int(math.log(t - f + 1, 2))
        return min(self.ta[f][dis], self.ta[t + 1 - 2 ** dis][dis])


def main():
    np.random.seed(0)
    p = np.random.randint(0, 1000, 1000)
    q = np.random.randint(0, len(p), (len(p) // 2, 2))
    q = np.vstack([np.min(q, axis=1), np.max(q, axis=1)]).T
    solver = [Brute(p), ST(p)]
    for f, t in q:
        ans = []
        for i in solver:
            ans.append(i.solve(f, t))
        if len(set(ans)) != 1:
            print(f"query {f} {t}", ans)
            print("error")
            break
    print('pass')


main()
