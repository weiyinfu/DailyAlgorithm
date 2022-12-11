"""
假设一个人是阴性的概率为x，则一管是阴性的概率为x^10,
现在一管是阴性的概率为1-0.13
则x=(1-0.13)**(1/10)
1000个人里面阳性的人数为：
1000*(1-x)


这种方法只能求出近似解，但是这个近似解也是非常精确，结果在两个数之间。
例如，如果有13管阳性，则阳性人数round近似值为14，但是实际答案为13.
"""
n = 100


def solve(sick):
    x = (1 - sick / n) ** (1 / 10)
    return 1000 * (1 - x)


def fix(sick):
    # 如果病人数为sick，那么100管里面期望有多少管是阳性。
    p = 1 - sick / 1000
    return (1 - p ** 10) * 100


def main():
    for sick in range(n + 1):
        print(sick, solve(sick))


def print_fix():
    print(fix(13))
    print(fix(14))


# print_fix()
main()
