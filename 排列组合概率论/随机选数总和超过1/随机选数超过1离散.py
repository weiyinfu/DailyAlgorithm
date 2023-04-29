"""
每次选择到的数字是离散值0，1.期望选择多少次才能使得和超过1.

答案是4次。
"""


def P(n):
    return (n - 1) * (1 / 2) ** n


def S():
    s = 0
    for i in range(1, 100):
        s += i * P(i)
    print(s)


S()
