from scipy.special import comb
import pylab as plt
"""
这是一种错误的答案

假设有x个人阳性，则x个人分成13组的概率最大的时候就是答案。

x个人分成13组的概率为：隔板法，x-1个空挡插入12个板子。等于C(x-1,12)
x个人分成1组的概率为：C(x-1,0)
x个人分成2组的概率为：C(x-1,1)
...
x个人分成x组的概率：C(x-1,x-1)

最终答案为C(x-1,12)/(2**(x-1))

当x等于24的时候此值最大。  

这种解法是错误的。  

"""
a = []

for i in range(13, 130):
    a.append((i, comb(i - 1, 12, exact=True) / 2 ** (i - 1)))
print(a)
ma = (0, 0)
for i in a:
    if i[1] > ma[1]:
        ma = i
print(ma)

plt.plot([i[0] for i in a], [i[1] for i in a])
plt.show()
