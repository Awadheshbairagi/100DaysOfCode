class Solution:
    def countDigitOne(self, n: int) :
        n = str(n)       #converting it to string
        c=0   #initializing count variable
        l=len(n)

        for i in range(l-1,0,-1):
            num=int(n)
            first_dig=int(n[0])   #taking the first digit
            if first_dig==1:
                c+=(int(str(i)+'0'*(i-1))+1)
                c+=int(n[1:])
            elif first_dig==0:
                pass
            else:
                c+=(int(str(i)+'0'*(i-1))+1)
                c+=(int('9'*i))
                c+=((first_dig-1)*(int(str(i)+'0'*(i-1))))
            n=n[1::]     #removing the first digit.

        if n=='0':
            return c     #if 0 return c
        else:
            return c+1  