class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def __repr__(self):
        s = (self.value, self.left, self.right)
        return str(s)


def build(pre, mid):
    if len(mid) == 0:
        return None
    i = 0
    while mid[i] != pre[0]:
        i += 1
    no = Node(pre[0])
    no.left = build(pre[1:1 + i], mid[:i])
    no.right = build(pre[i + 1:], mid[i + 1:])
    return no


def main():
    pre = [3, 9, 20, 15, 7]
    mid = [9, 3, 15, 20, 7]
    node = build(pre, mid)
    print(node)


main()
"""
3
|--9
|--20
    |---15
    |---7
"""