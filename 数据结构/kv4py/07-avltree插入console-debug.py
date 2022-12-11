from kv4py import console_tree_view
from kv4py import lib

t = lib.Avl()
a = [1, 3, 2]
n = 10
for i in a:
    t.insert(i, i)
    print(console_tree_view.binary_tree_view(t.root, indent_unit=2))
    print('====')
