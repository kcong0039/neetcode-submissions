class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        if len(s1)>len(s2): 
            return False
        for j in range(len(s1)):
            d1[s1[j]]+=1
            d2[s2[j]]+=1
        
        i = 0
        if d1==d2:
            return True

        while i+len(s1)<len(s2):
            d2[s2[i]]-=1
            if d2[s2[i]] == 0:
                d2.pop(s2[i])
            d2[s2[i+len(s1)]]+=1
            print (i, d2)
            if d1==d2:
                return True
            else:
                i+=1
        return d1==d2

        