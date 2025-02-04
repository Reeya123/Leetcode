class Solution(object):
    def removeDuplicates(self, s, k):
        stack = [] # pair : character: count
        for elem in s:
            if stack and stack[-1][0] == elem:
                stack.append((elem, stack[-1][1] + 1))
                
                if stack[-1][1] == k:
                    for _ in range(k):
                        stack.pop()
                        
                    
            else:
                stack.append((elem, 1))
                
                
        res = "".join(char for char,count in stack)
        return res
            