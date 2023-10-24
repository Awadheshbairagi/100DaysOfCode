class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.hashset = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        if not self.hashset[index]:
            self.hashset[index] = [key]
        else:
            if key not in self.hashset[index]:
                self.hashset[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.hashset[index]:
            if key in self.hashset[index]:
                self.hashset[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return self.hashset[index] and key in self.hashset[index]
