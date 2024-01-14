class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n)==1:
            return str(int(n)-1)
        tests=[]
        tests.append(10**(len(n)-1)+1)
        tests.append(10**(len(n))+1)
        tests.append(10**(len(n)-1)-1)
        tests.append(10**(len(n))-1)
        if len(n)%2==0:
            tests.append(int(n[:len(n)//2]+n[:len(n)//2][::-1]))
            x=str(int(n[:len(n)//2])-1)
            tests.append(int(x+x[::-1]))
            y=str(int(n[:len(n)//2])+1)
            tests.append(int(y+y[::-1]))
        else:
            tests.append(int(n[:len(n)//2]+n[:len(n)//2+1][::-1]))
            x=str(int(n[:1+len(n)//2])-1)
            tests.append(int(x+x[::-1][1:]))
            y=str(int(n[:1+len(n)//2])+1)
            tests.append(int(y+y[::-1][1:]))
        n=int(n)
        ans=0
        mini=float("inf")
        for i in tests:
            if abs(i-n)<mini and i!=n:
                mini=abs(i-n)
                ans=i
            elif abs(i-n)==mini and ans>i:
                ans=i
        return str(ans)