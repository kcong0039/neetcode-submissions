class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []
        self.helper(0, nums, target, [])
        return self.ret
    
    def helper(self, i, nums, target, curr):
        if sum(curr) == target:
            self.ret.append(curr.copy())
            return 1
        elif sum(curr) > target or i >= len(nums):
            return 0
            
        curr.append(nums[i])
        self.helper(i, nums, target, curr)
        curr.pop()
        self.helper(i+1, nums, target, curr)

        
        