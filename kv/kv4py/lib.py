"""
一旦知道了平衡树的要求，不需要知道平衡树是怎么实现的，自己就应该可以想出来平衡树是怎么实现的

一切类，只需要实现get、remove、insert三个函数就可以加入测试，update函数等价于remove+insert，就不考虑了
"""

from abc import abstractmethod
from typing import List, Union, Tuple

import numpy as np
from tabulate import tabulate


class Kv:
    @abstractmethod
    def insert(self, k, v):
        pass

    @abstractmethod
    def remove(self, k):
        pass

    @abstractmethod
    def get(self, k):
        pass


class Dic(Kv):
    def __init__(self):
        self.a = {}

    def get(self, key):
        return self.a.get(key)

    def remove(self, key):
        if key in self.a:
            del self.a[key]

    def insert(self, k, v):
        self.a[k] = v


class Array(Kv):
    def insert(self, k, v):
        self.a.append((k, v))

    def remove(self, k):
        ans = -1
        for ind, i in enumerate(self.a):
            if i[0] == k:
                ans = ind
        if ans != -1:
            del self.a[ans]

    def get(self, k):
        for i in self.a:
            if i[0] == k:
                return i[1]
        return None

    def __init__(self):
        self.a = []


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next: Union[LinkedListNode, None] = None


class LinkedList(Kv):
    # 基于链表实现kv
    def __init__(self):
        self.head = LinkedListNode(None)  # 哨兵单元

    def insert(self, k, v):
        temp = self.head.next
        it = LinkedListNode((k, v))
        self.head.next = it
        it.next = temp

    def get(self, k):
        i = self.head.next
        while i:
            if i.value[0] == k:
                return i.value[1]
            i = i.next
        return None

    def remove(self, k):
        i = self.head
        while i.next and i.next.value[0] != k:
            i = i.next
        if not i.next:
            return None
        removing = i.next
        i.next = removing.next


class HashTable(Kv):
    # 哈希表外层是一个数组，内层可以是任意一种kv结构
    def __init__(self, ratio=0.7, init_size=16):
        self.ratio = ratio  # 负载因子，非空闲元素的比例，一旦超过这个比例，就需要扩容，扩容的时候遵循两倍原则
        self.init_size = init_size
        self.capacity = self.init_size
        self.a: List[Union[None, LinkedList]] = [None] * self.capacity
        self.full_count = 0
        self.count = 0

    def _hash(self, k):
        return hash(k) % self.capacity

    def _create(self, pos):
        self.a[pos] = LinkedList()
        self.full_count += 1

    def _expand(self):
        # 执行扩容操作
        a = self.a
        self.capacity *= 2
        self.a: List[Union[None, LinkedList]] = [None] * self.capacity
        for i in a:
            if i is None:
                continue
            j = i.head.next
            while j:
                self.insert(j.value[0], j.value[1])
                j = j.next

    def insert(self, k, v):
        pos = self._hash(k)
        if not self.a[pos]:
            self._create(pos)
        self.a[pos].insert(k, v)
        if self.full_count / self.capacity > self.ratio:
            self._expand()

    def remove(self, k):
        pos = self._hash(k)
        if not self.a[pos]:
            return
        self.a[pos].remove(k)

    def get(self, k):
        pos = self._hash(k)
        if not self.a[pos]:
            return None
        return self.a[pos].get(k)


class SkiplistNode:
    # 跳表的结点
    def __init__(self, key, value):
        self.next: List[Union[SkiplistNode, None]] = []
        self.key = key
        self.value = value


