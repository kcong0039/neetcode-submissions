class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        print (stones)
        while len(stones) > 1:
            b = heapq.heappop(stones)
            s = heapq.heappop(stones)
            print(b-s)
            if s-b != 0:
                heapq.heappush(stones, b-s)
        stones.append(0)
        return -stones[0]