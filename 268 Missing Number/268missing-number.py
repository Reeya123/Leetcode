class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_n = (n * (n + 1)) // 2
        sum_nums = sum(nums)
        
        missingNumber = sum_n - sum_nums
        
        return (missingNumber)
        