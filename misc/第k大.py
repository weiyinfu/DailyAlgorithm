import numpy as np
from tqdm.autonotebook import tqdm


def which(a: np.ndarray, k: int):
    a.sort()
    return a[k]


def quick(a, k):
    def go(beg, end, k):
        if beg >= end:
            if beg != k:
                print(beg, k, 'bagga')
            return a[beg]
        # 在beg，end闭区间上求第k大
        ind = np.random.randint(beg, end + 1)
        mid = a[ind]
        l = beg
        r = end
        while l < r:
            while l < r and a[l] <= mid:
                l += 1
            while l < r and a[r] >= mid:
                r -= 1
            if l == r: break
            a[l], a[r] = a[r], a[l]
        if l < ind:
            if a[l] < mid:
                l += 1
        elif l > ind:
            if a[l] > mid:
                l -= 1
        a[l], a[ind] = a[ind], a[l]
        if l == k:
            return mid
        elif l > k:
            return go(beg, l - 1, k)
        else:
            return go(l + 1, end, k)

    return go(0, len(a) - 1, k)


def test():
    for _ in tqdm(range(10000)):
        a = np.random.randint(0, 100, 1000)
        k = np.random.randint(0, len(a))
        right = which(a.copy(), k)
        mine = quick(a.copy(), k)
        if right != mine:
            print("question is ", a)
            print(right, mine)


test()
