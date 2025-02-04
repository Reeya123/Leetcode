class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        left , right = 0, k - 1
        sub = float("inf")
        
        

            
        while right < len(nums):
            
            sub = min(sub, nums[right] - nums[left])
            left, right = left + 1, right + 1
        
        return sub
        
        