class SkipList(Kv):
    def __init__(self):
        self.head = SkiplistNode(None, None)  # 哨兵单元
        self.node_count = 0

    @staticmethod
    def random_height():
        h = 1
        while np.random.rand() < 0.5:
            h += 1
        return h

    def _incr_head(self, h):
        while self.height() < h:
            self.head.next.append(None)

    def height(self):
        return self.head.next.__len__()

    def _locate(self, k):
        # 执行查询k的过程，返回高度与跳表高度相同的前向结点列表
        if self.height() == 0:
            return None
        pre: List[Union[SkiplistNode, None]] = [None] * self.height()
        now = self.head
        h = self.height() - 1
        while h >= 0:
            nex = now.next[h]
            if nex is None or nex.key >= k:
                # 当无法向后走了，执行下钻过程
                pre[h] = now
                h -= 1
            else:
                now = nex
        return pre

    def insert(self, k, v):
        # 插入一个结点
        h = SkipList.random_height()
        if h > len(self.head.next):  # 如果高度不足，则提升高度
            self._incr_head(h)
        pre = self._locate(k)
        if pre[0].next[0] and pre[0].next[0].key == k:
            # 如果找到了，说明已经存在，直接更改它的数值即可
            pre[0].next[0].value = v
            return
        # 如果不存在，则需要创建这个结点
        new_node = SkiplistNode(k, v)
        new_node.next = [None] * h
        # 为pre插入后继
        for i in range(h):
            temp = pre[i].next[i]
            pre[i].next[i] = new_node
            new_node.next[i] = temp
        self.node_count += 1

    def remove(self, k):
        pre = self._locate(k)
        if pre is None \
                or pre[0].next[0] is None \
                or pre[0].next[0].key != k:
            return
        for i, node in enumerate(pre):
            temp = node.next[i].next[i] if node.next[i] else None
            node.next[i] = temp
        self.node_count -= 1

    def get(self, k):
        pre = self._locate(k)
        if pre is None \
                or pre[0].next[0] is None \
                or pre[0].next[0].key != k:
            return None
        return pre[0].next[0].value

    def __len__(self):
        return self.node_count

    def __repr__(self):
        # 以可视化较好的方式展示skiplist
        if self.height() == 0 or self.node_count == 0:
            return "empty"
        table: List[List[Union[Tuple, None]]] = [[None] * self.height() for _ in range(self.node_count)]
        now: SkiplistNode = self.head
        i = 0
        while now:
            now = now.next[0]
            if not now:
                break
            for j in range(len(now.next)):
                table[i][j] = (now.key, now.value)
            i += 1
        return tabulate(table)

    def __str__(self):
        return self.__repr__()


class BinaryTreeNode:
    def __init__(self, key, value):
        # 二叉树结点：左右儿子+kv
        self.left: Union[None, BinaryTreeNode] = None
        self.right: Union[None, BinaryTreeNode] = None
        self.key = key
        self.value = value


class BinaryTree(Kv):
    """
    这个数据结构没有parent指针，如果添加parent指针，只需要关注所有的
    x.left=y这样的语句，把y.parent设置为x
    x.right=y，把y.parent设置为x
    self.root=x,把x的parent设置为None
    """

    def __init__(self):
        self.root: Union[None, BinaryTreeNode] = None

    def _locate(self, k) -> List[Union[BinaryTreeNode, None]]:
        if not self.root:
            return []
        parents = []  # 记录祖先结点的目的是简化处理
        now: BinaryTreeNode = self.root
        while now:
            parents.append(now)
            if now.key > k:
                now = now.left
            elif now.key < k:
                now = now.right
            else:
                break
        return parents

    def get(self, k):
        parents = self._locate(k)
        if len(parents) == 0 or parents[-1].key != k:
            return None
        return parents[-1].value

    def insert(self, k, v):
        parents = self._locate(k)
        if len(parents) == 0:
            self.root = BinaryTreeNode(k, v)
            return
        if parents[-1].key == k:
            parents[-1].value = v
            return
        new_node = BinaryTreeNode(k, v)
        if k > parents[-1].key:
            parents[-1].right = new_node
        else:
            parents[-1].left = new_node

    def remove(self, k):
        parents = self._locate(k)
        if len(parents) == 0 or parents[-1].key != k:
            # node根本就不存在
            return
        no = parents[-1]
        father = parents[-2] if len(parents) >= 2 else None
        assert no.key == k
        # 找到右子树最小值替代，或者找到左子树最大值替代，或者直接把右子树贴到左子树中的对应位置
        if no.left is None and no.right is None:
            # 如果是叶子
            if father is None:
                # 必定为根
                self.root = None
            else:
                if father.left == no:
                    # 如果是左子树
                    father.left = None
                else:
                    assert father.right == no
                    father.right = None
        else:
            # 如果有后继结点，随机用左儿子或者右儿子进行替换。这种写法会导致不平衡性加剧
            if no.left:
                if no.right:
                    # 把右子树插入到左子树的最右侧
                    i = no.left
                    while i.right:
                        i = i.right
                    i.right = no.right
                candidate = no.left
            else:
                assert no.right is not None
                candidate = no.right
            assert candidate is not None
            if father:
                if candidate.key < father.key:
                    father.left = candidate
                else:
                    assert candidate.key > father.key
                    father.right = candidate
            else:
                self.root = candidate


