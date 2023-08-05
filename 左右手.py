"""
你和你的小伙伴（甲和乙），要参加一个节目，叫默契挑战。挑战的规则是这样的：
节目开始后，甲和乙上台，台上有一个人丙，丙拿出一张纸条给乙看但不给甲看，纸条上面按顺序写有5个字，每个字是“左"或"右”。乙看后不能与甲交流。接下来的5轮，甲、乙、丙要依次伸出左手或右手，丙会严格按照纸条上的顺序出左或者右。每轮如果甲、乙、丙三人出的都一样，则得1分，如果任意两人不一样，则不得分。5轮以后，得到3分或以上视为挑战成功，不足3分则为挑战失败。
假设丙的纸条为随机生成，即32种组合均匀分布。如果节目开始之前，甲乙二人可以充分商讨策略，请问甲乙使用最佳策略，挑战成功的概率是多少？


应该有必胜策略. 甲先固定一个策略, 比如是RRRRR, 每一次如果猜对了, 就接着按照固定策略出, 如果猜错了, 下一轮按照乙的指示出, 这样除非丙的1/3/5轮都是L的情况以外都能cover; 如果是丙的1/3/5轮都是L的话, 乙在第一轮故意告诉甲一个错误答案, 这样甲在第二轮发现乙告诉的是错的, 就知道第三轮和第五轮都应该是L了, 然后乙在第二轮告诉甲第四轮的结果, 即可必胜


正解更简洁：第一轮甲随便出，234轮哪个多乙就出哪个，并让甲234轮都出这个。234轮中，乙能得分就得分，不能得分则告诉甲第5轮的答案。

"""
import numpy as np


def math_solve():
    dp = np.zeros((5, 5, 2))  # (i,j,k),i表示轮次，j表示从1到i已经胜利几轮，k表示最后一轮是否正确，dp(i,j,k)表示这个离散事件发生的概率
    for turn in range(5):
        if turn == 0:
            dp[0][0][0] = 1 / 2
            dp[0][1][1] = 1 / 2
        else:
            for j in range(turn):
                dp[turn][j + 1][1] += dp[turn - 1][j][0]  # 上一轮错了，这一轮必对
                dp[turn][j][0] += dp[turn - 1][j][1] * 1 / 2  # 蒙错了
                dp[turn][j + 1][1] += dp[turn - 1][j][1] * 1 / 2  # 蒙对了
    s = np.sum(dp[-1][3:])
    return s


def brute():
    def get_rate(x, count=1000):
        winwin = 0
        for i in range(count):
            last_right = True
            win = 0
            for j in range(5):
                if not last_right:
                    last_right = True
                    win += 1
                    continue
                guess = np.random.randint(0, 2)
                if guess and x & (1 << j):
                    last_right = True
                    win += 1
                else:
                    last_right = False
            if win >= 3:
                winwin += 1
        return winwin / count

    rate_sum = 0
    for i in range(2 ** 5):
        now = get_rate(i)
        rate_sum += now
        print(i, now)
    return rate_sum / (2 ** 5)


print(math_solve())
print(brute())
