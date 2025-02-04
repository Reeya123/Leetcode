class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True
        if len(t) < len(s):
            return False
        
        
    
        l = 0 #pointer for s
        r = 0 #pointer for t
        #r goes through indices 0 to len(t) - 1. The loop exits when r == len(t).
        while r < len(t):
            if l < len(s) and s[l] == t[r]: #if theres a char match ; increment both pointers 
                
                l += 1
            r += 1 #increment the r pointer regardles
            
            #This happens when all characters of s are matched in t. The pointer l increments past the last index of s, making l == len(s) true.
            if l == len(s):
                return True
            
        return False
            