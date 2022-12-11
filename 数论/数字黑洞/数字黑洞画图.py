from collections import defaultdict

import pydot
from tqdm import tqdm

"""
给定一个二进制数字，判断这个数字模n余几，这个问题可以使用有限状态自动机来描述
"""


def format_number(x, n):
    a = list(str(x))
    a = ['0'] * (n - len(a)) + a
    a = sorted(a)
    v = int(''.join(a))
    return v


def get_next(x, n):
    a = list(str(x))
    a = ['0'] * (n - len(a)) + a
    a = sorted(a)
    v = int(''.join(a))
    vv = int(''.join(a[::-1]))
    return format_number(vv - v, n)


def build(n, simplify=True):
    g = {}
    for i in tqdm(range(10 ** (n - 1), 10 ** n - 1)):
        x = format_number(i, n)
        if x in g:
            continue
        g[x] = get_next(i, n)
    if simplify:
        entrance = defaultdict(lambda: 0)
        for i in g.values():
            entrance[i] += 1
        a = []
        for k, v in g.items():
            if entrance[k] and entrance[v]:
                a.append((k, v, ''))
    else:
        a = []
        for k, v in g.items():
            a.append((k, v, ''))
    return a


def export(g) -> pydot.Dot:
    dot = pydot.Dot(graph_type='digraph')
    for i, j, label in g:
        dot.add_edge(pydot.Edge(i, j, label=label))
    return dot


def main():
    n = 8
    simplify = True
    g = build(n)
    dot = export(g)
    filename = f'数字黑洞{n}-{simplify}.jpg'
    dot.write(filename, prog="dot", format="jpg")


if __name__ == '__main__':
    main()
