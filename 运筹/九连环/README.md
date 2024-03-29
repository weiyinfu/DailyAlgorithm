九连环、汉诺塔、华容道、拼图、魔方是非常有趣的解谜游戏，并且是单人游戏。  

九连环的核心：只能改变第一个1后面的状态。  
所以一个结点，只有两个子节点：要么让第一个元素上去，要么让现在的1后面的状态反转。  
例如10011，可以到达00011和11011两种状态；0001011可以到达1001011和0001111两种状态。  

# N连环的状态总数
2^N
# N连环最优解步数
1 1
2 2
3 5
4 10
5 21
6 42
7 85
8 170
9 341
10 682
11 1365
12 2730
13 5461
14 10922
15 21845

递推公式：
f(1)=1  
f(2n)=f(2n-1)*2  
f(2n+1)=f(2n)*2+1  


通项公式：
`f(n)=[2^(n+1)-2+n%2]/3`  

通过N连环的递推公式能够看出来一些结论：
* 如果是2n，把最后一个环拿下来需要f(2n-1)步，然后再把倒数第二个环拿下来有需要f(2n-1)步

# 九连环操作的表示
直接使用一个数组表示，例如`[1,2,3]`，表示依次反转每个元素的状态。
# 九连环可执行的操作
给定一个九连环的状态，它可执行的操作有两种：
* 反转第一个元素
* 反转第一个1后面的那个元素的状态
```
def get(a):
    ans = []
    for i in range(len(a) - 1):
        if a[i] == 1:
            nex = np.copy(a)
            nex[i + 1] = 1 - nex[i + 1]
            ans.append((nex, i + 1))
            break
    nex = np.copy(a)
    nex[0] = 1 - nex[0]
    ans.append((nex, 0))
    return ans
```

# N连环的最简操作步骤
N连环的解法其实就是格雷码。  
格雷码每次变化都只有一位发生改变。  

```python
def grey(n):
    return n ^ (n >> 1)


def print_path(n):
    ans = solve([1] * n)
    a = [1] * n
    x = (1 << n) - 1
    for ind, i in enumerate(ans):
        a[i - 1] = 1 - a[i - 1]
        x ^= 1 << (i - 1)
        g = grey(len(ans) - 1 - ind)
        print(a, bin(x), bin(g))

```
因为格雷码的存在，对于任意阶的N连环，都可以无需打表，直接计算求出最佳路径。  