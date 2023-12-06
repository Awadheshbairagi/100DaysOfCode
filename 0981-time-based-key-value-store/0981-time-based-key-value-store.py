from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.dt = {}
        self.keys_ts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[(key,timestamp)] = value
        self.keys_ts[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        ats = None
        s_l = self.keys_ts[key]
        if not s_l or timestamp < s_l[0]:
            return ''
        l,r = 0,len(s_l)-1
        while r>=l:
            m = (l+r)//2
            if s_l[m]>timestamp:
                r = m-1
            elif s_l[m]<timestamp:
                l = m+1
            else:
                ats = s_l[m]
                break       
        if not ats:
            ats = s_l[l-1]
        return self.dt[(key,ats)]  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)