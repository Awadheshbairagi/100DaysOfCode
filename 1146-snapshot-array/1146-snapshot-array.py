class SnapshotArray:
    def bs(self,lt,rt,tr,lst):
        ps=0
        while lt<=rt:
            mid=(lt+rt)//2
            if lst[mid][1]<=tr:
                ps=mid
                lt=mid+1
            else:
                rt=mid-1
        return ps


    def __init__(self, length: int):
        self.lst=[0]*length
        self._id=0
        self.nums=[[(0,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.lst[index]=val
        if self.nums[index][-1][1]==self._id:
            self.nums[index][-1]=(val,self._id)
        elif self.nums[index][-1][1]<self._id:
            self.nums[index].append((val,self._id))
        

    def snap(self) -> int:
        x=self._id
        self._id+=1
        return x
        

    def get(self, index: int, snap_id: int) -> int:
        x=self.bs(0,len(self.nums[index])-1,snap_id,self.nums[index])
        return self.nums[index][x][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)