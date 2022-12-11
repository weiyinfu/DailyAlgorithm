"""
https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/submissions/

给这个问题增加一点难度：输出乘积最小的那一对数字
"""


def solve(n):
    a = [int(i) for i in str(n - 1)]
    b = [0] * len(a)
    b[-1] = 1

    def go(n):
        for i in range(n, -1, -1):
            if a[i] <= 0:
                a[i] += 10
            else:
                a[i] -= 1
                break

    def update_a():
        beg = 0
        changed = False
        while beg < len(a) and a[beg] == 0:
            beg += 1
        for i in range(beg, len(a)):
            if a[i] <= 0:
                go(i)
                changed = True
                break
        return changed

    def update_b():
        beg = 0
        while beg < len(b) and b[beg] == 0:
            beg += 1
        for i in range(beg, len(b)):
            if b[i] == 0:
                b[i] += 1
                a[i] -= 1
                return True
        return False

    def ton(a):
        s = 0
        for i in range(len(a)):
            s = s * 10 + a[i]
        return s

    while 1:
        # print(a, b)
        changed = update_a()
        if changed:
            continue
        for i in range(len(a)):
            if a[i] == 10:
                b[i] += 1
                a[i] -= 1
                changed = True
        if changed:
            continue
        changed = update_b()
        if not changed:
            break

    s = ton(a)
    return [s, n - s]


def bruteforce(n):
    for i in range(1, n // 2 + 1):
        if '0' in str(i) or '0' in str(n - i):
            continue
        else:
            return [i, n - i]


def fatasitic(n):
    """
    让两个数字逐渐向中间靠拢，一直到无法update为止
    :param n:
    :return:
    """
    def prev(n):
        # 小于n的不含0的数字
        a = [int(i) for i in str(n - 1)]
        first = -1
        for i in range(len(a)):
            if a[i] == 0:
                first = i
                break
        if first == -1:
            return n - 1
        a[first - 1] -= 1
        for i in range(first, len(a)):
            a[i] = 9
        s = 0
        for i in a:
            s = s * 10 + i
        return s

    def nex(n):
        # 大于n且不含0的数字
        a = [int(i) for i in str(n + 1)]
        first = -1
        for i in range(len(a)):
            if a[i] == 0:
                first = i
                break
        if first == -1:
            return n + 1
        a[first] = 1
        for i in range(first, len(a)):
            a[i] = 1
        s = 0
        for i in a:
            s = s * 10 + i
        return s

    a, b = n - 1, 1
    while 1:
        # print(a, b, 'prev', prev(102))
        if '0' in str(a):
            aa = prev(a)
            if aa != a:
                a = aa
                b = n - a
                continue
        if '0' in str(b):
            bb = nex(b)
            if bb != b:
                b = bb
                a = n - b
                continue
        break
    return [a, b]


def test_solve():
    for i in range(2, 20000):
        x = bruteforce(i)
        y = solve(i)
        if set(x) != set(y):
            print(i, x, y)


def test_fatastic():
    for i in range(2, 20000):
        x = bruteforce(i)
        y = fatasitic(i)
        if set(x) != set(y):
            print(i, x, y)


def test_one():
    x = 201002
    # print(bruteforce(x))
    # print(solve(x))
    print(fatasitic(x))


# test_fatastic()
print(fatasitic(103))
