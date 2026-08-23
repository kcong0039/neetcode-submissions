class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(grid, i, j, curr):
            rows, cols = len(grid), len(grid[0])
            ds = [(0,1), (1, 0), (0, -1), (-1, 0)]
            for d in ds:
                if i+d[0] >=0 and i +d[0] < rows and j+d[1] >= 0 and j+d[1]< cols:
                    if grid[i+d[0]][j+d[1]] > curr:
                        grid[i+d[0]][j+d[1]] = curr
                        bfs(grid, i+d[0], j+d[1], curr+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = grid[i][j]
                if curr == 0:
                    bfs(grid, i, j, 1)
        