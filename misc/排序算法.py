import numpy as np
from tqdm.autonotebook import tqdm


def bubble(a):
    """
    冒泡排序的复杂度比较确定，它跟选择排序的复杂度是一致的，都是非常确定的O(n^2)
    丝毫没有优化空间，而插入排序则是存在优化空间的
    :param a:
    :return:
    """
    for i in range(len(a)):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


def quick(a):
    # 快排
    def go(beg, end):
        if beg >= end:
            return
        k = np.random.randint(beg, end + 1)
        a[beg], a[k] = a[k], a[beg]
        mid = a[beg]
        l = beg
        r = end
        while 1:
            while l < r and a[r] > mid:
                r -= 1
            if l == r: break
            a[l], a[r] = a[r], a[l]
            l += 1
            while l < r and a[l] < mid:
                l += 1
            if l == r: break
            a[l], a[r] = a[r], a[l]
            r -= 1
        go(beg, l - 1)
        go(l + 1, end)

    go(0, len(a) - 1)


def quick2(a):
    def go(beg, end):
        if beg >= end:
            return
        k = np.random.randint(beg, end + 1)
        mid = a[k]
        l = beg
        r = end
        while l < r:
            while l < r and a[l] <= mid:
                l += 1
            while l < r and a[r] >= mid:
                r -= 1
            if l == r:
                break
            a[l], a[r] = a[r], a[l]
        if l > k:
            if a[l] > a[k]:
                l -= 1
                a[l], a[k] = a[k], a[l]
            else:
                a[l], a[k] = a[k], a[l]
        elif l < k:
            if a[l] > a[k]:
                a[l], a[k] = a[k], a[l]
            else:
                l += 1
                a[l], a[k] = a[k], a[l]
        go(beg, l - 1)
        go(l + 1, end)

    go(0, len(a) - 1)


def quick3(a):
    # 对quick2的化简
    def go(beg, end):
        if beg >= end:
            return
        k = np.random.randint(beg, end + 1)
        mid = a[k]
        l = beg
        r = end
        while l < r:
            while l < r and a[l] <= mid:
                l += 1
            while l < r and a[r] >= mid:
                r -= 1
            if l == r:
                break
            a[l], a[r] = a[r], a[l]
        if (l > k) == (a[l] > a[k]):
            if l > k:
                l -= 1
            elif l < k:
                l += 1
        a[l], a[k] = a[k], a[l]
        go(beg, l - 1)
        go(l + 1, end)

    go(0, len(a) - 1)


def quick4(a):
    """
    对于包含大量重复元素的数组，一次partition能够做到将值为mid的元素移动到中间部分
    这被称为”三向切分“，适用于包含大量重复元素的情形
    三向切分的复杂度与二分相当，但是写起来却很复杂
    :param a:
    :return:
    """

    def go(beg, end):
        if beg >= end:
            return
        k = np.random.randint(beg, end + 1)
        mid = a[k]
        r = end + 1
        i = beg
        for l in range(beg, end + 1):
            if l == r:
                break
            if a[l] < mid:
                if i < l:
                    a[i] = a[l]
                i += 1
            elif a[l] == mid:
                continue
            else:
                # find right
                r -= 1
                while r > l and a[r] > mid:
                    r -= 1
                if l == r:
                    break
                temp = a[r]
                a[r] = a[l]
                if temp < mid:
                    a[i] = temp
                    i += 1
        for j in range(i, r):
            a[j] = mid
        go(beg, i - 1)
        go(r, end)

    go(0, len(a) - 1)


def quick5(a):
    """
    这种写法缺点是需要反复swap，对于5 5 5 5这种，需要多次swap。
    :param a:
    :return:
    """

    def go(beg, end):
        if beg >= end:
            return
        mid = a[beg]
        l = beg
        r = end
        i = beg + 1
        while i <= r:
            if a[i] > mid:
                a[i], a[r] = a[r], a[i]
                r -= 1
            else:
                a[i], a[l] = a[l], a[i]
                l += 1
                i += 1
        go(beg, l - 1)
        go(l + 1, end)

    go(0, len(a) - 1)


def quick6(a):
    """
    这是我最初的快排模板，这种写法依旧存在多次交换的缺点。
    例如，对于[5,5,5,6,5]，会对5进行多次swap
    :param a:
    :return:
    """

    def go(beg, end):
        if end <= beg:
            return
        x = np.random.randint(beg, end + 1)
        sep = a[x]
        a[beg], a[x] = a[x], a[beg]
        l = beg
        r = end
        while 1:
            while r > l and a[r] >= sep:
                r -= 1
            if r <= l:
                break
            a[l] = a[r]
            a[r] = sep
            l += 1
            # 移动功能左边的指针，直到找到大于sep的值
            while l < r and a[l] <= sep:
                l += 1
            if l >= r:
                break
            a[r] = a[l]
            a[l] = sep
            r -= 1
        go(beg, l - 1)
        go(l + 1, end)

    go(0, len(a) - 1)


