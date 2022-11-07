class MinStack:

    def __init__(self):
        self.data = []
   
    def _copyAndSort(self):
        self.sorted = []
        for i in self.data:
            self.sorted.append(i)
        self.sorted.sort()

    def push(self, val: int) -> None:
        self.data.append(val)    

    def pop(self) -> None:
        del self.data[-1]

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        self._copyAndSort()
        return self.sorted[0]
