from math import *
import tkinter
import matplotlib.pyplot as plt
from tkinter.font import Font

r = 1  # 操场半径为r
a = (0, 0)  # 小明的初始位置
b = (r, 0)  # 小红的初始位置
v1 = 0.9  # 小明的速度
v2 = 1.1  # 小红的速度
dt = 0.001  # 时间dt
t = 0  # 当前的时间
eps = 1e-1

##########UI
update_dt = 1  # UI的更新速度
R = 200  # UI的实际宽度
a_oval, b_oval = None, None  # 小明的位置和小红的位置，都是两个圆


def model():
    global t, a, b
    w = v2 / r  # 小红的角速度
    while 1:
        # 小红的新位置
        b = r * cos(w * t), r * sin(w * t)
        # 小明的方向
        dir = b[0] - a[0], b[1] - a[1]
        dir = dir[0] / hypot(dir[0], dir[1]), dir[1] / hypot(dir[0], dir[1])
        # 小明的新位置
        a = (a[0] + v1 * dir[0] * dt, a[1] + v1 * dir[1] * dt)
        t += dt
        # 如果追上了
        if hypot(a[0] - b[0], a[1] - b[1]) < eps:
            break
        else:
            yield a, b
    print('追上所花费的时间', t)
    yield None, None


def pos(x, y):
    # 把数学中的坐标系转换成UI中的坐标系
    return x / r * R + R, y / r * R + R


ui_model = None


def init():
    global a_oval, b_oval, ui_model
    global v1, v2, a, b, t
    v1, v2 = float(v1_str.get()), float(v2_str.get())
    a, b = (0, 0), (r, 0)
    t = 0
    ui_model = model()
    canvas.delete(tkinter.ALL)
    (ax, ay), (bx, by) = pos(*a), pos(*b)
    a_oval = canvas.create_oval(ax - 5, ay + 5, ax + 5, ay + 5, fill='white')  # 小明
    b_oval = canvas.create_oval(bx - 5, by + 5, bx + 5, by + 5, fill='red')  # 小红
    # 圆心的位置
    canvas.create_oval(ax - 5, ay - 5, ax + 5, ay + 5, fill='blue')
    # 操场
    canvas.create_oval(ax - R, ay - R, ax + R, ay + R, outline='yellow')
    # 小明有希望达到的半径
    v1r = v1 / (v2 / r) / r * R
    canvas.create_oval(ax - v1r, ay - v1r, ax + v1r, ay + v1r, outline='green')


def update():
    # 调用UI模型获取小红和小明的新位置
    a_pos, b_pos = next(ui_model)
    if not a_pos:
        return
    (ax, ay), (bx, by) = pos(*a_pos), pos(*b_pos)
    # 更改UI中两个小圆圈的位置
    canvas.coords(a_oval, (ax - 5, ay - 5, ax + 5, ay + 5))
    canvas.coords(b_oval, (bx - 5, by - 5, bx + 5, by + 5))
    timer_id.append(root.after(update_dt, update))


def do_model():
    # 开始模拟
    if timer_id:
        print('正在取消')
        for tid in timer_id:
            root.after_cancel(tid)
        timer_id.clear()
    init()
    timer_id.append(root.after(update_dt, update))


def ui():
    global timer_id
    do_model()
    root.mainloop()


root = tkinter.Tk()
root.wm_title('圆形操场追人问题')
root.resizable(width=False, height=False)
v1_str = tkinter.StringVar(value=str(v1))
v2_str = tkinter.StringVar(value=str(v2))
font = Font(family='helvetica', size=20)
tkinter.Label(root, text="小明的速度", font=font).grid(row=0, column=0)
tkinter.Label(root, text="小红的速度", font=font).grid(row=1, column=0)
tkinter.Button(root, text="模拟", command=do_model, font=font).grid(row=2, columnspan=2)
tkinter.Entry(root, textvariable=v1_str, font=font).grid(row=0, column=1)
tkinter.Entry(root, textvariable=v2_str, font=font).grid(row=1, column=1)
canvas = tkinter.Canvas(root, width=2 * R, height=2 * R, bg='black')
canvas.grid(row=4, columnspan=2)

timer_id = []

ui()
