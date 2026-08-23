class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        lo = 0
        hi = 1
        while hi < len(prices):
            if prices[hi] < prices[lo]:
                lo = hi
                hi += 1
            else:
                profit = prices[hi]-prices[lo]
                if profit > max:
                    max = profit
                hi +=1
        return max

