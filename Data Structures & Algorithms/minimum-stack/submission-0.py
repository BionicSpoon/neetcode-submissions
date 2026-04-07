class MinStack:

    def __init__(self):
        self.items = []
        self.min_before = [] 

    def push(self, val: int) -> None:
        self.items.append(val)
        self.min_before.append(min(val, self.min_before[-1]) if self.min_before else val)

    def pop(self) -> None:
        self.items.pop()
        self.min_before.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_before[-1]
