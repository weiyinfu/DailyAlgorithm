n = int(input())
for i in range(n):
    input()
if n == 1:
    print(2)
elif n == 2:
    print(1 + 2 + 1)
else:
    print(n + (n * (n - 1) // 2) + 1 + (n * (n - 1) * (n - 2) // 6))
