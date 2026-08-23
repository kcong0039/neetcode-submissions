class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while hi>lo:
            mid = (lo+hi)//2
            if nums[mid]==target:
                return mid
            if hi-lo==1:
                if nums[lo]==target:
                    return lo
                if nums[hi]==target:
                    return hi
                return -1
            else:
                if nums[mid]-nums[lo]>0:
                    if target <= nums[mid] and target >= nums[lo]:
                        hi = mid-1
                    else:
                        lo = mid+1
                else:
                    if target >= nums[mid] and target <= nums[hi]:
                        lo = mid+1
                    else:
                        hi = mid-1
        return lo if nums[lo]==target else -1