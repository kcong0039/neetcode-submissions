class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        ret = []
        heapq.heapify(minheap)
        for p in points:
            heapq.heappush(minheap, [-(math.sqrt(p[0]**2 + p[1]**2)), p[0], p[1]])
            if len(minheap) > k:
                curr = heapq.heappop(minheap)
        for entry in minheap:
            ret.append(entry[1:])
        return ret
                
