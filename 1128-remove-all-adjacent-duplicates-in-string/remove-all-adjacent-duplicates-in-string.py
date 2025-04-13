class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                #duplicate found- pop it 
                stack.pop()
                continue
            stack.append(char)
            
        return "".join(stack)