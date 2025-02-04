class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''hashmap = {} #key = int ; value :number of occ 
        for index in range(len(nums)):
            if nums[index] not in hashmap:
                hashmap[nums[index]] = 1
                
            else:
                hashmap[nums[index]] += 1
                
        #find the max ocurence         
        maxoccurence = max(hashmap.values())
        
        #find the key that matches the maxoccurence 
        '''
        '''if i have the value in hashmap, how do i return its key?
        search key-values pairs in hashmap usng hashmap.items()'''
        
        '''
        for key, value in hashmap.items():
            if value == maxoccurence and maxoccurence > (len(nums) // 2):
                return key #majority elemey'''

        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate 