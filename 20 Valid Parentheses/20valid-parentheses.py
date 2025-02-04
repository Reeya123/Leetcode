class Solution(object):
    '''
hashmap - to map the key and values pairs 
initialize an empty stack
iterate over each char in the string:
check if char is in hashmap?#This would check the keys(closing brackets) 
if yes, its a closing bracket  - ( check the stack top  and the stack isnt empty), it must be an openning bracket
if no - its an opening bracket; we simply append it to the stack 

lastly, return True if stack is empty 
'''


    def isValid(self, s):
        hashmap = {')' : '(' , '}' : '{' ,']' : '['  } #key: closing brack ; value: opening bracket
        
        stack = []
        
        
        for char in s:
            if char in hashmap: #char = closing bracket 
                if stack and stack[-1] == hashmap[char]:
                    
                    stack.pop()
                else:
                    return False
                
            else: #char is opening brac
                stack.append(char)
                
                
                
        return len(stack) == 0