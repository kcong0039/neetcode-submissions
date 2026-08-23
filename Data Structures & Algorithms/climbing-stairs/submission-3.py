class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for _ in range(n+1)]
        for i in range(n, 0, -1):
            if i == n:
                cache[i] = 1
            elif i == n-1:
                cache[i] = 2
            else:
                cache[i] = cache[i+1]+cache[i+2]
        return cache[1]
