import numpy as np

"""
小明始终朝着小红跑，小红沿着直线跑。
求小明的运动轨迹。
"""
a = [0, 0]  # 小明的初始位置
b = [1, 0]  # 小红的初始位置
v = 1
dt = 0.01
# x,y记录小明各个时刻的位置
x = []
y = []
for i in range(100):
    k = (b[1] - a[1]) / (b[0] - a[0])
    a[0] += dt * v * 1 / np.sqrt(1 + k * k)
    a[1] += dt * v * k / np.sqrt(1 + k * k)
    b[1] += dt * v
    x.append(a[0])
    y.append(a[1])
import matplotlib.pyplot as plt

xx = np.linspace(0, 0.9)
yy = 1 / 4 * (1 - xx) ** 2 - 1 / 2 * np.log(1 - xx) - 1 / 4
plt.plot(x, y)
plt.plot(xx, yy)
plt.show()
