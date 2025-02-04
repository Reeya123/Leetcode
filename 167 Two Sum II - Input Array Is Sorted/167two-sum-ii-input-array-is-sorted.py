class Solution(object):
    def twoSum(self, numbers, target):
        l = 0 
        r = len(numbers) - 1
        
        while l < r:
            currsum = numbers[l] + numbers[r] 
            
            if currsum == target:
                return l+1, r+1
            
            elif currsum < target:
                l += 1
            else:
                r -= 1

            