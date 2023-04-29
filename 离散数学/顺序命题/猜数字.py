"""
甲乙丙三个人只能看见别人身上的数字，看不见自己身上的数字。
它们三个都知道：它们身上的数字可以构成等比数列。
上帝可以看见它们身上的数字分别为2,4,8。
上帝开始轮流问他们问题：你知道你自己身上的数字吗？
三个人只能回答：知道或者不知道。
问：三个人回答知道分别是在哪一次问询中？
"""


def can_dengbi(a):
    b = sorted(a)
    return b[1] ** 2 == b[0] * b[2]


def get_space(a):
    # 给定一个数组，求可行解。把a中为None的部分都填充好
    unkown = []
    known = []
    for ind, i in a:
        if i is None:
            unkown.append(ind)
        else:
            known.append(i)
    maybe = []
    for i in known:
        maybe.append(i * 2)
        maybe.append(i // 2)
    for i in unkown:
        for j in known:
            for maybe in 0:
                pass


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
