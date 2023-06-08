"""
甲乙丙三个人只能看见别人身上的数字，看不见自己身上的数字。
它们三个都知道：它们身上的数字可以构成等比数列。
上帝可以看见它们身上的数字分别为2,4,8。
上帝开始轮流问他们问题：你知道你自己身上的数字吗？
三个人只能回答：知道或者不知道。
问：三个人回答知道分别是在哪一次问询中？


此程序尝试解决，但是没有写完，太难写了
"""

max_value = 100  # 为了便于处理问题的上限，假设每个人的value都不超过100


def can_dengbi(a):
    b = sorted(a)
    return b[1] ** 2 == b[0] * b[2]


def get_space(a):
    # 给定一个数组，求可行解。把a中为None的部分都填充好
    ans = []

    def get(ind, now):
        if ind == len(a):
            if can_dengbi(now):
                ans.append(now)
            return
        if a[ind] is not None:
            get(ind + 1, now + [a[ind]])
            return
        for can in range(1, max_value):
            get(ind + 1, now + [can])

    get(0, [])
    return ans


class Person:
    def __init__(self, ind, others):
        self.ind = ind
        self.space = get_space([i[1] for i in others])
        self.others = others

    def do_you_know(self):
        return len(self.space) == 1

    def update(self, ind, ans):
        if ind == self.ind:
            # 自己对自己肯定没有信息增益
            return



def get_person(a, ind):
    return Person(ind, [(i, a[i] if i != ind else None) for i in range(len(a))])


def main():
    a = [2, 4, 8]
    persons = [get_person(a, i) for i in range(len(a))]
    for i in persons:
        print(i.space)
    input()
    while True:
        all_know = False
        for i in persons:
            resp = i.do_you_know()
            print(f"第{i.ind}个人回答{resp},他的可行解空间为：{i.space}")
            for j in persons:
                j.update(i.ind, resp)
            if not resp:
                all_know = False
        if all_know:
            break


if __name__ == '__main__':
    main()
