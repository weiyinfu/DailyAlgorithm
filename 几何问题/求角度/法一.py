from sympy import *

"""
设角A为a
"""
x, a, b = symbols('x a b')
t = (2 * cos(a)) ** 2  # AD线段的距离


def co(a, b, c):  # 根据三角形三条边求角的余弦值
    return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)


one = Eq(cos(pi - 2 * a), co(1 - t, t, x))  # 三角形DCE，求角C的余弦定理，t表示AD。x表示DE这条边的长度
x = solve(one, x)[1]
two = Eq(cos(b), co(x, 2 * cos(a), 1 - t))  # 三角形BDE，求角BDE的余弦定理
b = solve(two, b)[1]
print(b)
ans = b.subs({
    a: rad(70)
})
print(ans, ans.evalf())
