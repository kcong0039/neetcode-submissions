class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        numIslands = 0

        rows, cols = len(grid), len(grid[0])

        def bfs(grid, r, c):
            q = collections.deque()
            seen.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = ((1,0), (0,1), (-1,0), (0,-1))
                for dr, dc in directions:
                    if ((row+dr, col+dc) not in seen and 
                        row+dr in range(rows) and
                        col+dc in range(cols) and
                        grid[row+dr][col+dc] == "1"):
                        seen.add((row+dr, col+dc))
                        q.append((row+dr, col+dc))

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == "1" and (row, col) not in seen:
                    print(seen)
                    numIslands += 1
                    bfs(grid, row, col)
                    
        return numIslands
    