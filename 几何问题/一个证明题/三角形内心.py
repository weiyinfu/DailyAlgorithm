import numpy as np
import scipy.linalg as sl

A, B, C = np.random.random((3, 2))


def get_dis(A, B):
    return np.linalg.norm(A - B)


a, b, c = get_dis(B, C), get_dis(A, C), get_dis(A, B)
O = (a * A + b * B + c * C) / (a + b + c)


def point2line_square(O, A, B):
    # O点到直线AB的距离的平方
    return sl.det([
        [A[0], A[1], 1],
        [B[0], B[1], 1],
        [O[0], O[1], 1],
    ]) ** 2 / ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


print(point2line_square(O, A, B))
print(point2line_square(O, A, C))
print(point2line_square(O, B, C))
