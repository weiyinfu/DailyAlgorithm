from typing import List


def quick_sort(a: List[int]):
    def solve(beg, end):
        if beg >= end:
            return
        i = beg
        j = end
        v = a[beg]
        while i < j:
            while i < j and a[j] >= v:
                j -= 1
            if i >= j:
                break
            a[j] = a[i]
            while i < j and a[i] <= v:
                i += 1
            if i >= j:
                break
            a[i] = a[j]

        print(f"mid={v} {a}")
        a[i] = v
        solve(beg, i - 1)
        solve(i + 1, end)

    solve(0, len(a) - 1)


def quicksort2(a: List[int]):
    def go(beg, end):
        if beg >= end:
            return
        print(a[beg:end + 1])
        i = beg
        j = end
        ii = beg
        jj = end
        eq = 0
        v = a[beg]
        while ii < jj:
            while ii < jj and a[ii] <= v:
                if a[ii] == v:
                    eq += 1
                else:
                    a[i] = a[ii]
                    i += 1
                ii += 1
            while ii < jj and a[jj] >= v:
                if a[jj] == v:
                    eq += 1
                else:
                    a[j] = a[jj]
                    j -= 1
                jj -= 1
            if ii < jj:
                a[ii], a[jj] = a[jj], a[ii]
            else:
                if a[ii] < v:
                    a[i] = a[ii]
                    i += 1
                else:
                    a[j] = a[ii]
                    j -= 1
        for i in range(i, j + 1):
            a[i] = v
        go(beg, i - 1)
        go(j + 1, end)

    go(0, len(a) - 1)


def quicksort3(a: List[int]):
    """
    快排最佳模板：写起来虽然简单，但是存在比较多的无用交换
    :param a:
    :return:
    """

    def go(beg, end):
        if beg >= end:
            return
        j = end
        v = a[beg]
        i = beg + 1
        while i < j:
            if a[i] > v:
                a[i], a[j] = a[j], a[i]
                j -= 1
            else:
                i += 1
        if a[i] > v:
            i -= 1
        a[i], a[beg] = a[beg], a[i]
        go(beg, i - 1)
        go(i + 1, end)

    go(0, len(a) - 1)


def quicksort4(a: List[int]):
    """
    性能最佳模板
    :param a:
    :return:
    """

    def go(beg, end):
        if beg >= end:
            return
        j = end
        v = a[beg]
        i = beg + 1
        while i < j:
            while i < j and a[i] <= v:
                i += 1
            while i < j and a[j] >= v:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if a[i] > v:  # 这句话是点睛之笔，必须要让i和j指向一个较小的值，这样才便于跟a[beg]进行交换
            i -= 1
        a[i], a[beg] = a[beg], a[i]
        go(beg, i - 1)
        go(i + 1, end)

    go(0, len(a) - 1)


def main():
    # a = [1, 3, 1, 2, 4, 5]
    # quick_sort(a)
    # print(a)
    a = [1, 3, 1, 2, 4, 5]
    quicksort4(a)
    print(a)


main()
