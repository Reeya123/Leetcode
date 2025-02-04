class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} #key : curr integer ; Val : index 
        for index in range(len(nums)):
            diff = target - nums[index]
            #check if target is in hashmap
            if diff in hashmap:
                return [index, hashmap[diff]]
                
                
            else:
                hashmap[nums[index]] = index