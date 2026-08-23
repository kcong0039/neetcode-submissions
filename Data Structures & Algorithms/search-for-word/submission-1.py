class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        
        def helper(board, word, letterI, coords, lastRow, lastCol):
            print(letterI, coords)
            if letterI==len(word):
                return 1
            for i,j in ((lastRow-1, lastCol), (lastRow, lastCol-1), (lastRow+1, lastCol), (lastRow, lastCol+1)):
                if i >=0 and i<rows and (i,j) != (lastRow,lastCol) and j >=0 and j<cols:
                    print(board[i][j])
                    if (i,j) not in coords and board[i][j] == word[letterI]:
                        coords.add((i,j))
                        if helper(board, word, letterI +1, coords, i, j):
                            return 1
                        coords.remove((i,j))
            return 0
        for row in range(rows):
                for col in range(cols):
                    if board[row][col] == word[0]:
                        ans = helper(board, word, 1, set([(row,col)]), row, col)
                        if ans != 0:
                            return True
        return False


