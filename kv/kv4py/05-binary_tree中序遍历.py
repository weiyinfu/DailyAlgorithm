import numpy as np
from kv4py.lib import BinaryTree, mid_order

x = BinaryTree()
for i in range(10):
    k = np.random.randint(0, 10)
    x.insert(k, k)
mid_order(x.root)
print()
print(x.get(8))
