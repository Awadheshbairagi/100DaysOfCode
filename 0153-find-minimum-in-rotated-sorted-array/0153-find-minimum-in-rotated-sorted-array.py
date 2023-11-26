class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        mi=-1
        while(l<=h):
            mid=(l+h)//2
            prev=(mid+len(nums)-1)%len(nums)
            if nums[mid]<=nums[prev]:
                mi=mid
                break
            if nums[l]<=nums[h]:
                mi=l
                break
            elif nums[l]<=nums[mid]:
                l=mid+1
            elif nums[mid]<=nums[h]:
                h=mid-1
        return nums[mi]