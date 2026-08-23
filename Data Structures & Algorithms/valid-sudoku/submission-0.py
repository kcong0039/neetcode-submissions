class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                print((row / 3) * 3 + (col / 3))
                curr = board[row][col]
                if curr != ".":
                    if curr in rows[row]:
                        return False
                    else:
                        rows[row].add(curr)
                    if curr in cols[col]:
                        return False
                    else:
                        cols[col].add(curr)
                    if curr in squares[int((row // 3) * 3 + (col // 3))]:
                        return False
                    else:
                        squares[int((row // 3) * 3 + (col // 3))].add(curr)
        return True

