class Solution(object):
    def maxSubsequence(self, nums, k):
        sortednums = sorted(nums)
        res = []
        for elem in sortednums[- k ::]:
            res.append(elem)
            
        return res
            