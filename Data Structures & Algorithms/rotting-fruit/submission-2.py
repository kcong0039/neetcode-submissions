class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if sum(sum(row) for row in grid)==0:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i, j, 0))
                    seen.add((i, j))       
        while q:
            
            ds = [(0,1), (1, 0), (0, -1), (-1,0)]
            curr = q.popleft()
            i, j = curr[0], curr[1]
            print(curr, q, seen)
            for d in ds:    
                if i+d[0] >=0 and i +d[0] < rows and j+d[1] >= 0 and j+d[1]< cols:
                    if (i+d[0], j+d[1]) not in seen and grid[i+d[0]][j+d[1]] == 1:
                        grid[i+d[0]][j+d[1]] = 2
                        seen.add((i+d[0], j+d[1]))
                        q.append((i+d[0], j+d[1], curr[2]+1))
        for row in grid:
            if 1 in row:
                return -1             
        return curr[2]



