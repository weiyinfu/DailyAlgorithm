"""
甲乙丙三人下象棋，胜一局加一分，负一局减一分（此处我看成了负一局减1分，原题是负一局不加分），和一局各得0.5分。
三人两两对局数相等。
甲胜最多，乙负最少，丙分最高。求对局情况。

甲 vs 乙 2胜 3平 2负
甲 vs 丙 3胜 0平 4负
乙 vs 丙 0胜 7平 0负

总计
甲 5胜 3平 6负   6.5
乙 2胜 10平 2负  7
丙 4胜 7平 3负   7.5

更小的解答（可能是最小解）：

甲 vs 乙 2胜 3平 2负
甲 vs 丙 3胜 0平 4负
乙 vs 丙 0胜 7平 0负

总计
甲 5胜 3平 6负   6.5
乙 2胜 10平 2负  7
丙 4胜 7平 3负   7.5
"""

import sympy as sp
import numpy as np

a = sp.symarray('a', (3, 3))
b = np.zeros((3, 3), dtype=np.object)
c = [[0, 1], [0, 2], [1, 2]]
for i in range(3):
    for j in range(3):
        x, y = c[i]
        state = j
        cnt = a[i][j]
        if state == 0:
            b[x][0] += cnt
            b[y][1] += cnt
        elif state == 1:
            b[y][0] += cnt
            b[x][1] -= cnt
        else:
            b[y][2] += cnt
            b[x][2] += cnt
score = np.matmul(b, [1, -1, 0.5])
k = sp.symarray('k', 6)
mat = [
    # 甲胜最多
    b[0][0] - b[1][0] - k[0],
    b[0][0] - b[2][0] - k[1],
    # 乙负最少
    b[0][1] - b[1][1] - k[2],
    b[2][1] - b[1][1] - k[3],
    # 丙分最多
    score[2] - score[0] - k[4],
    score[2] - score[1] - k[5],
    # 两两对局次数相等
    sum(a[0]) - sum(a[1]),
    sum(a[0]) - sum(a[2]),
]
from pprint import pprint

pprint(mat)
print('=' * 10)
unknown = list(a.reshape(-1))
ans = sp.solve(mat, unknown)
maybe = {i: 0.1 for i in k}
for k, v in ans.items():
    print(k, v.subs(maybe))
