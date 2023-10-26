class Fancy:

    def __init__(self):
        self.sequence = []  # List to store the sequence
        self.operations = []  # List to store operations
        self.operations.append((0, 1))  # Initial operation: (addition, multiplication)

    def append(self, val: int) -> None:
        # Append the current value after applying inverse operations
        addition, multiplication = self.operations[-1]
        val = (val - addition) * pow(multiplication, -1, 10**9 + 7)
        val %= (10**9 + 7)
        self.sequence.append(val)

    def addAll(self, inc: int) -> None:
        # Update the last operation for addition
        addition, multiplication = self.operations[-1]
        addition += inc
        self.operations.append((addition, multiplication))

    def multAll(self, m: int) -> None:
        # Update the last operation for multiplication
        addition, multiplication = self.operations[-1]
        addition = (addition * m) % (10**9 + 7)
        multiplication = (multiplication * m) % (10**9 + 7)
        self.operations.append((addition, multiplication))

    def getIndex(self, idx: int) -> int:
        # If the index is out of range, return -1
        if idx >= len(self.sequence):
            return -1
        
        # Apply the current operations to the value at the given index
        addition, multiplication = self.operations[-1]
        val = self.sequence[idx]
        val = (val * multiplication + addition) % (10**9 + 7)
        return val

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
