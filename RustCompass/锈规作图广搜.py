import math

import matplotlib.pyplot as plt
import numpy as np


def load():
    f = open("construction-data.txt")
    data = [float(i) for i in " ".join(f.readlines()).split()]
    sz = len(data) // 6
    for i in range(sz):
        yield (data[i * 6], data[i * 6 + 1]), (data[i * 6 + 2], data[i * 6 + 3]), (data[i * 6 + 4], data[i * 6 + 5])


point_list = None
A = None
B = None
AC = None
AB = None
eps = 1e-4


def visited(a):
    for i in point_list:
        if dis(i[1], a) < eps:
            return True
    return False


def is_ans(a):
    one = dis(a, A)
    two = dis(a, B)
    return abs(one - two) < eps


def tooFar(a):
    one = dis(a, A)
    two = dis(a, B)
    return one > 1.4 * AB and two > 1.4 * AB


def show():
    plt.scatter([i[1][0] for i in point_list], [i[1][1] for i in point_list])
    plt.show()


# 给定两个圆心求交点
def getCross(a, b):
    a, b = np.array(a), np.array(b)
    ab = b - a  # ab向量
    chui = np.array((ab[1], -ab[0]))
    chui_len = math.sqrt((AC * 2) ** 2 - dis(a, b) ** 2)
    chui = chui * chui_len / math.hypot(chui[0], chui[1])  # ab向量的垂直向量
    p1 = (ab + chui) / 2 + a
    p2 = (ab - chui) / 2 + a
    print(a,b,AC,p1,p2)
    return p1, p2


def dis(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


# 元组：id，坐标元组，解释
def solve(a, b, c):
    global AC, point_list, A, B, AB
    A, B = a, b
    AC = dis(a, c)
    AB = dis(a, b)
    point_list = [(1, a, "P 1"), (2, b, "P 2"), (3, c, "P 3")]
    ind = 1
    while ind < len(point_list):
        print(ind, point_list[ind])
        show()
        for i in range(ind):
            if dis(point_list[ind][1], point_list[i][1]) < AC * 2:
                p1, p2 = getCross(point_list[ind][1], point_list[i][1])
                for p in (p1, p2):
                    if tooFar(p):
                        print("too far", p, A, B)
                        continue
                    if visited(p):
                        print("visited", p, A, B)
                        continue
                    point_list.append((len(point_list), p, "C {} {}".format(point_list[ind][0], point_list[i][0])))
                    if is_ans(p):
                        return
        ind += 1


def main():
    for i in load():
        solve(i[0], i[1], i[2])
        for j in point_list[:-1]:
            print(str(j[0]) + "#", j[1][0], j[1][1], j[2])
        last = point_list[len(point_list) - 1]
        print("D", last[1][0], last[1][1], last[2])


main()
