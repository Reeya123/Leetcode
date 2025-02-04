class Solution(object):
    def maxAscendingSum(self, nums):
        '''
iterate over the nums array 
 
if nums[i] > nums[i -1 ]
sum  += nums[i]
        '''
        maxsum = 0
        currsum = nums[0] 
        
        for i in range(1 , len(nums)):
            
            
            if nums[i] > nums[ i - 1]:
                
                #add prev elem to curr sum 
                currsum += nums[i]
                
                
            else:
                maxsum = max(maxsum , currsum)
                currsum = nums[i]
                
                
            
        maxsum = max (maxsum , currsum)
        return maxsum
            

