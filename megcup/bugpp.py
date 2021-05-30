from  PIL import Image

img = Image.open("bugpp_logo_2000.png")
sz = 2000
a = [[0] * sz for i in range(sz)]
for i in range(sz):
    for j in range(sz):
        c = img.getpixel((i, j))
        a[i][j] = 1 if c[0] == 255 else 0
b = [[1] * sz for i in range(sz)]
cnt = 0

#以十字架最上方定点为（0,0）
pos = [(0, 0), (1, 0), (2, 0), (3, 0),
       (4, 0), (5, 0), (6, 0),
       (3, -1), (3, -2), (3, -3), (3, 1), (3, 2), (3, 3)]


def go(x, y):
    for i, j in pos:
        xx, yy = x + i, y + j
        if 2000 > xx >= 0 and 2000 > yy >= 0:
            a[xx][yy] ^= 1
            b[xx][yy] ^= 1


print("begin")
for i in range(sz):
    for j in range(sz):
        if a[i][j] == b[i][j]: continue
        cnt += 1
        go(i, j)
print(a==b)
print(cnt)
