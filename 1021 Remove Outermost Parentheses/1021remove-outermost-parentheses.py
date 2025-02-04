class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0: #append only if its not outermost
                    res.append(char)
                    
                depth += 1
                
            elif char == ')':
                depth -= 1
                if depth > 0:
                    res.append(char)
        res = ''.join(res)
        return res
            