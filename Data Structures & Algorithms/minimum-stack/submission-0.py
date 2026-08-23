class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        ret = self.stack.pop()
        self.stack.append(ret)
        return ret


    def getMin(self) -> int:
        return self.minstack[-1]
        
