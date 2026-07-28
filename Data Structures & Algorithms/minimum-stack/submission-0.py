class MinStack:

    def __init__(self):
        self.items = []
        self.min_val = []
        

    def push(self, val: int) -> None:
        self.items.append(val)

        if not self.min_val:
            self.min_val.append(val)
        else:
            self.min_val.append(min(val, self.min_val[-1]))


    def pop(self) -> None:
        if self.items:
            self.items.pop()
            self.min_val.pop()
        

    def top(self) -> int:
        return self.items[-1] if self.items else None
        

    def getMin(self) -> int:
        return self.min_val[-1] if self.min_val else None

        
