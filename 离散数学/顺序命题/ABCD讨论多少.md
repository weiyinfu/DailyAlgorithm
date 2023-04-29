四个人A、B、C、D各自有若干个球，已知他们的球的总数为20.  
A说：你们三个肯定有人比我球多。  
B说：听完你说的，我才刚刚意识到肯定也有人比我球多。  
C说：听完你们两个说的，我才刚刚意识到我的球是最多的。  
D说：听完你们三个说的，我才刚刚意识到我的球是最少的。

问，ABCD四个人分别有多少个球？

这道题巧妙之处与红眼人、蓝眼人有异曲同工之妙，妙就妙在每个人都只能知道自己的，通过别人说的话产生信息增益，从而自己又能继续产生信息增益，最终所有人都得到了结果。

思路：把每一句话变成一个命题，最终得到一个命题集合。要求这些命题集合全部为True。  
A,B,C,D四个命题都成立。  
如果A命题不成立，则B命题不成立。
如果A命题成立，B命题不成立，则C命题不成立。
如果AB命题成立，C命题不成立，则D命题不成立。

我称这个问题为顺序命题。

如果把这个问题改为，四个人有N个球。怎么样构造ABCD四个人的句子，才能保证四个人的球数有唯一的解法 ？

# 在这道题的框架下，微调参数可以得到新问题

调整总数，可以得到新问题。 在100范围内，仅有16、20两个数字是有解的。

```plain
16 [(3, 4, 7, 2)]
20 [(4, 5, 9, 2)]
```

# 从顺序命题进一步延伸
这道题中，ABCD是顺序的，实际上他们完全可以组成一个图。  
在这个图中有依赖关系，例如A先说，B和C这时候同时说出了自己的命题，D没有听见B说的，只根据C说的得出了另一个命题。
E没有听见C说的，只根据B说的得出了自己的命题。  
F听见了所有人说的，得出了自己的命题。  

# 问题构造
根据若干个命题，在一个问题空间中求解真实答案， 这种问题的构造其实是比较简单的。  
如果约束太紧了，那么就把约束改的松一些；如果约束太松了就把问题改的简单一些。    

# 解法概述
首先定义A,B,C,D四个命题。命题的输入参数为可行域，返回值为一个bool值。  
表明在这个可行域上，命题是否一定成立。

使用Python很容易实现逆命题
```
def not_predicate(f):
    def ff(*args, **kwargs):
        return not f(*args, **kwargs)

    return ff
```

给定一个可行域，给定一个命题，求满足命题的可行的数值有哪些。  
p表示可行域，也就是问题的所有的可能解的集合。  
ind表示当前要考察哪一个数字的可行的数值。  
predicate表示需要满足的命题。  
返回第ind个数字满足命题predicate的可行的数值有哪些。
```
def get_can_values(p, ind, predicate):
    ma = defaultdict(lambda: [])
    for i in p:
        ma[i[ind]].append(i)
    can_set = [i for i, cand in ma.items() if predicate(cand)]
    return set(can_set)

```

主过程
```python
p = get_all(total) # 得到所有的可行解，total=20，表示总数
print(f"最开始有{len(p)}种可能") # 这个数字的上限为total^3
Acan = get_can_values(p, 0, A) # 获取满足A命题时，第0个数字的可行值
lastp = p
p = [i for i in p if i[0] in Acan] # 利用A命题缩小可行解范围
print("a=", Acan)
print(f"经过A之后有{len(p)}种可能")
Bcan = get_can_values(p, 1, B) # 满足B命题时，第1个数字的可行值
Bcan2 = get_can_values(lastp, 1, not_predicate(B)) # 如果A没有说话，那么B命题是无法成立的。满足这个约束时，第1个数字的可行值
Bcan = Bcan.intersection(Bcan2) # 两个约束求交集
lastp = p
p = [i for i in p if i[1] in Bcan]
print("b=", Bcan)
print(f"经过B之后有{len(p)}种可能")
Ccan = get_can_values(p, 2, C) # 满足C命题时，第2个数字的可行值。
Ccan2 = get_can_values(lastp, 2, not_predicate(C)) # 如果B没有说话，那么C命题是无法成立的，满足这个约束时，第2个数字的可行值
Ccan = Ccan.intersection(Ccan2) # 两个约束求交集
lastp = p
p = [i for i in p if i[2] in Ccan] 
print("c=", Ccan)
print(f"经过C之后有{len(p)}")
Dcan = get_can_values(p, 3, D)
Dcan2 = get_can_values(lastp, 3, not_predicate(D))
Dcan = Dcan.intersection(Dcan2)
lastp = p
p = [i for i in p if i[3] in Dcan]
print("d=", Dcan)
print(f"经过D之后有{len(p)}种可能")
print(p)
return p

```