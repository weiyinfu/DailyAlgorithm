import time

import numpy as np

"""
密码比较的时候是一个for循环，通常写成下面这样。一旦遇到不相等，立即返回。  
如果相等，则for循环的耗时会更长一点。  

def guess(g):
    for i in range(len(g)):
        if g[i] != ans[i]:
            return False
    return True
    
    
计时攻击是一种猜测密码的手段，它得以实施的前提是暴力猜测很多次。  
如果每次只猜测一个字母，那么很大概率会出错，所以需要使用迭代加深搜索。  

即便采用迭代加深搜索，最后几个字母出错的概率依旧挺大，但是最后几个字母也是可以给出概率来的。  
"""
passwd_length = 10


def generate():
    a = []
    for i in range(passwd_length):
        a.append(chr(np.random.randint(0, 26) + ord('a')))
    return ''.join(a)


ans = generate()


def guess(g):
    for i in range(len(g)):
        if g[i] != ans[i]:
            return False
    return True


def timing(g, times=100000):
    beg = time.time()
    for i in range(times):
        guess(g)
    end = time.time()
    return end - beg


def find(had):
    candidates = [had]
    for loop in range(min(3, passwd_length - len(had))):
        nex = []
        for cand in candidates:
            for i in range(26):
                ch = chr(ord('a') + i)
                g = ''.join(cand + [ch] + ['a'] * (passwd_length - len(cand) - 1))
                t = timing(g)
                nex.append((cand + [ch], t))
        nex.sort(key=lambda x: x[1])
        candidates = [x[0] for x in nex[-3:]]
        # chs = [x[len(had)] for x in candidates]
        # if len(set(chs)) == 1:
        #     break
    return candidates[-1][len(had)]


def find2(had):
    candidates = []
    for i in range(26):
        ch = chr(ord('a') + i)
        g = ''.join(had + [ch] + ['a'] * (passwd_length - len(had) - 1))
        t = timing(g)
        candidates.append((ch, t))
    candidates.sort(key=lambda x: x[1])
    return candidates[-1][0]


def attack(find):
    cur = []
    for i in range(passwd_length):
        ch = find(cur)
        cur.append(ch)
        print(f"attack {cur} {ch}")
    return ''.join(cur)


def main():
    print(ans)
    mine = attack(find)
    print(f"mine={mine} ans={ans}")


main()
