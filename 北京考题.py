import numpy as np
from tqdm import tqdm

n = 17


def get():
    return np.random.choice(np.arange(1, n + 1), n)


def getset(x):
    xset = set()
    for i in range(len(x)):
        for j in range(i, len(x)):
            xset.add(sum(x[i:j + 1]))
    return xset


def ok(x, y):
    xset = getset(x)
    yset = getset(y)
    z = xset & yset
    return len(z) > 0


def main(cas=100000):
    for i in tqdm(range(cas)):
        x = get()
        y = get()
        if not ok(x, y):
            print(x, y)


main()
