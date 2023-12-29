class Solution:
    def dp(self,i,jobDifficulty,d,n,mx,dct):
        if i>=n:
            if  d>0:
                return float("infinity")
            return mx
        if (i,d,mx) in dct:
            return dct[(i,d,mx)]
        x=self.dp(i+1,jobDifficulty,d-1,n,0,dct)+max(mx,jobDifficulty[i])
        y=self.dp(i+1,jobDifficulty,d,n,max(mx,jobDifficulty[i]),dct)
        dct[(i,d,mx)]=min(x,y)
        return min(x,y)
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)
        if n<d:
            return -1
        return self.dp(0,jobDifficulty,d,n,0,{})
