class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxSize = 0

        rows, cols = len(grid), len(grid[0])

        def bfs(grid, r, c):
            q = collections.deque()
            seen.add((r,c))
            q.append((r,c))
            ret = 0

            while q:
                ret += 1
                row, col = q.popleft()
                directions = ((1,0), (0,1), (-1,0), (0,-1))
                for dr, dc in directions:
                    if ((row+dr, col+dc) not in seen and 
                        row+dr in range(rows) and
                        col+dc in range(cols) and
                        grid[row+dr][col+dc] == 1):
                        seen.add((row+dr, col+dc))
                        q.append((row+dr, col+dc))
            return ret

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in seen:
                    
                    size = bfs(grid, row, col)
                    maxSize = max(maxSize, size)
        return maxSize
    