class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            # Check if mid^2 is less than or equal to x and (mid+1)^2 is greater than x
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                ans = mid  # Update the answer with the current mid
                break
            # If mid^2 is greater than x, update the right pointer
            elif mid * mid > x:
                right = mid - 1
            # If mid^2 is less than x, update the left pointer
            else:
                left = mid + 1
        
        return ans
