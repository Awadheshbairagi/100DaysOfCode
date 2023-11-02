from typing import List

class Solution:
    def countSubsets(self, n: int, arr: List[int], l: int, r: int) -> int:
        def generate_subsets(idx, current_sum):
            nonlocal count
            if idx == n:
                if l <= current_sum <= r:
                    count += 1
                return

            # Include the current element
            generate_subsets(idx + 1, current_sum + arr[idx])

            # Exclude the current element
            generate_subsets(idx + 1, current_sum)

        count = 0
        generate_subsets(0, 0)
        return count



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        
        l,r =map(int,input().split())
        obj = Solution()
        res = obj.countSubsets(n, arr, l, r)
        
        print(res)
        

# } Driver Code Ends