class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        # start with an empty current subset
        self.helper(nums, [])
        return self.ret

    def helper(self, nums, curr):
        if not nums:
            # append a copy to avoid later mutations
            self.ret.append(curr.copy())
            return
        # without nums[0]
        self.helper(nums[1:], curr)
        # with nums[0]
        curr.append(nums[0])
        self.helper(nums[1:], curr)
        # backtrack
        curr.pop()