class Solution(object):
    def removeStars(self, s):
        stack = []
        for elem in s:
            if elem == '*' and stack:
                stack.pop()
                
            else:
                stack.append(elem)
        res = "".join(stack)        
        return res
        