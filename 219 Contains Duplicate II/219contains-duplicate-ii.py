class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
    
        for index, elem in enumerate(nums):
            if elem in dic and index - dic[elem] <= k:
                return True
            
            dic[elem] = index
            
        return False
        