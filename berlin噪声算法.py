import math

import numpy as np
import pylab as plt

"""
柏林噪声（Perlin Noise）算法是 Ken Perlin 发明的一种自然噪声生成算法，并在图形学领域广泛使用。例如模拟火焰、云彩的纹理、生成随机地形图等。
https://en.wikipedia.org/wiki/Perlin_noise
"""
rows = 15
cols = 15
ratio = 34
a = np.random.random((rows, cols, 2))
a /= np.linalg.norm(a, axis=2, keepdims=True)
rs = int(ratio * (rows - 1))
cs = int(ratio * (cols - 1))
b = np.zeros((rs, cs))
for (i, j), v in np.ndenumerate(b):
    x, y = i / ratio, j / ratio
    fx, tx = math.floor(x), math.ceil(x)
    fy, ty = math.floor(y), math.ceil(y)
    vw = []
    for p in (fx, tx):
        for q in (fy, ty):
            vw.append((np.dot(a[p, q], (x - p, y - q)), (1 - abs(x - p)) * (1 - abs(y - q))))
    vw = np.array(vw)
    vw[:, 1] /= np.sum(vw[:, 1])
    b[i, j] = np.sum(vw[:, 0] * vw[:, 1])
plt.imshow(b)
plt.show()
