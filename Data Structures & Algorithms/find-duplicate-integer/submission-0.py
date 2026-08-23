class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr = nums[i]
            swap = nums[curr-1]
            if curr-1 != i and curr == swap:
                return curr
            nums[curr-1] = curr
            nums[i] = swap
            print(nums)