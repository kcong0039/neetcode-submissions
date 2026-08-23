class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        while nums:
            ret = ret ^ nums[-1]
            nums = nums[:-1]
        return ret