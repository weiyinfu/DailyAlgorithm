from kv4py.lib import SkipList


def get_value(k):
    return str(k) + "value"


x = SkipList()
a = [int(i) for i in "8 8 6 2 8 7 2 1 5 4 4 5 7 3 6 4 3 7 6 1 3 5 8 4 6 3 9 2 0 4 2 4 1 7 8 2 9 8 7 1".split()]
op = [int(i) for i in "2 0 2 1 1 1 1 2 0 2 2 0 0 2 2 0 0 2 2 0 2 0 1 2 1 2 2 2 0 2 1 0 0 1 1 2 1 1 1 1".split()]
for i, o in zip(a, op):
    print('插入 获取 删除'.split()[o], i)
    if o == 0:
        x.insert(i, get_value(i))
    elif o == 1:
        print(x.get(i))
    elif o == 2:
        x.remove(i)
    print(x)
