class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize pointers to create left and right boundaries 
        left = 0 
        right = len(nums) - 1
        
        #loop holds true unntil target is found or search space is exhausted 
        while left <= right:
            #calculat the mid index 
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            #check if left is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: #section/subarray is valid 
                    right = mid - 1
                    
                # subarray is invalid, check in the right section     
                else : 
                    left = mid + 1
                    
            #check if right is sorted
            else :
                if nums[right] >= target > nums[mid]: #section/subarray is valid 
                    left = mid + 1
                    
                # subarray is invalid, check in the left section     
                else: 
                    right = mid - 1 
                    
        return -1