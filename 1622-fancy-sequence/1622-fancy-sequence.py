class Fancy:

    def __init__(self):
        self.sequence = []  
        self.operations = []  
        self.operations.append((0, 1))
    def append(self, val: int) -> None:
        addition, multiplication = self.operations[-1]
        val = (val - addition) * pow(multiplication, -1, 10**9 + 7)
        val %= (10**9 + 7)
        self.sequence.append(val)

    def addAll(self, inc: int) -> None:
        addition, multiplication = self.operations[-1]
        addition += inc
        self.operations.append((addition, multiplication))

    def multAll(self, m: int) -> None:
        addition, multiplication = self.operations[-1]
        addition = (addition * m) % (10**9 + 7)
        multiplication = (multiplication * m) % (10**9 + 7)
        self.operations.append((addition, multiplication))

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        addition, multiplication = self.operations[-1]
        val = self.sequence[idx]
        val = (val * multiplication + addition) % (10**9 + 7)
        return val