class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        #iterate over the string 
        for curr in s:
            if curr == "*":
                if stack[-1] != "*" and len(stack) != 0:
                    stack.pop()

            else:
                stack.append(curr)

        return "".join(stack) 
