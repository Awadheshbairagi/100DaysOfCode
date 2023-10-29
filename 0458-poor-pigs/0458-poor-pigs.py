class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests_per_pig = minutesToTest // minutesToDie + 1
        pigs = 0        
        while tests_per_pig ** pigs < buckets:
            pigs += 1 
        return pigs
