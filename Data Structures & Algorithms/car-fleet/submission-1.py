import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times  = [0 for _ in position]
        for i in range(len(position)):
            times[i] = (target-position[i])/speed[i]
        pst = [(position[i], speed[i], times[i]) for i in range(len(position))]
        pst.sort(reverse = True)

        fleets = 0
        stack = []
        print(pst)
        for car in pst:
            if not stack:
                stack.append(car)
            else:
                if car[2] <= stack[0][2]:
                    stack.append(car)
                else:
                    stack = [car]
                    fleets += 1
        return fleets+1
