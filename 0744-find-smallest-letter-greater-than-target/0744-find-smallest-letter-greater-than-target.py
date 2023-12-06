class Solution:
    def nextGreatestLetter(self, L: List[str], T: str) -> str:
        return L[bisect_right(L, T)] if bisect_right(L, T) < len(L) else L[0]