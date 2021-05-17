def get_primes():
    primes = []
    N = 40000
    is_prime = [True] * N
    for i in range(2, N):
        if is_prime[i]:
            primes.append(i)
        for j in primes:
            if j * i >= len(is_prime):
                break
            is_prime[j * i] = False
            if i % j == 0:
                break
    return primes


def main():
    n, m, g = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    primes = get_primes()
    phi = get_phi(m, primes)  # 求m的phi
    prod = [0] * (1 + len(a))
    prod[-1] = 1
    for i in range(len(a) - 1, -1, -1):
        now = a[i] * prod[i + 1]
        if now != 0 and now % phi == 0:
            prod[i] = phi
        else:
            prod[i] = now % phi
    s = g
    ans = [0] * len(a)
    for ind, i in enumerate(a):
        # print(s, prod[ind + 1], m)
        ans[ind] = pow(s, prod[ind + 1], m)
        s = pow(s, i, m)
    print(' '.join(str(i) for i in ans))


"""
3 8 2
2 2 2
"""


def get_phi(x, primes):
    s = x
    p = []
    for i in primes:
        if x % i == 0:
            p.append(i)
            while s % i == 0:
                s //= i
    if s != 1:
        p.append(s)
    s = x
    for i in p:
        s -= s // i
    return s


main()
# print(get_phi(10, get_primes()))
