class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int) 
        for c in s: count[c] += 1
        return "".join([a[1] * a[0] for a in sorted([[count[c], c] for c in count], reverse=True)])