class Solution(object):
    '''
    solution: #Binary search - O(log(n))
l = 0 r = len(nums) - 1
calculate mid elem = l + r // 2 (int div)
check if target == mid elem
    yes - return the elem
elsif target > mid elem (look in the right part of the array)

else : look in the left part of the array 

'''
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)- 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid  + 1
                
            elif nums[mid] > target:
                right = mid - 1
                
                
           
        return left
        
            