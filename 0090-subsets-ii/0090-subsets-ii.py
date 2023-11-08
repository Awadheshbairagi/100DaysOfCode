class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path, res):
            res.append(path[:])
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path, res)
                path.pop()
        
        nums.sort()  # Sort the input array to handle duplicates
        result = []
        backtrack(0, [], result)
        return result
