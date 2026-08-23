class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        res = nums[0]
        while lo < hi:

            if nums[lo]<nums[hi]:
                return min(nums[lo], res)

            mid = (lo+hi)//2
            if nums[mid]-nums[lo] < 0:
                hi = mid
            else:
                lo = mid+1
        return nums[hi]
            
