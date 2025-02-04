class Solution(object):
    def removeDuplicates(self, nums):
        l = 0 
        count = 0
        for right in range(len(nums)):
            if nums[right] != nums[l]:
                l +=1
                nums[l], nums[right] = nums[right], nums[l]
                count += 1
        return count+1
        
        