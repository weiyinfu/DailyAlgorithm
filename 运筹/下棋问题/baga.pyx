import numpy as np

SCORE = [1, 0, 0.5]  # 胜负和
cdef judge(a):
    cdef int i, j
    cdef int x, y, state, cnt
    b = np.zeros((3, 3), dtype=np.object)
    c = [[0, 1], [0, 2], [1, 2]]
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            x, y = c[i]
            state = j
            cnt = a[i][j]
            if state == 0:
                b[x][0] += cnt
                b[y][1] += cnt
            elif state == 1:
                b[y][0] += cnt
                b[x][1] += cnt
            else:
                b[y][2] += cnt
                b[x][2] += cnt
            j += 1
        i += 1
    score = np.matmul(SCORE, b.T)
    mat = [
        # 甲胜最多
        b[0][0] - b[1][0],
        b[0][0] - b[2][0],
        # 乙负最少
        b[0][1] - b[1][1],
        b[2][1] - b[1][1],
        # 丙分最多
        score[2] - score[0],
        score[2] - score[1],
    ]
    for ii in mat:
        if ii <= 0:
            return False
    # 两两对局次数相等
    if sum(a[0]) - sum(a[1]):
        return False
    if sum(a[0]) - sum(a[2]):
        return False
    return True

ans = []
a = np.zeros((3, 3))

n = 8
cdef go(int x, int y, pro):
    if x == 3:
        pro.update(1)
        if judge(a):
            ans.append(a.copy())
        return
    for i in range(n):
        a[x][y] = i
        if y < 2:
            go(x, y + 1, pro)
        else:
            go(x + 1, 0, pro)

def solve():
    from tqdm import tqdm
    go(0, 0, tqdm(total=n ** 9))
    print(ans)
def py_judge(a):
    return judge(a)
