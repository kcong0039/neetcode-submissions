class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        wl = deque()
        ret = 0
        def expand():
            deltas = [(1,0), (-1,0), (0, 1), (0, -1)]
            while wl:
                tmp = wl.popleft()
                for d in deltas:
                    if (d[0] + tmp[0] < len(grid) and
                        d[0] + tmp[0] >= 0 and
                        d[1] + tmp[1] < len(grid[0]) and
                        d[1] + tmp[1] >=0 and 
                        grid[d[0]+tmp[0]][d[1]+tmp[1]] == "1" and
                        (d[0]+tmp[0], d[1]+tmp[1]) not in seen):
                        seen.add((d[0]+tmp[0], d[1]+tmp[1]))
                        wl.append((d[0]+tmp[0], d[1]+tmp[1]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = (i,j)
                currval = grid[i][j]
                if curr not in seen and currval == "1":
                    print(curr)
                    seen.add(curr)
                    wl.append(curr)
                    ret += 1
                    expand()
        return ret
