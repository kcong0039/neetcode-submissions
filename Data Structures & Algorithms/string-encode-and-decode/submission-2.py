class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s))
            ret += "#"
            ret += s
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        last = 0
        i = 0
        while i < len(s):
            if s[i] != "#":
                i+=1
            else:
                length = int(s[last:i])
                ret.append(s[i+1:i+1+length])
                i += 1+length
                last = i
        return ret



