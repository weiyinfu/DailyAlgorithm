import sympy as sp

x = sp.symbols("x")
"""
A=1
B=8
C=8

构建一个1，8，8的等腰三角形，顶角为A，两个底角为B、C。设BC=1. 
根据余弦定理构建方程。  

最终的方程为：
1 - 1/(2*x) - 32/x**2 + 168/x**4 - 336/x**6 + 330/x**8 - 176/x**10 + 52/x**12 - 8/x**14 + 1/(2*x**16)

此方程至多有16个解。 
其中前两个解比较正常，
然后是1/2+-二分之根号五，有两个解
x**4 + 4*x**3 - 4*x**2 - x + 1 有四个解
x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1 有8个解
=======
[-1, 
1/2, 
1/2 - sqrt(5)/2, 
1/2 + sqrt(5)/2, 
CRootOf(x**4 + 4*x**3 - 4*x**2 - x + 1, 0), 
CRootOf(x**4 + 4*x**3 - 4*x**2 - x + 1, 1), 
CRootOf(x**4 + 4*x**3 - 4*x**2 - x + 1, 2), 
CRootOf(x**4 + 4*x**3 - 4*x**2 - x + 1, 3), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 0), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 1), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 2), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 3), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 4), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 5), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 6), 
CRootOf(x**8 - 4*x**7 - 10*x**6 + 10*x**5 + 15*x**4 - 6*x**3 - 7*x**2 + x + 1, 7)]


===========
真实解为8次方程的最后一个根，使用sympy无法求出。
"""


def cos(a, b, c):
    return (a * a + b * b - c * c) / (2 * a * b)


cosA = cos(x, x, 1)
sinA = sp.sqrt(1 - cosA ** 2)
cosB = cos(x, 1, x)
cos2A = cosA ** 2 - sinA ** 2
sin2A = sp.sqrt(1 - cos2A ** 2)
cos4A = cos2A ** 2 - sin2A ** 2
sin4A = 2 * sin2A * cos2A
cos8A = cos4A ** 2 - sin4A ** 2
f = cos8A - cosB
f = f.simplify()
print(f)
print("=======")
ans = sp.solve(f, x)
print(ans)

print("======真实答案======")
real_ans = 1 / 2 / sp.cos(8 / 17 * sp.pi)
print(real_ans.evalf())
print(1 / 2 + 5 ** 0.5 / 2)
print('=======')
ff = cos8A - 1 / (2 * x)
print(ff.simplify())
