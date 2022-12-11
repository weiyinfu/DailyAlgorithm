"""
已知正三棱锥SABC，锥尖为S。三棱锥高SD=1/2，底面边长AB=BC=AC=1。过A向它所对侧面SBC做垂线AO，垂足为O，在AO取一点X使得AX:XO=40。求经过X且平行于ABC的截面面积。
"""

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from mpl_toolkits.mplot3d import Axes3D


def get_dis(a, b):
    return sp.sqrt(sum((a - b) ** 2))


def get_area_by_edge(a, b, c):
    # 海伦公式根据三条边求面积
    p = (a + b + c) / 2
    return sp.sqrt(p * (p - a) * (p - b) * (p - c))


def get_area_by_point(A, B, C):
    return get_area_by_edge(get_dis(A, B), get_dis(A, C), get_dis(B, C))


def eval_point(p):
    a = []
    for i in p:
        if i is sp.Expr:
            a.append(i.evalf())
        else:
            a.append(i)
        print(type(a[-1]))
    return a


A = np.array([0, 0, 0], dtype=sp.Rational)
B = np.array((1, 0, 0), dtype=sp.Rational)
C = (sp.Rational(1, 2), sp.sqrt(3) / 2, sp.Rational(0))
D = np.mean([A, B, C], axis=0)
S = np.array((D[0], D[1], sp.Rational(1, 2)))
M = np.mean([B, C], axis=0)
ASM = get_area_by_point(A, M, S)
AO = ASM / get_dis(S, M)
MO = sp.sqrt(get_dis(A, M) ** 2 - AO ** 2)
OH = AO * MO / get_dis(A, M)
XZ = OH * sp.Rational(40, 41)
ABC = get_area_by_point(A, B, C)
ratio = 1 - XZ / S[2]
ans = ABC * ratio ** 2
ans = ans.simplify()
print(ans, ans.evalf())
"""
简单地可视化一下
"""
fig = plt.figure()
ax = Axes3D(fig)
p = np.array((A, B, C, D, S, M), dtype=np.float32)
ax.scatter(p[:, 0], p[:, 1], p[:, 2], c='r', marker='o')
text = 'ABCDSM'
for i in range(len(text)):
    x, y, z = p[i]
    ax.text(x, y, z, s=text[i])
lines = [(A, B, 'r'), (B, C, 'r'), (A, C, 'grey'), (A, M, 'grey'), (A, S, 'r'), (B, S, 'r'), (C, S, 'r'), (S, M, 'r'), (S, D, 'grey')]
for f, t, c in lines:
    line = np.array([f, t], dtype=np.float32)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], c=c)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
