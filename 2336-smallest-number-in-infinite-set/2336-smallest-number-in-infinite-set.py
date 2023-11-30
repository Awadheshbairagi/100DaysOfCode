class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(range(1,1001))
        

    def popSmallest(self) -> int:
        self.nums.sort()
        n = self.nums[0]
        self.nums[:] = self.nums[1:]
        return n

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.append(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)