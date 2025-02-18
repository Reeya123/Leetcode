class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] #stores all combinations 
        sol= [] # partial sol - dynamically creates individual combinations - we append and pop elements from this list
        n = len(nums)
        def backtrack(index, currsum):
            #base cases
            
            if currsum == target:
                res.append(sol[:])
                return
            if currsum > target or index == n: #reached the end of the array , no more numbers to consider 
                return 
            
            #choice of not picking the number. so index increases but sum rtemaains same
            backtrack(index + 1, currsum)
            
            #choice of picking the number. so index remains the same and curr num gets addded to currsum
            sol.append(nums[index])
            backtrack(index, currsum + nums[index])
            sol.pop()
        backtrack(0,0) 
        return res
        