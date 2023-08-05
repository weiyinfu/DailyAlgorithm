"""
TODO:实现manacher算法

"""
def solve(s):
    def get_odd(x):
        for j in range(len(s)):
            p, q = x - j, x + j
            if p < 0 or q >= len(s) or s[x - j] != s[x + j]:
                return s[p + 1:q]
        return s[x]

    def get_even(x):
        for j in range(len(s)):
            p, q = x - j, x + 1 + j
            if p < 0 or q >= len(s) or s[p] != s[q]:
                return s[p + 1:q]
        return ""

    ans = ""
    for i in range(len(s)):
        x = get_odd(i)
        y = get_even(i)
        if x and len(x) > len(ans):
            ans = x
        if y and len(y) > len(ans):
            ans = y
    return ans


def main():
    s = "uiasisuuia"
    ans = solve(s)
    print(ans)

# todo:manacher算法
main()
