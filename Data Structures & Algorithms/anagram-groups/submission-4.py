class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for w in strs:
            curr = set()
            for c in w:
                curr.add((c, self.count(w, c)))
            if frozenset(curr) in seen:
                seen[frozenset(curr)].append(w)
            else:
                seen[frozenset(curr)] = [w]
        print(seen)
        return list(seen.values())
    def count(self, word, letter):
        ret = 0
        for c in word:
            if c == letter:
                ret += 1
        return ret


        