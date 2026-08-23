from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        minlen = -1
        lo = 0
        hi = 0
        queue = []
        ds = defaultdict(int)
        dt = defaultdict(int)

        for c in t:
            dt[c] += 1

        def covers(ds, dt):
            for c in dt:
                if ds[c] < dt[c]:
                    return False
            return True

        while hi < len(s):
            if not queue and s[hi] not in dt:
                lo += 1
                hi += 1
                continue
            elif s[hi] in dt:
                ds[s[hi]] += 1
                queue.append(hi)
                # Shrink window if we have more than needed
                while queue and ds[s[queue[0]]] > dt[s[queue[0]]]:
                    ds[s[queue[0]]] -= 1
                    queue.pop(0)
                lo = queue[0]
                hi += 1
            elif queue and s[hi] not in dt:
                hi += 1

            if covers(ds, dt):
                currlen = hi - lo
                if minlen == -1 or currlen < minlen:
                    minlen = currlen
                    ret = s[lo:hi]

        return ret