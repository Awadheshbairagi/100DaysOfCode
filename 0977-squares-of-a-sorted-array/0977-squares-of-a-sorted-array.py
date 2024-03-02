class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
            x.append(nums[i])
        x.sort()
        return x