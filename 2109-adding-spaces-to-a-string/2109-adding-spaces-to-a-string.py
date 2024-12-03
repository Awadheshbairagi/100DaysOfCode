class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result=[]
        space=0
        for i in range(len(s)):
            if(space<len(spaces) and i==spaces[space]):
                result.append(" ")
                space+=1
            result.append(s[i])
        return "".join(result)