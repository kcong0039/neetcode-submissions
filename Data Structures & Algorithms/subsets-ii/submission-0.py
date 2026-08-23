class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        def helper(nums, curr):
            if not nums:
                tmp = tuple(sorted(curr.copy()))
                if tmp not in ret:
                    ret.add(tmp)
                return
            for i in range(len(nums)):
                n = nums[i]
                nums.pop(i)
                helper(nums, curr)
                curr.append(n)
                helper(nums, curr)
                curr.pop()
                nums.insert(i, n)


        helper(nums, [])
        ret = [list(l) for l in ret]
        return ret
                
