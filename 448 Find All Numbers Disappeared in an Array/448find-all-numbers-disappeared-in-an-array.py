class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        res = []
        numset = set(nums)
        for i in range(1, n+1):
            
            if i not in numset:
                res.append(i)
        return res
            