"""
给定两个数字，求除法循环节
"""


def get(n, a):
    left = {}
    same = None
    while n:
        l = n % a
        v = n // a
        n = l * 10
        if l in left:
            same = left[l][0]
            break
        else:
            ind = len(left)
            left[l] = (ind, v)
    left = list(left.items())
    left.sort(key=lambda x: x[1])
    return [i[1][1] for i in left], same


ans = get(13, 7)
print(ans)
