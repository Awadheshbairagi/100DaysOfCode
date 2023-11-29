class Solution:
    def removeStars(self, s: str) -> str:
        return reduce(lambda r,c:(r+c,r[:-1])[c=='*'],s,'')