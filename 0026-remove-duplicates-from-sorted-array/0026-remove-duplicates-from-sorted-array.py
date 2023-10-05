class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        curr_val,next_val=0,1
        while(next_val<len(nums)):
            while(next_val<len(nums) and nums[curr_val]==nums[next_val]):
                next_val+=1
            if(next_val==len(nums)):
                break
            curr_val+=1
            nums[curr_val]=nums[next_val]
            next_val+=1
        return curr_val+1