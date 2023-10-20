class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        # Push the elements of nestedList in reverse order onto the stack
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        # As the stack contains integers at the top, simply pop and return the top element
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # Continue the loop until the stack is empty
        while self.stack:
            # Get the top element from the stack
            top = self.stack[-1]
            if top.isInteger():
                return True  # If it's an integer, hasNext is True
            # If it's a list, pop it from the stack and push its elements onto the stack in reverse order
            self.stack.pop()
            for i in range(len(top.getList()) - 1, -1, -1):
                self.stack.append(top.getList()[i])
        return False  # If the stack is empty, there are no more elements

# Example usage:
# nestedList = [[1, 1], 2, [1, 1]]
# i = NestedIterator(nestedList)
# while i.hasNext():
#     print(i.next())  # Output: [1, 1, 2, 1, 1]
