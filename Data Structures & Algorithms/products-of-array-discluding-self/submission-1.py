class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        z = 0
        ret = []
        for i in nums:
            if i == 0: 
                z += 1
            else:
                product *= i
        if z >1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if z:
                if nums[i] == 0:
                    ret.append(product)
                else:
                    ret.append(0)
            else:
                ret.append(int(product/nums[i]))
        return ret