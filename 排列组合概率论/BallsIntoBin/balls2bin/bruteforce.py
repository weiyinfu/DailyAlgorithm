from collections import Counter

import numpy as np


def solve(m, n):
    # 暴力算法，n个球放入m个箱子
    a = np.arange(m)
    times = 100000
    b = np.random.choice(a, (times, n))
    ans = np.zeros(n + 1, dtype=np.float32)
    for i in b:
        c = Counter(i).most_common(1)[0][1]
        ans[c] += 1
    ans = ans / times
    return np.dot(np.arange(len(ans)), ans)
