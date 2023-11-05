class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        total, ret, digits = 1, "", [i for i in range(1, n+1)]
        for i in range(2, n):
            total*= i
        k-=1

        for i in range(n-1, -1, -1):
            #choose digit and remove it from digits
            val = k // total
            ret+= str(digits[val])
            del digits[val]
            k-= val*total

            total = total//i if i>0 else total
        return ret