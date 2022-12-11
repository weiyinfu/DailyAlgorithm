"""
哈希表扩容的时候，如果一次性复制到新表，会导致CPU占用过多，造成卡顿。
因此必须要缓慢地扫描旧哈希表，逐个把元素复制到新哈希表。
如何缓慢地扫描旧哈希表呢？新开一个线程？但是redis是单线程的。
那就把复制过程与增删改查操作关联起来。
当哈希表处于扩容状态时，设置一个index变量，初始值为0.每当增删改查时，让index+1，并且把旧哈希表中index处的元素复制到新哈希表。增删改查len(old)次旧哈希表就可以删除了。
"""


class Hash:
    def __init__(self, n: int):
        self.a = [[] for i in range(n)]
        self.index = -1
        self.used = 0
        self.b = []

    def update_a(self, a, k, v, only_add=False):
        found = False
        ind = hash(k) % len(a)
        for i in a[ind]:
            if i[0] == k:
                if not only_add:
                    i[1] = v
                found = True
                break
        if not found:
            a[ind].append([k, v])
        return found

    def tidy(self):
        while self.index != -1:
            self.slow_copy()

    def put(self, k, v):
        if self.index != -1:
            # 更新到新的里面去
            found = self.update_a(self.b, k, v)
            self.slow_copy()
        else:
            found = self.update_a(self.a, k, v)
        if not found:
            self.used += 1
            if self.index == -1 and self.used > len(self.a) // 2 - 3:
                # 需要扩容了
                self.b = [[] for _ in range(len(self.a) * 2)]
                self.index = 0
                self.used = 0
        return found

    def slow_copy(self):
        if self.index == -1:
            return
        for k, v in self.a[self.index]:
            if not self.update_a(self.b, k, v, only_add=True):
                self.used += 1
        self.index += 1
        if self.index == len(self.a):
            # copy结束
            self.index = -1
            self.a = self.b
            self.b = []

    def get(self, k):
        def go(a):
            ind = hash(k) % len(a)
            for i in a[ind]:
                if i[0] == k:
                    return i[1]
            return None

        if self.index == -1:
            # 处于非扩容状态
            ans = go(self.a)
        else:
            # 处于扩容状态
            ans = go(self.b)
            if ans is None:
                ans = go(self.a)
            self.slow_copy()
        return ans

    def show(self):
        print(f"Hash=====\n{self.a}\n{self.b}\nindex={self.index} used={self.used}\n====")


import numpy as np
from tqdm import tqdm

a = np.random.randint(0, 100, (30, 2))
ha = Hash(3)
ma = {}
for k, v in a:
    ha.put(k, v)
    ma[k] = v
print(len(ma), ha.used)

for k, v in tqdm(ma.items(), total=len(ma)):
    assert v == ha.get(k)
ha.tidy()
# ha.show()
print(ha.used)
