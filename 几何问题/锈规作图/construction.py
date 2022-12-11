import math
from pprint import pprint

import numpy as np

AC = 0  # AC长度，也就是半径
eps = 1e-4
point_list = []  # 点列表，用于演示
event_list = []  # 事件列表，用于演示


# 给定两个圆心，半径为AC，求交点
def getCross(a, b):
    a, b = np.array(a), np.array(b)
    ab = b - a  # ab向量
    chui = np.array((ab[1], -ab[0]))  # ab向量的垂直向量
    chui_len = (AC * 2) ** 2 - dis(a, b) ** 2  # 垂向量的长度
    chui_len = 0 if chui_len < eps else math.sqrt(chui_len)
    chui = chui * chui_len / math.hypot(chui[0], chui[1])  # ab向量的垂直向量
    p1 = (ab + chui) / 2 + a
    p2 = (ab - chui) / 2 + a
    return p1, p2


def dis(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def eq(x, y):
    return abs(x - y) < eps


# 以a为中心，以c为端点，画一个正六边形
def expand(a, c):
    ps = [(c[0] - a[0], c[1] - a[1])]
    for i in range(5):
        t = ps[-1]
        ps.append((t[0] / 2 - math.sqrt(3) / 2 * t[1], t[1] / 2 + t[0] * math.sqrt(3) / 2))
    ps = [(i[0] + a[0], i[1] + a[1]) for i in ps]
    return ps


# 由a，c两点做一条从a到b的折线
def zhexian(a, b, c):
    ans = [c, a]
    while 1:
        if dis(ans[-1], b) < AC * 2:  # 如果与目标b的距离足够近了，折线结束
            ans.extend([getCross(ans[-1], b)[0], b])
            event_list.append(('折线', len(point_list), ans[1:]))
            return ans[1:]  # 去掉c
        ans.append(min(expand(ans[-1], ans[-2]), key=lambda x: dis(x, b)))


# 从a，c出发做一个平行四边形，使得ac//bd
def sibianxing(a, b, c):
    ps = zhexian(a, b, c)
    ans = c
    for i in range(1, len(ps)):
        point_list.append(ans)
        if eq(0, dis(ans, ps[i])):
            ans = 2 * np.array(ps[i]) - np.array(ps[i - 1])
        else:
            p = getCross(ans, ps[i])
            ans = p[0] if eq(0, dis(p[1], ps[i - 1]))else p[1]
    return ans


# 由三点a,b,c求第四点d使abd为正三角形
def sanjiaoxing(a, b, c):
    ps = zhexian(a, b, c)
    ans = getCross(ps[0], ps[1])[0]
    for i in range(1, len(ps) - 1):
        event_list.append(('多边形', len(point_list), (a, ans, ps[i])))
        point_list.append(ans)
        second = getCross(ps[i], ps[i + 1])[0]
        event_list.append(("多边形", len(point_list), (ps[i], ps[i + 1], second)))
        temp = ans
        ans = sibianxing(ps[i], ans, second)
        event_list.append(("多边形", len(point_list), (ps[i], second, ans, temp)))
        event_list.append(("多边形", len(point_list), (a, ps[i + 1], ans)))
        point_list.append(ans)
    return ans


def solve(a, b, c):
    global AC, point_list, event_list
    AC = dis(a, c)
    point_list, event_list = [], []
    d = sanjiaoxing(a, b, c)
    print(dis(d, a), dis(d, b), dis(a, b), "三条边长")
    return np.array(point_list), event_list


def main():
    for a, b, c in np.array([float(i) for i in open("construction-data.txt").read().split()]).reshape((-1, 3, 2)):
        solve(a, b, c)
        pprint(point_list)


if __name__ == '__main__':
    main()
