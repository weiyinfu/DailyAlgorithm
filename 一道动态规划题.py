"""
给定一个字符串aabbbccdef，它可以压缩表示为：2a3b2c1d1e1f
现在要删掉k个字符，使得字符串的压缩表达形式尽量短。例如输入aabbaa和k=2，删掉中间的两个bb，则字符串压缩形式为4a，这就是最短表示。
输入：一个只包含小写字母的字符串，和一个int（表示k）。
输出：一个int，表示删除k个字符之后压缩表达形式的长度。
"""


def solve(s, k):
    ma = {}

    def go(ind, k, tail, tail_count):
        kk = (ind, k, tail, tail_count)
        if kk in ma:
            return ma[kk]
        if ind == len(s):
            return len(str(tail_count)) + 1
        ans = 1e9
        if s[ind] == tail:
            # 不删除
            now = go(ind + 1, k, tail, tail_count + 1)
            ans = min(ans, now)
            if k > 0:
                # 删除
                now = go(ind + 1, k - 1, tail, tail_count)
                ans = min(ans, now)
        else:
            # 不删除
            now = go(ind + 1, k, s[ind], 1) + len(str(tail_count)) + 1
            ans = min(ans, now)
            # 删除
            if k > 0:
                now = go(ind + 1, k - 1, tail, tail_count)
                ans = min(ans, now)
        ma[kk] = ans
        return ans

    return go(0, k, '$', 1) - 2


def main():
    s = input()
    k = int(input())
    ans = solve(s, k)
    print(ans)


main()
