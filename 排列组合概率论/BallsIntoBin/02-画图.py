from balls2bin import bruteforce, exact
import pylab as plt
import numpy as np


def draw():
    for i in range(3, 20):
        p = bruteforce.solve(i, i)
        print(f"{i}=>{p}")
        plt.scatter(i, p)
    x = np.linspace(3, 20, 100)
    y = (np.log(np.log(x))) / np.log(x)
    plt.plot(x, y)
    plt.show()


draw()
