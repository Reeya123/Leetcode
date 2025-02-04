class Solution(object):
    def maxDepth(self, s):
        totalcount = 0
        currcount = 0
        for char in s:
            
            if char == '(':
                
                currcount  += 1
                totalcount = max(currcount , totalcount)
            elif char == ')':
                currcount -= 1
                
        return totalcount
            