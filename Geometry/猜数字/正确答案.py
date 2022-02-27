from scipy.special import factorial

"""
C(n,k)<=A(n,k-1)
n*(n-1)*(n-2)*...*(n-k+1)/k!<=n*(n-1)*(n-2)*...*(n-k+2)
n-k+1<=k!
n<=k!+k-1
"""
for i in range(2, 10):
    print(i, factorial(i) + i - 1)
