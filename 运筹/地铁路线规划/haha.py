from typing import List


class Solution:
    def metroRouteDesignI(self, lines: List[List[int]], start: int, end: int) -> List[int]:
        from collections import defaultdict
        g = defaultdict(lambda: [])
        for ind, line in enumerate(lines):
            for i in range(len(line) - 1):
                g[line[i]].append((line[i + 1], ind))
                g[line[i + 1]].append((line[i], ind))

        def get_graph(start, end):
            dp = defaultdict(lambda: {})
            from queue import PriorityQueue
            q = PriorityQueue()
            virtual_line = len(lines)
            dp[start][virtual_line] = (0, [])
            q.put((0, start, virtual_line))
            handled = set()
            while not q.empty():
                used, now, line_id = q.get()
                handled.add((now, line_id))
                for nex, line in g[now]:
                    if (nex, line) in handled:
                        continue
                    if line == line_id:
                        triple = (used, nex, line)
                    else:
                        triple = (used + 1, nex, line)
                    cost, nex, line = triple
                    if line not in dp[nex]:
                        dp[nex][line] = [cost, [(now, line_id)]]
                        q.put((cost, nex, line))
                    elif cost <= dp[nex][line][0]:
                        q.put((cost, nex, line))
                        dp[nex][line][1].append((now, line_id))
            # for pos, line_map in dp.items():
            #     print(pos, line_map)
            # 广度优先搜索构图，去除无效边
            gg = set()
            for pos, line_map in dp.items():
                if len(line_map) == 0:
                    continue
                cand = []
                for line, (cost, pred) in line_map.items():
                    cand.append((cost, line, pred))
                cand.sort()
                line_pred = []
                for i in cand:
                    _, line, pred = i
                    line_pred.append((line, pred))
                for line, pred in line_pred:
                    for last, last_line in pred:
                        gg.add((last, pos))
                        gg.add((pos, last))
            return gg

        g1 = get_graph(start, end)
        g2 = get_graph(end, start)
        g3 = g1.intersection(g2)
        g4 = defaultdict(lambda: set())
        for f, t in g3:
            g4[f].add(t)
            g4[t].add(f)
        print('g1', g1)
        print('g2', g2)
        print('g4', g4)
        ans = [start]
        while ans[-1] != end:
            v = g4[ans[-1]]
            print(v, ans, start, end)
            can = set(v) - set(ans)
            can = list(can)
            if not can:
                break
            nex = can[0]
            ans.append(nex)
        return ans


def main():
    lines = [[1, 2, 3, 4], [2, 6], [6, 5], [4, 5]]
    start = 1
    end = 5
    lines = [[1, 2, 3, 4, 5], [2, 10, 14, 15, 16], [10, 8, 12, 13], [7, 8, 4, 9, 11]]
    start = 1
    end = 7
    # lines=[[1,2,3],[2,4,5,6],[1,9],[9,5]]
    # start=1
    # end=6
    lines = [[1, 2, 3, 4, 5], [3, 6]]
    start = 1
    end = 6
    ans = Solution().metroRouteDesignI(lines, start, end)
    print(ans)


main()
