class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        counts = [[] for i in range(len(nums)+1)]
        for i in nums:
            seen[i] += 1
        for i, cnt in seen.items():
            counts[cnt].append(i)
        ret = []
        for i in range(len(counts)-1, 0, -1):
            for num in counts[i]:
                ret.append(num)
                if len(ret) == k:
                    return ret
            

