from math import *
import matplotlib.pyplot as plt
"""
小明在（0,0）处，小红在（r，0）处，小明朝着小红跑，小红沿着直线跑。
问小明什么时候追上小红。
"""
r = 3  # 模型
a = (0, 0)
b = (r, 0)
v1 = 1
v2 = 0.4
dt = 0.0001
t = 0
eps = 1e-3


def mine():
    c = r ** (v2 / v1)
    y = c / 2 * v1 / (v1 - v2) * r ** (1 - v2 / v1) - 1 / 2 / c * v1 / (v1 + v2) * r ** (1 + v2 / v1)
    return y / v2


print(mine())

ro = []
a_pos = []
b_pos = []
while 1:
    b = (r, v2 * t)  # 小红的新位置
    dir = b[0] - a[0], b[1] - a[1]
    dir = (dir[0] / hypot(dir[0], dir[1]), dir[1] / hypot(dir[0], dir[1]))
    a = (a[0] + v1 * dir[0] * dt, a[1] + v1 * dir[1] * dt)
    t += dt
    ro.append(hypot(a[0], a[1]))
    a_pos.append(a)
    b_pos.append(b)
    if hypot(a[0] - b[0], a[1] - b[1]) < eps:
        break
print(t)
one = plt.subplot('211')
one.plot([i * dt for i in range(len(ro))], ro)
two = plt.subplot('212')
two.plot([i[0] for i in a_pos], [i[1] for i in a_pos])
two.plot([i[0] for i in b_pos], [i[1] for i in b_pos])
plt.show()
