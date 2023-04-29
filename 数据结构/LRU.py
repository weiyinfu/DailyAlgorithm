import random
from tqdm.autonotebook import tqdm
from collections import OrderedDict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"({self.key},{self.value})"


class LinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = self.head
        self.sz = 0

    def append(self, node):
        self.sz += 1
        self.tail.next = node
        node.next = None
        node.prev = self.tail
        self.tail = node

    def remove(self, node):
        self.sz -= 1
        if node == self.tail:
            self.tail = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def size(self):
        return self.sz

    def remove_head(self):
        if self.sz == 0:
            raise Exception("no element")
        self.head = self.head.next
        self.sz -= 1
        return self.head

    def __repr__(self):
        a = []
        i = self.head.next
        while i:
            a.append(str(i))
            i = i.next
        return 'Link{' + ','.join(a) + "}"


class Lru:
    def __init__(self, n, io):
        self.ma = {}
        self.link = LinkedList()
        self.n = n
        assert n > 0, 'too little size'
        self.io = io

    def get(self, k):
        if k in self.ma:
            node = self.ma[k]
            self.link.remove(node)
            self.link.append(node)
            return node.value
        else:
            value = self.io.get(k)
            node = Node(k, value)
            self.link.append(node)
            self.ma[k] = node
            while self.link.size() > self.n:
                no = self.link.remove_head()
                del self.ma[no.key]
            return value

    def __str__(self):
        return str(self.link)


class LruByOrderedDict:
    """
    利用python内置对象orderedDict实现LRU
    """

    def __init__(self, n, io):
        self.a = OrderedDict()
        self.n = n
        self.io = io

    def get(self, k):
        if k in self.a:
            v = self.a[k]
            del self.a[k]
            self.a[k] = v
            return v
        else:
            value = self.io.get(k)
            self.a[k] = value
            if len(self.a) > self.n:
                self.a.popitem(last=False)
            return value


def test():
    class Io:
        def get(self, k):
            return str(k) + 'value'

    y = Io()
    for x in (Lru(2, y), LruByOrderedDict(2, y)):
        random.seed(0)
        for i in tqdm(range(1000)):
            k = random.randint(0, 10)
            value = x.get(k)
            if value != y.get(k):
                print(k, value, y.get(k))
                assert False
            print('get', k, value)
            print(x)


test()
