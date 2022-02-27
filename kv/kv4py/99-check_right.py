import numpy as np
from tqdm import tqdm

from kv4py import lib


def get_value(k):
    return str(k) + "value"


n = 50000
import time

seed = int(time.time())
print(seed)
np.random.seed(seed)
a = np.random.randint(0, 5000, n)  # 操作数
op = np.random.randint(0, 3, n)  # 三种操作：插入、读取、删除、初始化
op[op == 1] = 2
coll_types = [
    lib.Dic,
    # lib.BinaryTree,
    # lib.SkipList,
    # lib.Avl,
    lib.Array,
    lib.LinkedList,
    lib.HashTable,
]
coll = [i() for i in coll_types]
verbose = False
print(a, op)
for i, o in zip(tqdm(a), op):
    if verbose:
        print('插入 获取 删除 初始化'.split()[o], i)
    if o == 0:
        # 插入
        for c in coll:
            c.insert(i, get_value(i))
    elif o == 1:
        # 获取
        values = set()
        for c in coll:
            values.add(c.get(i))
        if len(values) != 1:
            print(values)
            assert False
    elif o == 2:
        for c in coll:
            c.remove(i)
    elif o == 3:
        for c in range(len(coll_types)):
            coll[c] = coll_types[c]()
