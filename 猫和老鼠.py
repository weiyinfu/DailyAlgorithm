from typing import List

"""
https://leetcode-cn.com/contest/weekly-contest-224/problems/cat-and-mouse-ii/
"""
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        xsize = len(grid)
        ysize = len(grid[0])
        grid = [list(i) for i in grid]
        mouse = (0, 0)
        cat = (0, 0)
        food = (0, 0)
        for i in range(xsize):
            for j in range(ysize):
                if grid[i][j] == 'C':
                    cat = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == 'F':
                    food = (i, j)
                    grid[i][j] = '.'

        def legal(x, y):
            return 0 <= x < xsize and 0 <= y < ysize

        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        from collections import defaultdict

        graph = defaultdict(lambda: [])
        vis = set()

        def build(mx, my, cx, cy, op):
            # op means who move
            k = (mx, my, cx, cy, op)
            if k in vis:
                return
            vis.add(k)
            if op == 0:
                for dx, dy in directions:
                    for i in range(1, mouseJump + 1):
                        x, y = mx + dx * i, my + dy * i
                        if not legal(x, y):
                            break
                        if grid[x][y] == '#':
                            break
                        nex = (x, y, cx, cy, 1)
                        graph[nex].append(k)
                        if (x, y) == food:
                            continue
                        build(*nex)
            else:
                for dx, dy in directions:
                    for i in range(1, catJump + 1):
                        x, y = cx + dx * i, cy + dy * i
                        if not legal(x, y):
                            break
                        if grid[x][y] == '#':
                            break
                        nex = (mx, my, x, y, 0)
                        graph[nex].append(k)
                        if (x, y) == food:
                            continue
                        if (x, y) == (mx, my):
                            # 如果抓住了，直接继续
                            continue
                        build(*nex)

        build(mouse[0], mouse[1], cat[0], cat[1], 0)

        # 找到所有的老鼠必胜状态，然后执行广度优先搜索
        def solve():
            nex_count=defaultdict(lambda :0)
            for f,tos in graph.items():
                for t in tos:
                    nex_count[t]+=1
            q = []
            f=dict()
            for it in graph:
                mx, my, cx, cy, op = it
                if op == 1 and (mx, my) == food:
                    q.append(it)
                    f[it]=1
                elif op == 0 and (cx, cy) == food or (cx,cy)==(mx,my):
                    q.append(it)
            vis = set()
            for i in q:
                vis.add(i)
            while q:
                now = q.pop()
                for pre in graph[now]:
                    if pre not in vis:
                        vis.add(pre)
                        q.append(pre)
            return (mouse[0], mouse[1], cat[0], cat[1], 0) in vis

        return solve()


grid = ["M.C...F"]
catJump = 1
mouseJump = 3
res = Solution().canMouseWin(grid, catJump, mouseJump)
print(res)
