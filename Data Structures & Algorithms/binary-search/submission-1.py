class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums, 0, len(nums), target)
    
    def bs(self, nums, lo, hi, target):
        if hi - lo==1:
            if nums[lo]==target:
                return lo
            return -1
        mid = (hi+lo)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            return self.bs(nums, mid, hi, target)
        elif nums[mid] > target:
            return self.bs(nums, lo, mid, target)
