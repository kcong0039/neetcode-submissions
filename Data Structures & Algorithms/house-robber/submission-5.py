class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        cache = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                cache[i] = nums[0]
            elif i == 1:
                cache[i] = nums[1]
            else:
                cache[i] = max(cache[i-1], cache[i-2]+nums[i], cache[i-3]+nums[i])
        print(cache)
        return max(cache)
