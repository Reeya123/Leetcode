class Solution(object):
    def maxSubArray(self, nums):
        '''
        2 solutions :

        1 - Brute force approach 
        - We run 2 nested loops , check for each subarray and return the max sum. 
        - problem - Slow, inefficient: O(n^2) 

        2 - Kadane Algorithm 
        - At every step ,we calculate the best possible outcome 

        - 2 variables : currsum, maxsum 
        - If currsum + Currelem < currelem, its better to start a new subarray
        - update the maxsum accordingly 
        - TC: O(n) 

        '''

        currsum = 0
        maxsum = nums[0]
        
        for currelem in nums: 
            currsum = max(currelem , currsum + currelem) #If currsum + Currelem < currelem, its better to start a new subarray
            
            maxsum = max(maxsum, currsum)
            
        return maxsum

        