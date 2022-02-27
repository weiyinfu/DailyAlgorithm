n = 101
big = 0xffffff
f = [[big] * n for _ in range(n)]
f[0][0] = 0
"""
可以执行的操作
* 写一个字符
* ctrl+c复制
* ctrl+a全选
* ctrl+v

如果可以删除，则需要使用优先队列存储操作次数最少的。
"""
for i in range(n):
    for hold in range(n):
        if f[i][hold] == big:
            continue
        # write char
        if i + 1 < n:
            f[i + 1][hold] = min(f[i + 1][hold], f[i][hold] + 1)
        # copy all
        if i * 2 < n:
            f[i * 2][i] = min(f[i * 2][i], f[i][hold] + 7)
        # ctrl v
        if i + hold < n:
            f[i + hold][hold] = min(f[i + hold][hold], f[i][hold] + 2)
print(min(f[100]))
