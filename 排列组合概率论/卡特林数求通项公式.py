from typing import List

"""
卡特林数，1/(n+1)*C_2n^n
"""
def get(n):
    if n == 1 or n == 2:
        return 1
    s = 0
    for i in range(1, n):
        s += get(i) * get(n - i)
    return s


for i in range(10):
    print(i, get(i))
