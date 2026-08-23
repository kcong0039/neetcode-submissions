class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(r, c):
            if ((r,c) not in seen and
                r>=0 and r<rows and
                c>=0 and c<cols and
                board[r][c] == "O"):
                seen.add((r,c))
                ds = [[0,1],[1,0],[0,-1],[-1,0]]
                for d in ds:
                    dfs(r+d[0], c+d[1])



        for row in range(rows):
            if board[row][0]=="O" and (row,0) not in seen:
                dfs(row, 0)
            if board[row][cols-1]=="O" and (row, cols-1) not in seen:
                dfs(row, cols-1)
        for col in range(cols):
            if board[0][col]=="O" and (0, col) not in seen:
                dfs(0, col)
            if board[rows-1][col] == "O" and (row-1, col) not in seen:
                dfs(rows-1, col)

        print(seen)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen:
                    board[r][c] = "X"