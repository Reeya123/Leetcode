class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftsum = 0
        
        for i in range(len(nums)):
            rightsum = total - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
            
        return -1
                