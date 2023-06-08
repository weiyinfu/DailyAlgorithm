import numpy as np


def solve(a, depth):
    if len(a) == 6:
        return max(a) + min(a), []
    ans_value = None
    ans = None
    for ind, i in enumerate(a):
        for j in np.linspace(0, i, 50):
            now, op = solve(a[:ind] + a[ind + 1:] + [j, i - j], depth + 1)
            if depth % 2 == 0:
                if ans_value is None or ans_value < now:
                    ans_value = now
                    ans = [(i, j)] + op
            else:
                if ans_value is None or ans_value > now:
                    ans_value = now
                    ans = [(i, j)] + op
    return ans_value, ans


def main():
    ans_value, ans = solve([1], 0)
    for x, y in ans:
        print(f"把{x}切成{y}+{x - y}")


main()
