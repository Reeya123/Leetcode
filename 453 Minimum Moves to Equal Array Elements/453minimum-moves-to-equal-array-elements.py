class Solution(object):
    def minMoves(self, nums):
        moves = 0 
        maxval = min(nums)
        currsum = sum(nums)
        for num in nums:
            moves = abs(currsum - (len(nums) * maxval))

            
        return moves
        