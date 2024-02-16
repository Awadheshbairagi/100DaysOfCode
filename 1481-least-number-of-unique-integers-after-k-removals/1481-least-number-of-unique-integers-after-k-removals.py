class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        frequencies = list(freq_map.values())
        frequencies.sort()
        elements_removed = 0
        for i in range(len(frequencies)):
            elements_removed += frequencies[i]
            if elements_removed > k:
                return len(frequencies) - i
        return 0