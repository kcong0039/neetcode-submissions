class Solution:
    def reverseBits(self, n: int) -> int:
        tmp = bin(n)[2:]
        dummy = 31
        ret = 0
        for c in tmp[::-1]:
            ret += int(c) << dummy
            dummy -=1
        return ret



            