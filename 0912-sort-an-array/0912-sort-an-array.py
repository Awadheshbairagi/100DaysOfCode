class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        arr=[0]*(10**5+1)
        for i in nums:
            arr[i+(50000)]+=1
        new=[]
        for i in range(len(arr)):
            if arr[i]:
                for j in range(arr[i]):
                    new.append(i-50000)
        return new