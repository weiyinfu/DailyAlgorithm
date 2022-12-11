"""
一个集合有n个元素，从中选择若干个元素

直接-1加且就可以遍历所有组合，复杂度为O(2^n)，远比写一个递归函数便捷得多。
"""
x = 0b10011001
n = 10
j = x
l = x
ans = []
while j:
    print(bin(j))
    j = (j - 1) & l
    ans.append(j)
print(len(ans))
# 2**4=16
print(bin(x)[2:].count('1'))
