class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        curr = self.times[key]
        print(curr)
        def bs(lo, hi, times):
            print(lo, hi, times)   
            if hi-lo<=1:
     
                if not times or times[lo][0] > timestamp:
                    return ""
                return times[lo][1]
            else:
                mid = (hi+lo)//2
                if times[mid][0] == timestamp:
                    return times[mid][1]
                elif times[mid][0] > timestamp:
                    return bs(lo, mid, times)
                else:
                    return bs(mid, hi, times)
        return bs(0, len(curr), curr)
                
        
