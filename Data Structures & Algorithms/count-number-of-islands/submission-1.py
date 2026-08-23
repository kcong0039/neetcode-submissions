class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        ret = 0

        def bfs(i,j):
            deltas = [(1,0), (0, 1), (-1, 0), (0, -1)]
            wl = deque()
            wl.append((i,j))
            seen.add((i,j))
            while wl:
                tmp = wl.popleft()
                for d in deltas:
                    exploreRow = tmp[0]+d[0]
                    exploreCol = tmp[1]+d[1]
                    if (exploreCol >=0 and 
                       exploreCol < len(grid[0]) and 
                       exploreRow >= 0 and 
                       exploreRow < len(grid) and
                       grid[exploreRow][exploreCol] == "1"):
                        
                        if (exploreRow, exploreCol) not in seen:
                            seen.add((exploreRow, exploreCol))
                            wl.append((exploreRow, exploreCol))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = (i,j)
                if grid[i][j] == "1" and curr not in seen:
                    ret += 1
                    bfs(i,j)
        return ret