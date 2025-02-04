class Solution(object):
    def productExceptSelf(self, nums):
        #initialize 3 arrays
        prefix = [1] * len(nums) #store products of all elements before that index 
        suffix = [1] * len(nums)  #store products of all elements after that index 
        output = [1] * len(nums)
        
        
        #Calculate prefix! 
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        #Calculate suffix! 
        for i in range(len(nums) - 2, -1 , -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            
        #Calculate answer 
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
    
        
        return output
            