import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1  # minimum speed
        hi = max(piles)  # maximum speed
        return self.bananaSearch(piles, lo, hi, h)
    
    def canEat(self, piles, k, h):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
            if time > h:
                return False
        return True
        
    def bananaSearch(self, piles, lo, hi, h):
        while lo < hi:
            mid = (lo + hi) // 2
            if self.canEat(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1
        return lo