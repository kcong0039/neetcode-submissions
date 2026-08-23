class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        lmax, li = heights[l], l
        rmax, ri = heights[r], r
        curr = 0
        while r>l:
            if heights[r] > heights[l]:
                l += 1
                if heights[l] > lmax:
                    for i in range(li+1, l):
                        curr += lmax-heights[i]
                    lmax, li = heights[l], l
            else:
                r -= 1
                if heights[r] > rmax:
                    for i in range(r+1, ri):
                        curr += rmax-heights[i]
                    rmax, ri = heights[r], r
        
        for i in range(li+1, ri):

            curr += min(lmax, rmax) - heights[i]

        return curr


                
