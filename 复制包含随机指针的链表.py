import random

"""
链表复制，链表结点有随机指针
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None


def get_problem(n=10):
    a = []
    for i in range(n):
        no = Node(i)
        a.append(no)
    for i in range(0, len(a) - 1):
        a[i].next = a[i + 1]
    for i in range(len(a)):
        a[i].rand = a[random.randint(0, len(a) - 1)]
    return a[0]


def copy(no: Node):
    root = Node(no.val)
    up = no
    down = root
    # copy single link
    while up.next:
        down.next = Node(up.next.val)
        down = down.next
        up = up.next
    up = no
    down = root
    # insert old link to new link
    while up:
        down.rand = up.rand
        up.rand = down
        down = down.next
        up = up.next
    up = no
    down = root
    # update down.next as down.rand
    while up:
        nex = down.next
        down.next = down.rand.rand
        down = nex
        up = up.next
    up = no
    down = root
    while up:
        up_rand = down.rand
        down_rand = down.next
        down_next = up.next.rand if up.next else None
        up.rand = up_rand
        down.next = down_next
        down.rand = down_rand
        up = up.next
        down = down.next
    return root


def show_link(head):
    a = []
    while head:
        a.append(head)
        head = head.next
    b = []
    for i in a:
        b.append((i.val, i.rand.val))
    print(b)


p = get_problem(10)
show_link(p)
q = copy(p)
show_link(p)
show_link(q)
