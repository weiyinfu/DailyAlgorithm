from scipy import special as sp

"""
n个数字，摸k个,依次出示k-1个让别人猜测最后一个数字
"""


def solve(k):
    c = sp.factorial(k - 2, exact=True)
    value = c * 2 + 1
    color = k - 1
    return color * value


for i in range(2, 10):
    print(i, solve(i), sp.factorial(i - 1, exact=True))
