from collections import defaultdict


def A(a):
    # 你们中一定有人比我大
    return all(max(i[1], i[2], i[3]) > i[0] for i in a)


def B(a):
    # 你们中一定有人比我大
    return all(max(i[0], i[2], i[3]) > i[1] for i in a)


def C(a):
    # 我刚知道我是最大的
    return all(max(i[0], i[1], i[3]) < i[2] for i in a)


def D(a):
    """
    我刚刚知道原来我是最小的
    :param a:
    :return:
    """
    return all(min(i[0], i[1], i[2]) > i[3] for i in a)


def get_all(total):
    ans = []
    for A in range(1, total):
        for B in range(1, total - A):
            for C in range(1, total - A - B):
                D = total - A - B - C
                if min(A, B, C, D) == 0:
                    continue
                ans.append((A, B, C, D))
    return ans


def get_can_values(p, ind, predicate):
    ma = defaultdict(lambda: [])
    for i in p:
        ma[i[ind]].append(i)
    can_set = [i for i, cand in ma.items() if predicate(cand)]
    return set(can_set)


def not_predicate(f):
    def ff(*args, **kwargs):
        return not f(*args, **kwargs)

    return ff


def main(total):
    p = get_all(total)
    print(f"最开始有{len(p)}种可能")
    Acan = get_can_values(p, 0, A)
    lastp = p
    p = [i for i in p if i[0] in Acan]
    print("a=", Acan)
    print(f"经过A之后有{len(p)}种可能")
    Bcan = get_can_values(p, 1, B)
    Bcan2 = get_can_values(lastp, 1, not_predicate(B))
    Bcan = Bcan.intersection(Bcan2)
    lastp = p
    p = [i for i in p if i[1] in Bcan]
    print("b=", Bcan)
    print(f"经过B之后有{len(p)}种可能")
    Ccan = get_can_values(p, 2, C)
    Ccan2 = get_can_values(lastp, 2, not_predicate(C))
    Ccan = Ccan.intersection(Ccan2)
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


def find_problem():
    for total in range(4, 100):
        pos = main(total)
        if 0 < len(pos) < 3:
            print("found", total, pos)


# main(20)
find_problem()
