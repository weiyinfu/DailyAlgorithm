"""
I forget the problem.
I cannot find the original image.
I will draw it by skimage
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.draw import draw

w, h = 240, 240
cx, cy = w // 2, h // 2
img = np.zeros((w, h))
rec = draw.rectangle_perimeter((10, 10), (w - 10, h - 10), )
img[rec] = 1
circle = draw.circle_perimeter(cx, cy, (w - 20) // 2)
img[circle] = 1
x, y = draw.circle_perimeter(w - 10, 10, w - 20)
x_ind = np.logical_and(x >= 10, x <= w - 10)
y_ind = np.logical_and(y >= 10, y <= h - 10)
ind = np.logical_and(x_ind, y_ind)
img[x[ind], y[ind]] = 1
"""
描红
"""
A = (w - 10, 10, w - 20)
B = (cx, cy, (w - 20) // 2)


def in_circle(c, p):
    cx, cy, r = c
    return np.hypot(p[0] - cx, p[1] - cy) < r


for x in range(w):
    for y in range(w):
        p = (x, y)
        if in_circle(B, p) and not in_circle(A, p):
            img[x][y] = 1
img = 1 - img
io.imshow(img)
plt.axis('off')
plt.savefig("circle.png")
plt.show()
