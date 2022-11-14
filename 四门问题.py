import numpy as np
from tqdm import tqdm

"""

https://juejin.cn/post/7159849768016379911/


四门问题

如果不换门，中奖的概率为1/4。
所以只需要考虑换门中奖的概率是多少。

n门问题更换门之后的中奖概率提高了：
P=[(n-1)/n]×[1/(n-2)]=(n-1)/[n(n-2)]  

换门的中奖概率：
f(3)=2/3
f(4)=3/8
f(5)=4/15


换门比不换门中奖概率高
1/(n*(n-2))
"""
N = 4


def generate():
    a = [0] * N
    a[np.random.randint(0, N)] = 1
    return a


def one():
    # 生成一个随机问题，返回不换门中奖的概率
    a = generate()
    # 让用户从中选择一个
    ind = np.random.randint(0, len(a))
    # 主持人随机推开一个空门
    empty = []
    for i, v in enumerate(a):
        if i == ind:
            continue
        elif v == 0:
            empty.append(i)
    # 主持人推开的门的下标
    rm = empty[np.random.randint(0, len(empty))]
    # 场上剩余的门
    left = [v for i, v in enumerate(a) if i != rm and i != ind]
    # 换门
    change = np.random.randint(0, len(left))
    return left[change]


def main():
    s = 0
    n = 100000
    for i in tqdm(range(n)):
        s += one()
    print('如果换门中奖的概率为', s / n)


main()
