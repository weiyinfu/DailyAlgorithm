from kv4py import lib
from kv4py import binary_tree_viewer
import numpy as np

t = lib.BinaryTree()
binary_tree_viewer.main(t, np.random.randint(0, 30, 10), False)
