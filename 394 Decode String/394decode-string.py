class Solution(object):
    def decodeString(self, s):
        stack = []
    
        for char in s:
            if char != ']':
                stack.append(char)
                
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()
                #stack doesnt have any content of the curr bracket 
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                stack.append(substr * int(k))
                    
        return ''.join(stack)