class AvlNode:
    # AvlNode只是在TreeNode的基础上添加了height这个属性
    def __init__(self, key, value):
        # 二叉树的高度
        self.left: Union[None, AvlNode] = None
        self.right: Union[None, AvlNode] = None
        # AVL树结点记录parent结点便于执行回溯操作
        self.parent: Union[None, AvlNode] = None
        self.key = key
        self.value = value
        self.depth = 1

    def __repr__(self):
        return str(self.key)

    def update_depth(self):
        # 如果深度发生改变，则返回true，否则返回false
        now = max(self.left_depth(), self.right_depth()) + 1
        if now == self.depth:
            return False
        self.depth = now
        return True

    def left_depth(self):
        # 左子树深度
        if self.left is None:
            return 0
        return self.left.depth

    def right_depth(self):
        if self.right is None:
            return 0
        return self.right.depth

    def is_balance(self):
        return abs(self.left_depth() - self.right_depth()) <= 1

    def set_left(self, son):
        self.left = son
        if son:
            son.parent = self

    def set_right(self, son):
        self.right = son
        if son:
            son.parent = self

    def left_rotate(self):
        # 向左旋转：我是右子，弃我左子给父亲，我当王
        pa = self.parent
        is_left = pa.left == self if pa else False
        ri = self.right
        self.set_right(ri.left)
        ri.set_left(self)
        if pa:
            if is_left:
                pa.set_left(ri)
            else:
                pa.set_right(ri)
        else:
            ri.parent = None
        return ri

    def right_rotate(self):
        pa = self.parent
        is_left = pa.left == self if pa else False
        le = self.left
        self.set_left(le.right)
        le.set_right(self)
        if pa:
            if is_left:
                pa.set_left(le)
            else:
                pa.set_right(le)
        else:
            le.parent = None
        return le

    def is_leaf(self):
        return self.left is None and self.right is None


