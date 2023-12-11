class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        path_1_pre_2 = max(nums[0],nums[1])
        path_1_pre_1 = max(nums[0]+nums[2], nums[1])
        path_2_pre_2 = nums[1]
        path_2_pre_1 = max(nums[1], nums[2])
        for i in range(3,len(nums)-1):
            temp_1 = path_1_pre_1
            temp_2 = path_2_pre_1
            path_1_pre_1 = max(path_1_pre_2 + nums[i], path_1_pre_1)
            path_2_pre_1 = max(path_2_pre_2 + nums[i], path_2_pre_1)
            path_1_pre_2 = temp_1
            path_2_pre_2 = temp_2
        return max(path_1_pre_1, max(path_2_pre_1,path_2_pre_2+nums[-1]))