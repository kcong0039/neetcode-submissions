class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max = 0
        for n in nums:
            curr = 0
            if n-1 in numset:
                continue
            else:
                tmp = n
                while tmp in numset:
                    curr += 1
                    tmp += 1
                if curr > max:
                    max = curr
        return max

                
