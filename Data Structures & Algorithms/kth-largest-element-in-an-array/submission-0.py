class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ret = []
        heapq.heapify(ret)
        while nums:
            heapq.heappush(ret, nums.pop())
            if len(ret) > k:
                heapq.heappop(ret)
        return ret[0]