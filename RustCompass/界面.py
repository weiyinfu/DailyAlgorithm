from construction import solve, dis
import tkinter
import numpy as np

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
POINT_SIZE = 4
MA, MI = 0, 0
R = 0
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()


def data():
    global R, MA, MI
    for a, b, c in np.array([float(i) for i in open("construction-data.txt").read().split()]).reshape((-1, 3, 2)):
        point_list, event_list = solve(a, b, c)
        R = dis(a, c)
        MA, MI = max(point_list.reshape(-1)) + R, min(point_list.reshape(-1)) - R
        canvas.delete('all')
        for i in ((a, 'A'), (b, 'B'), (c, 'C')):
            put(*i[0], i[1])
        ei = 0
        for i in range(len(point_list)):
            while ei < len(event_list) and i == event_list[ei][1]:
                handle_event(event_list[ei])
                ei += 1
                yield None
            yield point_list[i]
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text='OVER')
    while 1:
        yield (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)


point_data = data()
last = None


def pos(x, y):
    return (x - MI) / (MA - MI) * CANVAS_WIDTH, (y - MI) / (MA - MI) * CANVAS_HEIGHT


def sz(w, h):
    return w / (MA - MI) * CANVAS_WIDTH, h / (MA - MI) * CANVAS_HEIGHT


def handle_event(e):
    print(e)
    if e[0] == '折线':
        ps = e[2]
        for i in range(0, len(ps) - 1):
            line(*ps[i], *ps[i + 1], 'brown')
    if e[0] == "多边形":
        print("多边形")
        ps = e[2]
        for i in range(0, len(ps)):
            line(*ps[i], *ps[(i + 1) % len(ps)], 'green')


def line(fx, fy, tx, ty, color='green'):
    fx, fy, tx, ty = *pos(fx, fy), *pos(tx, ty)
    canvas.create_line((fx, fy, tx, ty), fill=color, width=2)


def put(x, y, desc=None):
    global last
    if last:
        canvas.delete(last)
        last = None
    x, y = pos(x, y)
    wr, hr = sz(R, R)
    last = canvas.create_oval((x - wr, y - hr, x + wr, y + hr), outline='red', width=3)
    canvas.create_oval((x - POINT_SIZE, y - POINT_SIZE, x + POINT_SIZE, y + POINT_SIZE), fill='red')
    if desc:
        canvas.create_text(x + 10, y + 10, text=desc, fill='blue', width='10')


def clk(e):
    p = next(point_data)
    if p is not None:
        put(*p)


window.bind('<Button-1>', clk)
window.bind("<KeyRelease>", clk)
window.mainloop()
