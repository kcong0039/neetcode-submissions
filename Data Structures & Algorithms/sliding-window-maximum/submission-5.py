class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()          # stores indices, nums[dq] is decreasing
        out = []
        for i, x in enumerate(nums):
            # 1) drop indices that left the window
            while dq and dq[0] <= i - k:
                dq.popleft()
            # 2) maintain decreasing order (drop smaller/equal tails)
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            # 3) record max once first window is formed
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out


        

