import numpy as np
import scipy.linalg as lg


def get_area(A, B, C):
    # 给定三个点求面积
    return lg.det([
        [A[0], A[1], 1],
        [B[0], B[1], 1],
        [C[0], C[1], 1],
    ]) / 2


def get_dis(A, B):
    return np.hypot(A[0] - B[0], A[1] - B[1])


def hellen(A, B, C):
    a = get_dis(A, B)
    b = get_dis(A, C)
    c = get_dis(B, C)
    p = (a + b + c) / 2
    return np.sqrt(p * (p - a) * (p - b) * (p - c))


A, B, C = np.random.random((3, 2))

one = hellen(A, B, C)
print(one)
print(get_area(A, B, C))
