f = {}

"""
Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 stones ，其中 stones[i] 是第 i 个石子的价值。

Alice 和 Bob 轮流进行自己的回合，Alice 先手。每一回合，玩家需要从 stones 中移除任一石子。

如果玩家移除石子后，导致 所有已移除石子 的价值 总和 可以被 3 整除，那么该玩家就 输掉游戏 。
如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
假设两位玩家均采用 最佳 决策。如果 Alice 获胜，返回 true ；如果 Bob 获胜，返回 false 。


https://leetcode-cn.com/contest/weekly-contest-261/problems/stone-game-ix/
"""
def solve(x, y, z, who, s):
    # 判断是否必胜
    if x + y + z == 0:
        return True if who == 1 else False
    k = (x, y, z, who, s % 3)
    if k in f:
        return f[k]
    ans = False
    if x > 0 and not ans:
        # use 3
        ans = not solve(x - 1, y, z, 1 - who, s)
    if y > 0 and not ans and s % 3 in (0, 1):
        ans = not solve(x, y - 1, z, 1 - who, s + 1)
    if z > 0 and not ans and s % 3 in (0, 2):
        ans = not solve(x, y, z - 1, 1 - who, s + 2)
    f[k] = ans
    return ans


for i in range(5):
    for j in range(5):
        for k in range(5):
            solve(i, j, k, 0, 0)
ans_list = []
for k, v in f.items():
    x, y, z, who, s = k
    if who == 1:
        continue
    if s % 3 != 0:
        continue
    ans_list.append((x, y, z, v))


def go(x, y, z):
    def get(x, y, z):
        # 如果先选y，能够达到的最大长度
        s = x
        if y == 0: return 0
        yy = y - 1
        if yy >= z:
            s += 1 + z * 2 + min(1, yy - z)
        else:
            s += 1 + yy * 2
        return s

    one = get(x, y, z)
    two = get(x, z, y)
    print(one, two)
    if one == x + y + z:
        one_ans = False
    else:
        one_ans = one % 2 == 1
    if two == x + y + z:
        two_ans = False
    else:
        two_ans = two % 2 == 1
    return one_ans or two_ans


for x, y, z, v in ans_list:
    print(x, y, z, v, go(x, y, z))
go(1, 1, 3)
