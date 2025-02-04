class Solution(object):
    def maxArea(self, heightarr):
        
        l = 0 
        r = len(heightarr) - 1
        maxarea = 0
        while l < r:
            height = min(heightarr[l], heightarr[r])
            width = abs(r - l)
            
            area = height * width
            maxarea = max(maxarea, area)
            
            if heightarr[l] < heightarr[r]:
                #move the shorter line 
                l += 1
                
            else:
                r -= 1
                
                
        return maxarea