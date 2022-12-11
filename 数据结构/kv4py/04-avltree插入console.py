from kv4py import console_tree_view
from kv4py import lib

t = lib.Avl()

n = 4
for i in range(1, n):
    t.insert(i, i)
    print(console_tree_view.binary_tree_view(t.root, indent_unit=2))
    print('====')

for i in range(1, n):
    print('removing', t.root.key)
    print(console_tree_view.binary_tree_view(t.root, indent_unit=2))
    assert t.remove(t.root.key)
    print(console_tree_view.binary_tree_view(t.root, indent_unit=2))
    print('====')