def quick7(a):
    def go(left, right):
        if left >= right:
            return
        i = left
        j = right
        tmp = a[i]
        while i < j:
            while i < j and a[j] > tmp:
                j -= 1
            while i < j and a[i] <= tmp:
                i += 1
            a[i], a[j] = a[j], a[i]
        a[left], a[j] = a[j], a[left]
        go(left, i - 1)
        go(i + 1, right)

    go(0, len(a) - 1)


def quick8(a):
    """
    简化版三路切分，这种写法会造成swap次数比较多
    """

    def go(l, h):
        if l >= h:
            return
        lt = l
        i = l + 1
        gt = h
        v = a[l]
        while i <= gt:
            if a[i] < v:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
            elif a[i] > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        go(l, lt - 1)
        go(gt + 1, h)

    go(0, len(a) - 1)


def select(a):
    """
    选择排序的复杂度是比较高的，因为它的复杂度比较确定，每次一定会扫描全部数组
    而插入排序则只看前面，不看后面，有一定的概率使得交换次数尽量少
    :param a:
    :return:
    """
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]


def insert(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def heap(a):
    # 堆排序
    # 建堆过程
    def up(i):
        while i > 0:
            p = (i - 1) >> 1
            if a[i] < a[p]:
                a[i], a[p] = a[p], a[i]
            else:
                break
            i = p

    def down(i, big):
        while 1:
            l = i * 2 + 1
            r = i * 2 + 2
            if l >= big: return
            k = l if a[l] < a[r] or r >= big else r
            if a[k] >= a[i]: return
            a[i], a[k] = a[k], a[i]
            i = k

    for i in range(len(a)):
        up(i)
    for k in range(len(a) - 1, -1, -1):
        a[0], a[k] = a[k], a[0]
        down(0, k)
    for i in range(len(a) // 2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]


def merge(a):
    """
    归并排序：自顶向下算法
    """
    b = [0] * len(a)

    def go(beg, end):
        if beg == end:
            return
        mid = (beg + end) // 2
        go(beg, mid)
        go(mid + 1, end)
        i = beg
        j = mid + 1
        k = beg
        while k <= end:
            if j > end or i <= mid and a[i] < a[j]:
                b[k] = a[i]
                k += 1
                i += 1
            else:
                b[k] = a[j]
                k += 1
                j += 1
        for i in range(beg, end + 1):
            a[i] = b[i]

    go(0, len(a) - 1)


def fast_merge(a):
    """
    非递归归并：自底向上算法
    """
    step = 1
    b = [0] * len(a)

    def merge(beg, mid, end):
        i = beg
        j = mid + 1
        for k in range(beg, end + 1):
            if j > end or i <= mid and a[i] < a[j]:
                b[k] = a[i]
                k += 1
                i += 1
            else:
                b[k] = a[j]
                k += 1
                j += 1
        for k in range(beg, end + 1):
            a[k] = b[k]

    while step < len(a):
        for i in range(0, len(a), 2 * step):
            merge(i, i + step - 1, min(i + step * 2 - 1, len(a) - 1))
        step <<= 1


def shell(a):
    """
    希尔排序是对插入排序的改进，避免插入的时候移动太多元素

    希尔排序算法对于步长的选择很有门道，只需要保证最终步长为1即可，至于其它位置的步长可以随意
    :param a:
    :return:
    """

    def get_steps():
        steps = []
        step = 1
        while step < len(a):
            steps.append(step)
            step = 3 * step + 1
        return steps[::-1]

    for step in get_steps():
        for i in range(0, len(a)):
            j = i
            while j - step >= 0 and a[j] < a[j - step]:
                a[j], a[j - step] = a[j - step], a[j]
                j -= step


def test():
    for cas in tqdm(range(1000)):
        a = np.random.randint(0, 10, 10)
        ans = None
        for m in (bubble, quick, quick2, quick3,
                  quick4, quick5, quick6, quick7,
                  heap, select, insert, merge,
                  fast_merge, shell, quick8):
            b = a.copy()
            m(b)
            if ans is None:
                ans = b
            else:
                if not np.all(b == ans):
                    print(m.__name__, 'different')
                    print('problem', a)
                    print(b, ans)
                    assert False


def test_one(f):
    # np.random.seed(1)
    a = np.random.randint(0, 10, 5)
    print(a)
    f(a)
    print(a)


test()
# test_one(quick9)
