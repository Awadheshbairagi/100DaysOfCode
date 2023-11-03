class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        jumps = 1
        current_max = nums[0]
        next_max = nums[0]
        
        for i in range(1, len(nums)):
            if i > current_max:
                jumps += 1
                current_max = next_max
            next_max = max(next_max, i + nums[i])
        
        return jumps
