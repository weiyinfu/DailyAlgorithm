from kv4py.lib import Avl
from kv4py import console_tree_view


def get_value(k):
    return str(k) + "value"


x = Avl()
a = [int(i) for i in
     "3 0 2 4 1 0 1 4 0 0 4 3 4 4 1 0 2 4 3 2 4 2 2 2 3 4 0 2 3 4 3 2 0 3 1 1 1 3 4 0 4 1 0 2 3 4 2 1 3 4".split()]
op = [int(i) for i in
      "0 2 0 0 0 2 0 0 0 0 0 2 2 2 2 2 0 0 2 0 2 2 2 2 2 2 2 2 0 2 2 0 2 2 2 2 2 2 2 0 2 2 2 2 0 2 2 2 0 0".split()]
for i, o in zip(a, op):
    print('插入 获取 删除 新建'.split()[o], i)
    if o == 0:
        x.insert(i, get_value(i))
    elif o == 1:
        print(x.get(i))
    elif o == 2:
        x.remove(i)
    elif o == 3:
        x = Avl()
    print(console_tree_view.binary_tree_view(x.root, indent_unit=2))
