class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        operators = "*-+"
        isNumber = True
        for op in operators:
            if op in expression:
                isNumber = False
        if isNumber:
            return [int(expression)]
        for i,c in enumerate(expression):
            if c in operators:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i + 1:])
                for r1 in res1:
                    for r2 in res2:
                        result.append(eval(str(r1) + c + str(r2)))
        return result