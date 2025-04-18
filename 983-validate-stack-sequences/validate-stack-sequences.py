class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushstack = [] # push elements 
        popstack = [] # stores result stack
        popIndex = 0
        
        for elem in pushed:
            pushstack.append(elem)
            while pushstack and pushstack[-1] == popped[popIndex]:
                
                popstack.append(pushstack.pop())
                popIndex += 1
                
            
        return popstack == popped 