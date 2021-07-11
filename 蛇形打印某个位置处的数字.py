class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        n = num
        x, y = xPos, yPos
        turn = min(x, n - x - 1, y, n - y - 1)
        edge = n - turn * 2
        if x == turn:
            dis = y - turn
        elif y == turn:
            # left
            dis = edge + edge - 1 + edge - 1 - 1 + n - 1 - x - turn
        elif x == n - 1 - turn:
            # down
            dis = edge - 1 + edge - 1 + n - 1 - turn - y
        else:
            # right
            dis = x - turn + edge - 1
        if turn > 0:
            su = (turn - 1) * turn // 2
            s = (4 * n - 4) * turn - 8 * su
        else:
            s = 0
        s += dis
        # print(turn, dis, s, 'edge=', edge)
        return s % 9 + 1


x = Solution()
n = 4
for i in range(n):
    for j in range(n):
        print(x.orchestraLayout(n, i, j), end=' ')
    print()
# print(x.orchestraLayout(n, 2, 2))
