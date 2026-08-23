class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            curr = [0 for _ in range(26)]
            for c in w:
                curr[ord(c)-ord("a")] += 1
            if tuple(curr) in seen:
                seen[tuple(curr)].append(w)
            else:
                seen[tuple(curr)] = [w]
        
        return list(seen.values())



        