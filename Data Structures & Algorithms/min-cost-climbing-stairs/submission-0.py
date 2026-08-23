class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two = len(cost)-1
        one = two-1
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min(cost[i]+cost[one], cost[i]+cost[two])
            one -=1
            two -=1

        return min(cost[one], cost[two])
