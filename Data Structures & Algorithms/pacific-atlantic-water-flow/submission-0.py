class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        ret = []

        def dfs(r, c, ocean, last):
            if ((r,c) not in ocean and
                r>=0 and r < rows and
                c>=0 and c < cols and
                heights[r][c] >= last):
                ocean.add((r,c))
                dfs(r+1, c, ocean, heights[r][c])
                dfs(r-1, c, ocean, heights[r][c])
                dfs(r, c+1, ocean, heights[r][c])
                dfs(r, c-1, ocean, heights[r][c])
        
        for row in range(rows):
            dfs(row, 0, pac, 0)
            dfs(row, cols-1, atl, 0)
        
        for col in range(cols):
            dfs(0, col, pac, 0)
            dfs(rows-1, col, atl, 0)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    ret.append([r,c])
        return ret