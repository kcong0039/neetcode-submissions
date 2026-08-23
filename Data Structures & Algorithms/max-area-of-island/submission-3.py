class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        wl = deque()
        maxSize = 0

        def bfs(i, j):
            deltas = [(0,1),(1,0),(0,-1),(-1,0)]
            currSize = 1
            while wl:
                tmp = wl.popleft()
                for dr, dc in deltas:
                    nr = tmp[0]+dr
                    nc = tmp[1]+dc
                    if (nr >= 0 and 
                        nc >= 0 and
                        nr < len(grid) and
                        nc < len(grid[0]) and
                        (nr, nc) not in seen and
                        grid[nr][nc] == 1):
                        currSize += 1
                        seen.add((nr,nc))
                        wl.append((nr,nc))

            return currSize

                        


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = (i,j)
                currval = grid[i][j]
                if curr not in seen and currval == 1:
                    size = bfs(i,j)
                    wl.append(curr)
                    seen.add(curr)
                    maxSize = max(maxSize, size)

        return maxSize
