class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0 for i in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                print(stack, stack[-1])
                while stack and t> temperatures[stack[-1]]:
                    tmp = stack.pop()
                    ret[tmp] = i-tmp
                stack.append(i)
        return ret
            
            
            
                    
            

            