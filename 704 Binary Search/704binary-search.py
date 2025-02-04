class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) + 1 // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: #search left 
                r = mid - 1
            elif nums[mid] < target: #search right 
                l = mid + 1
                
            
            
        return -1 