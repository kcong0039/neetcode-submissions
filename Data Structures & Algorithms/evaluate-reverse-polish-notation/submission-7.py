import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        ret = 0
        for i in tokens:
            if len(i)>1 or i.isnumeric():
                operands.append(int(i))
            else:
                v2 = operands.pop()
                v1 = operands.pop()
                if i == "+":
                    operands.append(v1+v2)
                if i == "-":
                    operands.append(v1-v2)
                if i == "*":
                    operands.append(v1*v2)
                if i == "/":
                    operands.append(int(v1 / v2))
            print (operands)
        return operands[0]