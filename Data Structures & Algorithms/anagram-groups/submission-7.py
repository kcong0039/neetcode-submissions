class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            seen[str(sorted(s))].append(s)
        return list(seen.values())