"""
n个人围成一圈，最后能活下来的人是谁？
"""


def bruteforce(n, k):
    a = list(range(n))
    i = 0
    while len(a) > 1:
        i = i + k - 1
        i %= len(a)
        del a[i]
    return a[0]


def rec_slow(n, k):
    def solve(n):
        if n == 1:
            return 0
        die = k
        live = (die + solve(n - 1)) % n
        return live

    return solve(n)


def rec_fast(n, k):
    def solve(n):
        if n == 1:
            return 0
        if k == 1:
            return n - 1
        if n >= k:
            g = n // k  # k个人一组，第一波可以淘汰g个人
            c = solve(n - g)
            # print(n, k, "group count", g, 'kk', k, 'which=', c)
            left = n - g * k  # 右边剩下的人数
            ans = g * k + c + max(c - left, 0) // (k - 1)  # 加上c然后再加上已经淘汰的那些人
            ans %= n
            # print(f"{n} {k} live = {ans} real_ans={bruteforce(n, k)}")
        else:
            # 如果n小于k，那么每次只能淘汰一个人
            ans = (k + solve(n - 1)) % n
        return ans

    return solve(n)


def test_rec_slow():
    for n in range(1, 10):
        for k in range(1, 10):
            b = bruteforce(n, k)
            r = rec_slow(n, k)
            if b != r:
                print('error', n, k)
                exit(-1)
    print('pass')


def test_rec_fast():
    for n in range(1, 10):
        for k in range(1, 10):
            b = bruteforce(n, k)
            r = rec_fast(n, k)
            if b != r:
                print('error', n, k)
                exit(-1)
    print('pass')


def test_one():
    print(bruteforce(10, 3))
    print(rec_slow(10, 3))


def test_one_rec_fast():
    print(bruteforce(5, 2))
    print(rec_fast(5, 2))


# test_rec_slow()
test_rec_fast()
# test_one_rec_fast()
# print(bruteforce(4,3))
