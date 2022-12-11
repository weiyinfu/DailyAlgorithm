"""
递归算法求解九连环，缺点是步骤较多。
"""


def up(a, ind):
    if ind == 0:
        a[ind] = 1
        return [['up', 0]]
    ans = []
    ans.extend(up(a, ind - 1))
    ans.append(['up', ind])
    a[ind] = 1
    ans.extend(down(a, ind - 1))
    return ans


def down(a, ind):
    if ind == 0:
        a[ind] = 0
        return [['down', 0]]
    ans = []
    ans.extend(up(a, ind - 1))
    ans.append(['down', ind])
    a[ind] = 0
    ans.extend(down(a, ind - 1))
    return ans


def down_all(a):
    ans = []
    while 1:
        ind = -1
        for i in range(len(a)):
            if a[i] == 1:
                ind = i
                break
        if ind == -1:
            # 已经没有在上面的了
            break
        ans.extend(down(a, ind))
    for i in ans:
        i[1] += 1
    return ans


ans = down_all([1, 1, 1, 1, 1, 1, 1, 1, 1])
for ind, i in enumerate(ans):
    print(ind, i)
