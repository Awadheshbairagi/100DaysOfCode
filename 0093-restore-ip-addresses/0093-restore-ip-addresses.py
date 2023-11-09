class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            # If we have found a valid IP address
            if start == len(s) and len(path) == 4:
                result.append(".".join(path))
                return
            
            # Try inserting dots at different positions and validate the segment
            for i in range(start, start + 3):
                if i < len(s):
                    segment = s[start:i+1]
                    if 0 <= int(segment) <= 255 and (len(segment) == 1 or segment[0] != "0"):
                        backtrack(i + 1, path + [segment])
        
        result = []
        backtrack(0, [])
        return result
