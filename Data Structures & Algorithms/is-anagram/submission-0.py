class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterss = {}
        letterst = {}
        for c in s:
            if c in letterss:
                letterss[c] += 1
            else:
                letterss[c] = 1
        for c in t:
            if c in letterst:
                letterst[c] += 1
            else:
                letterst[c] = 1
        return letterss == letterst
        