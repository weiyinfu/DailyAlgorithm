from scipy import special as sp


def one():
    a = sp.comb(52, 5, exact=True)
    b = sp.comb(52, 4, exact=True)
    print(a, b)
    """
    能否用270725表示2598960种状态，答案是否定的
    """
    print(a / b)


def ar(n, k):
    s = 1
    for i in range(k):
        s *= n - k
    return s


def two():
    a = ar(52, 5)
    b = ar(52, 4)
    print(a / b)


two()
