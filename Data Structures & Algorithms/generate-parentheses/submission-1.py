from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        worklist = deque()
        countleft = deque()
        countright = deque()
        worklist.append("(")
        countleft.append(1)
        countright.append(0)
        while worklist:
            curr = worklist.popleft()
            currLeft = countleft.popleft()
            currRight = countright.popleft()
            if len(curr) == 2*n:
                ret.append(curr)
            else:
                if currLeft < n and currRight < n:
                    worklist.append(curr+"(")
                    countleft.append(currLeft+1)
                    countright.append(currRight)
                    if currLeft > currRight:
                        worklist.append(curr+")")
                        countleft.append(currLeft)
                        countright.append(currRight+1)
                elif currLeft<n:
                    worklist.append(curr+"(")
                    countleft.append(currLeft+1)
                    countright.append(currRight)
                elif currRight < currLeft:
                    worklist.append(curr+")")
                    countleft.append(currLeft)
                    countright.append(currRight+1)
            print(currLeft, currRight)
        return ret




