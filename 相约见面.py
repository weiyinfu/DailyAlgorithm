import numpy as np

"""
n个人相约在1点到2点之间见面，每个人等待20分钟，问这n个人能相遇的概率是多少。
"""
n = 3
a = np.random.random((100000, 2))
delta = np.max(a, axis=1) - np.min(a, axis=1)
print(delta.shape)
print(np.count_nonzero(delta < 1 / 3) / len(a))
print(5 / 9)
