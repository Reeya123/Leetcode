class Solution(object):
    def lemonadeChange(self, nums):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap = {5: 0 , 10: 0 , 20: 0 } #key: 5, 10 value: bills we have
    
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            
            if nums[i] == 10:
                if hashmap[5] > 0:
                    hashmap[5] -= 1
                else:
                    return False
            #if bill=20; return 3 bills of 5 or 1bill of 5 and 1 of 10
            if nums[i] == 20:
                
                    
                if hashmap[5] >= 1 and hashmap[10] >= 1:
                    hashmap[5] -= 1
                    hashmap[10] -= 1
                
                elif hashmap[5] >= 3:
                    hashmap[5] -= 3
                else:
                    return False 
                
        return True
            