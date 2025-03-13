class MyQueue:

    def __init__(self):
        self.stack1 = [] #used to push elements 
        self.stack2 = [] #used to pop/peek elements 

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        ## if stack2 is empty - transfer all elements from stack1 to stack 2 
        self.transfer_stacks()
        return self.stack2.pop() if self.stack2 else None

        

    def peek(self) -> int:
        self.transfer_stacks()
        return self.stack2[-1] if self.stack2 else None

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False

    def transfer_stacks(self):
        if not self.stack2: #transfer only if stack2 is empty ; otherwise dont disturb 
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()