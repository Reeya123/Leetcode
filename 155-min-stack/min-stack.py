class MinStack:
    

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
    
        self.stack.append(val)
        #append the curr val to minstack if - 
        # - min stack is empty 
        # - min stack top <= curr val
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()

            if self.minstack and popped == self.minstack[-1]:
                self.minstack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()