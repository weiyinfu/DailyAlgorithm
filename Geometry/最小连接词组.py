import copy

import numpy as np
from tqdm import tqdm

"""

所谓置换，实际上就是一元运算符

最小连接词组，就是魔方的最小操作集。基于一个置换集合可以到达全部置换。

而最小连接词组就是二元运算符。


正经来说有28个最小连接词组
按照 逆条件=条件，非逆条件=非条件，有17个连接词。

如何记忆？共17个
一级高手（2）个：非且、非或
二级高手（9）个：非4大金刚：非，与；非，或；非，条件；非，非条件
        条件，非条件
        异或，非条件；同或，条件
        永真，条件；永假，非条件
        
三级高手（6）个：与，同或，异或；与，同或，永假；与，异或，永真
        或，同或，异或；或，同或，永假；或，异或，永真
"""
A = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
namemap = {
    '0000': '永假',
    '0001': '与',
    '0010': '逆条件',
    '0011': 'A',
    '0100': '条件',
    '0101': 'B',
    '0110': '异或',
    '0111': '或',
    '1000': '非或',
    '1001': '同或',
    '1010': '非B',
    '1011': '非条件',
    '1100': '非A',
    '1101': '非逆条件',
    '1110': '非且',
    '1111': '永真'
}


def to(x):
    return int(''.join([str(i) for i in x]), base=2)


def parse(x):
    # 把数字转为操作
    a = []
    for i in range(4):
        if x & (1 << i):
            a.append(1)
        else:
            a.append(0)
    return np.array(a[::-1])


def go(x):
    a = [A[:, 0], A[:, 1], x]
    while len(a) < 16:
        pass


def run(x, y, f):
    # 在法则f下执行x和y
    x = parse(x)
    y = parse(y)
    ans = []
    for xx, yy in zip(x, y):
        ans.append(f[xx << 1 | yy])
    return np.array(ans)


def op_pattern2ops(op_group_num):
    op_group = []
    for i in range(16):
        if op_group_num & (1 << i):
            op_group.append(i)
    return op_group


def expand(op_group):
    op = [ops[ind] for ind in op_group]
    visited = {to(A[:, 0]), to(A[:, 1])}
    while 1:
        nex = copy.deepcopy(visited)
        for i in visited:
            for j in visited:
                for o in op:
                    res = run(i, j, o)
                    nex.add(to(res))
        if len(nex) == len(visited):
            # 不在变化了
            break
        visited = nex
    return visited


def can(op_group_num):
    # 从i出发，能否得到全部
    op_group = op_pattern2ops(op_group_num)
    visited = expand(op_group)
    return len(visited) == 16


def count1(x):
    s = bin(x)[2:]
    return s.count('1')


def contains(ar, x):
    for i in ar:
        if (i & x) == i:
            return True
    return False


def op2name(i):
    s = bin(i)[2:]
    s = '0' * (4 - len(s)) + s
    name = namemap[s]
    return name


def op_group2string(op_group):
    # 把操作集转成字符串
    ans = []
    for i in op_group:
        name = op2name(i)
        ans.append(name)
    return ans


ops = []
for i in range(2 ** 4):
    ops.append(parse(i))
    print(i, ops[-1], op2name(i))
candidate = []
for i in tqdm(range(2 ** len(ops))):
    # 需要排除包含关系 16个
    if contains(candidate, i):
        continue
    if can(i):
        candidate.append(i)
# 按照1的个数进行排序
candidate.sort(key=lambda x: count1(x))
final_ans = []
for i in candidate:
    if contains(final_ans, i):
        continue
    final_ans.append(i)
print('最小逻辑词组', final_ans, '个数', len(final_ans))
for i in final_ans:
    op_group = op_pattern2ops(i)
    print(i, op_group, op_group2string(op_group), len(op_group))

# 根据名称去重，非A和非B是等价的
dedup_ans = []
for i in final_ans:
    op_group = op_pattern2ops(i)
    name_list = op_group2string(op_group)
    ma = {'非A': '非', '非B': '非',
          '逆条件': '条件', '非逆条件': '非条件'}
    name_list = [ma.get(i, i) for i in name_list]
    name_list.sort()
    dedup_ans.append(','.join(name_list))
dedup_ans = np.unique(dedup_ans)
print('去重之后的结果', dedup_ans, len(dedup_ans))