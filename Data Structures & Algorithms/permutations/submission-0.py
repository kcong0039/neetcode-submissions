class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def helper(nums, curr):
            print(nums, curr)
            if not nums:
                ret.append(curr.copy())
            for i in range(len(nums)):
                val = nums[i]
                curr.append(val)
                nums.pop(i)
                helper(nums, curr)
                nums.insert(i, val)
                curr.pop()
        helper(nums, [])
        return ret

