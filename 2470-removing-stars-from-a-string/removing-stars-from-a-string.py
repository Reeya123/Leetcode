class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
    
        for char in s:
            if stack and char == "*":
                stack.pop()
                continue
                print(stack)
            stack.append(char)
            
        return "".join(stack)