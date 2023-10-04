class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.split()
        x=arr[len(arr)-1]
        
        return len(x)