class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for token in tokens:
            if token not in operators:
                # If token is a number, push it onto the stack
                stack.append(int(token))
            else:
                # If token is an operator, pop the last two numbers from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()
                # Perform the operation based on the token and push the result back to the stack
                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    # In Python, division between two integers always truncates toward zero
                    stack.append(int(operand1 / operand2))

        # The final result should be the only element left in the stack
        return stack[0]