class Avl(Kv):
    """
    平衡树不平衡的时候有两种情况：
    左子树高度大于右子树高度
    右子树高度大于左子树高度

    调整的方式很简单：把自己的小儿子送给自己的父亲，然后自己继承皇位

    旋转：弃子于父，逼父退位，我承继大统，令我父与我儿子祖孙二人一起玩耍。

    若我为右子，则我父只要我之左子。
    若我为左子，则我父只要我之右子。

    我只能弃弱子于父，不能弃强子于父。因为我父亦不能制我之强子。
    若我有我父不可接受的强子，则强子替我上位。

    出一道题，按1，2，3，4，5....的顺序向AVL树中插入结点，求：
    * f(n)表示插入n的时候二叉树的深度
    * f(n)表示插入n的时候执行的旋转的次数


    数据结构就是物理。数据结构有特定的目的，为了达成这个目的，这个数据结构必须按照一定的规则行事。

    给定一个随机二叉树，尝试将其平衡化。

    再出一道题：把一个不平衡的二叉树平衡化。
    """

    def __init__(self):
        self.root: Union[AvlNode, None] = None

    def _locate(self, k) -> Union[AvlNode, None]:
        # 返回parent和now，parent用于插入结点
        if not self.root:
            return None
        now: AvlNode = self.root
        ans = None
        while now:
            ans = now
            if now.key == k:
                break
            if now.key > k:
                now = now.left
            else:
                now = now.right
        return ans

    def get(self, k):
        no = self._locate(k)
        if no is None or no.key != k:
            return None
        return no.value

    def insert(self, k, v):
        no = self._locate(k)
        if no is None:
            self.root = AvlNode(k, v)
            return
        if no.key == k:
            no.value = v
            return
        new_node = AvlNode(k, v)
        if k > no.key:
            no.set_right(new_node)
        else:
            no.set_left(new_node)
        self._update(no)

    def _update(self, node: AvlNode):
        i = node
        while i:
            if not i.is_balance():
                my_left = i.left_depth()
                my_right = i.right_depth()
                has_parent = i.parent is not None
                # 分四种情况分类讨论
                if my_left > my_right:
                    son_left = i.left.left_depth()
                    son_right = i.left.right_depth()
                    if son_left < son_right:
                        i.set_left(i.left.left_rotate())
                    it = i.right_rotate()
                else:
                    assert my_left < my_right
                    son_left = i.right.left_depth()
                    son_right = i.right.right_depth()
                    if son_left > son_right:
                        i.set_right(i.right.right_rotate())
                    it = i.left_rotate()
                if not has_parent:
                    # 如果没有父亲，说明根节点发生变化
                    self.root = it
                    self.root.parent = None
            changed = i.update_depth()
            if not changed:
                # 如果当前结点没有发生改变，直接向上走
                break
            i = i.parent

    def remove(self, k) -> Union[None, AvlNode]:
        no = self._locate(k)
        if no is None or no.key != k:
            # node根本就不存在
            return
        assert no.key == k
        father = no.parent
        if no.is_leaf():
            # 如果是叶子
            if father:
                is_left = father.left == no
                father.set_left(None) if is_left else father.set_right(None)
                self._update(father)
            else:
                self.root = None
            return
            # 如果没有左子树，直接把右子树怼上去
        if not no.left:
            if father:
                is_left = father.left == no
                father.set_left(no.right) if is_left else father.set_right(no.right)
                self._update(father)
            else:
                # 直接把root的parent置为空
                self.root = no.right
                self.root.parent = None
            return
            # 用左儿子的最右边进行替换
        candidate_parent = no
        i = no.left
        while i.right:
            candidate_parent = i
            i = i.right
        if i == no.left:
            # 左边只有一个儿子
            assert candidate_parent == no
            if father:
                i.set_left(None)
                i.set_right(no.right)
                is_left = father.left == no
                father.set_left(i) if is_left else father.set_right(i)
                self._update(i)
            else:
                self.root = i
                no.left.parent = None
                i.set_right(no.right)
            return
        assert candidate_parent != no
        candidate_parent.set_right(i.left)  # 删除掉替代品
        # 让替代品完全替代我的位置，处理好与我的儿子、父亲的关系
        # 此处如果no.left=i，则no.left应该清空，否则会产生死循环
        i.set_left(no.left)
        i.set_right(no.right)
        if not father:
            # 如果真正被删除的结点没有父节点，直接更新root
            self.root = i
            i.parent = None
        else:
            is_left = father.left == no
            father.set_left(i) if is_left else father.set_right(i)
        # 进行彻底的替换，candidate_parent是需要更新的地方
        self._update(candidate_parent)
        return


class RedBlackTree(Kv):
    """
    红黑树读取性能不如AVL，写性能略优于Avl。
    整体而言，两者差不太多。
    """

    def __init__(self):
        pass

    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def get(self, k):
        pass


class MultiTreeNode:
    def __init__(self):
        self.sons: List[Union[None, MultiTreeNode]] = []
        self.keys: List[Union[None, MultiTreeNode]] = []


class MultiTree(Kv):
    """
    多叉树
    """

    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def get(self, k):
        pass

    def __init__(self, max_son: int):
        self.max_son = max_son


class BTree(Kv):
    """
    https://ivanzz1001.github.io/records/post/data-structure/2018/06/16/ds-bplustree#1-b%E6%A0%91
    https://segmentfault.com/a/1190000020416577

    B树是平衡树的泛化
    每一个节点最多有 m 个子节点
    每一个非叶子节点（除根节点）最少有 ⌈m/2⌉ 个子节点
    如果根节点不是叶子节点，那么它至少有两个子节点
    有 k 个子节点的非叶子节点拥有 k − 1 个键
    所有的叶子节点都在同一层
    """

    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def get(self, k):
        pass


class BplusTree(Kv):
    """
    wiki中B+树外部链接部分包含各种介绍：
    https://zh.wikipedia.org/wiki/B%2B%E6%A0%91
    """
    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def get(self, k):
        pass


class BstarTree(Kv):
    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def get(self, k):
        pass
