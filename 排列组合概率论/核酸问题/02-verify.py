"""
验证最终的答案：
24个人阳性，1000个人，问有13管阳性的概率是多少？
预测是：0.1611802577972412


这种做法是错误的。
"""

import numpy as np
from tqdm import tqdm


def get(a):
    # 进行一次实验
    b = np.reshape(a, (100, 10))
    c = b.sum(axis=1)
    return int(np.count_nonzero(c))


def go(n):
    s = [0] * 101
    a = np.zeros(1000)
    a[:24] = 1
    for _ in tqdm(range(n)):
        np.random.shuffle(a)
        s[get(a)] += 1
    print(s)
    return s[13] * 1.0 / n


print(go(200000))
