"""
二分法容易犯的错误就是容易写成死循环
m=(l+r)>>1，如果l+1==r，则m=l
更新的时候l=m，这样会导致死循环，所以二分法的终止条件只需要写成l+1=r即可，这种写法的好处是不需要在while循环内部进行缠斗。

这样一来，就需要对最终跳出循环之后的情况添加一些判断即可
"""


def lower_bound(a, v):
    # 此处需要注意，求lower_bound的时候有可能取到-1，求小于等于v的值
    l = 0
    r = len(a)
    while l + 1 < r:
        m = (l + r) >> 1
        if a[m] < v:
            l = m
        else:
            r = m
    if r < len(a) and a[r] <= v:
        return r
    if a[l] <= v:
        return l
    return -1


def upper_bound(a, v):
    # 此处需要注意，求upper_bound的时候有可能取到len(a)，大于等于v的值
    l = 0
    r = len(a)
    while l + 1 < r:
        m = (l + r) >> 1
        if a[m] <= v:
            l = m
        else:
            r = m
    if l < len(a) and a[l] >= v:
        return l
    return r


def exists(a, v):
    # 判断元素是否存在非常简单
    l = 0
    r = len(a) - 1
    while l + 1 < r:
        m = (l + r) // 2
        if a[m] < v:
            l = m + 1
        else:
            r = m
    return a[l] == v or a[r] == v


a = [2, 3, 3, 3, 4]
print(lower_bound(a, 1))  # -1
print(lower_bound(a, 2))  # 0
print(upper_bound(a, 2))  # 0
print(lower_bound(a, 3))  # 1
print(upper_bound(a, 3))  # 3
print(upper_bound(a, 4))  # 4
print(upper_bound(a, 5))  # 5
print(lower_bound(a, 5))  # 4
