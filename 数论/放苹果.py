"""
共有101箱苹果，总重为200公斤，每箱苹果的公斤数都是正整数。用一台处于平衡状态的空天平，然后按从重到轻的顺序把苹果逐箱放到天平两边，并且每次都放在天平较轻的一边，当天平处于平衡状态时可以放在任意一边。求证:当所有苹果箱都放到天平上时，天平每边苹果重量均为100公斤。

"""

import numpy as np


def get_question():
    a = np.arange(1, 200)
    b = np.random.choice(a, 100, False)
    b.sort()
    c = [b[0]]
    for i in range(1, len(b)):
        c.append(b[i] - b[i - 1])
    c.append(200 - b[-1])
    c.sort(reverse=True)
    return c


def run(a):
    x = a[0]
    for i in range(1, len(a)):
        x = abs(x - a[i])
    return x


def main():
    for i in range(100):
        x = get_question()
        print(run(x))


main()
