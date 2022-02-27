from kv4py import binary_tree_viewer
from kv4py import lib

t = lib.Avl()

binary_tree_viewer.main(t, list(range(50)))
