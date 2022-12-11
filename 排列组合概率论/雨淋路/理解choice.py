import random
import numpy as np

"""
不管是random.choices还是np.random.choice都是多次选择，每次随机选择一个，而不是一次性随机选择多个
"""
a = np.arange(5)
for i in range(10):
    print(random.choices(a, k=3))
print('=' * 10)
for i in range(10):
    print(np.random.choice(a, 3))
