s = 'asdofiuweqorjwerwqouioasdqwer'

"""
字符串s从任意一个下标开始，可以得到len(s)个字符串，对这些字符串排序，取排序后每个字符串的最后一个字符拼接起来
"""
def sort1():
    def cmp(x, y):
        for i in range(len(s)):
            m, n = s[(x + i) % len(s)], s[(y + i) % len(s)]
            if m != n:
                return ord(m) - ord(n)
        return 0

    a = list(range(len(s)))
    for i in range(len(s)):
        for j in range(i):
            if cmp(a[i], a[j]) < 0:
                a[i], a[j] = a[j], a[i]
    b = [s[(i - 1 + len(s)) % len(s)] for i in a]
    return ''.join(b)
