import math
import cmath
import numpy as np


class Point:
    def __init__(this, x, y, i, c, out):
        this.x = x
        this.y = y
        this.pos = complex(x, y)
        this.i = i
        this.c = c
        # create point
        out.write("{c}# {x:.10f} {y:.10f} {i}\n".format(c=c, x=x, y=y, i=i))

    def __str__(this):
        x = this.x
        y = this.y
        i = this.i
        c = this.c
        return "<Point {x:.10f} {y:.10f} <{i}> {c}>".format(x=x, y=y, i=i, c=c)

    def __repr__(this):
        return this.__str__()

    def find(this):
        x = this.x
        y = this.y
        i = this.i
        c = this.c
        return "D {x:.10f} {y:.10f} {i}".format(x=x, y=y, i=i)


def run(p, out):
    a = Point(p[0][0], p[0][1], "P 1", 1, out)
    b = Point(p[1][0], p[1][1], "P 2", 2, out)
    c = Point(p[2][0], p[2][1], "P 3", 3, out)
    nextCircle = 4
    unit = abs(c.pos - a.pos)  # 距离

    def r60(p1, p2):
        nonlocal nextCircle
        nonlocal out
        pos = (p2.pos - p1.pos) * cmath.rect(1, math.pi / 3) + p1.pos
        c1 = p1.c
        c2 = p2.c
        prt = Point(pos.real, pos.imag, "C {c1} {c2}".format(c1=c1, c2=c2), nextCircle, out)
        nextCircle += 1
        return prt

    def ext(p1, p2):
        p3 = r60(p2, p1)
        p4 = r60(p2, p3)
        return r60(p2, p4)

    def inter(p1, p2):
        nonlocal unit
        nonlocal nextCircle
        nonlocal out
        dis = abs(p1.pos - p2.pos)
        if dis > 2 * unit:
            raise Exception("baga")
        c1 = p1.c
        c2 = p2.c
        angle = math.acos(dis / (2 * unit))
        pos = cmath.rect(unit / dis, angle) * (p2.pos - p1.pos) + p1.pos
        prt = Point(pos.real, pos.imag, "C {c1} {c2}".format(c1=c1, c2=c2), nextCircle, out)
        nextCircle += 1
        return prt

    def dim(p1, p2, p3):
        nonlocal nextCircle
        nonlocal out
        c2 = p2.c
        c3 = p3.c
        trans = (p1.pos - p2.pos) / (p3.pos - p2.pos)
        pos = p2.pos + (p3.pos - p2.pos) * trans.conjugate()
        prt = Point(pos.real, pos.imag, "C {c2} {c3}".format(c2=c2, c3=c3), nextCircle, out)
        nextCircle += 1
        return prt

    def makelink(p1, p2, l):
        link = []
        if l == 0:
            link.append(p1)
        elif l > 0:
            link.append(p1)
            link.append(p2)
            remain = l - 1
            pendd = p1
            pend = p2
            while remain > 0:
                pnext = ext(pendd, pend)
                pendd = pend
                pend = pnext
                link.append(pnext)
                remain -= 1
        elif l < 0:
            prev = ext(p2, p1)
            return makelink(p1, prev, -l)
        return link

    def makechain(p1, p2, u, v):
        link = makelink(p1, p2, u)
        v1 = r60(p1, p2)
        v2 = r60(v1, p2)
        e1 = link[-1]
        e2 = makelink(v1, v2, u)[-1]
        link1 = makelink(e1, e2, v)
        return (link[:-1]) + link1

    xy = (b.pos - a.pos) / (c.pos - a.pos)
    v = 2 * xy.imag / math.sqrt(3)
    u = xy.real - xy.imag / math.sqrt(3)
    chain = makechain(a, c, u, v)
    last = chain[:-1]
    inte = inter(chain[-1], b)
    chain.append(inte)
    chain.append(b)
    between = chain[1:-1]
    points = [r60(chain[i], chain[i + 1]) for i in range(len(chain) - 1)]
    while len(between) > 0:
        nextpoints = [dim(between[i], points[i], points[i + 1]) for i in range(len(between))]
        between = points[1:-1]
        points = nextpoints
    pfind = points[0]
    out.write(pfind.find() + "\n")


data = np.array(list(map(lambda x: float(x), open("construction-data.txt").read().split()))).reshape(-1, 3, 2)
with open("out.txt", mode="w", encoding="utf-8") as output:
    for i in data:
        run(i, output)
