import numpy as np

"""
morris中序遍历是一种无需递归、不需要栈，但是需要对原树结构进行写操作的算法

这是巧妙至极的算法
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# np.random.seed(5)


def generate_tree():
    # 随机产生一个二叉树

    def insert(node: Node, value):
        if not node: return Node(value)
        if value > node.value:
            node.right = insert(node.right, value)
        else:
            node.left = insert(node.left, value)
        return node

    a = np.unique(np.random.randint(0, 30, 7))
    now = Node(15)
    np.random.shuffle(a)
    for i in a:
        insert(now, i)
    return now


def morris(root: Node):
    cur = root
    pre: Node = None
    while cur:
        if cur.left is None:
            print(cur.value, end=',')
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                print(cur.value, end=',')
                cur = cur.right
    print()


def print_tree(node: Node):
    def go(node: Node, padding: int):
        if not node: return
        print(' ' * padding, node.value)
        go(node.left, padding + 1)
        go(node.right, padding + 1)

    go(node, 0)


def mid_order(node: Node):
    sta = [(node, 0)]
    while sta:
        now, visited = sta.pop()
        if visited:
            print(now.value, end=',')
        else:
            now.right and sta.append((now.right, 0))
            sta.append((now, 1))
            now.left and sta.append((now.left, 0))
    print()


tree = generate_tree()
mid_order(tree)
morris(tree)
