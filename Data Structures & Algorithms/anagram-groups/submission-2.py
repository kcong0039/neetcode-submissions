class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        ret = defaultdict(list)
        for word in strs:
            id = [0]*26
            for c in word:
                id[ord(c)-ord("a")]+=1
            ret[tuple(id)].append(word)

        return list(ret.values())


        