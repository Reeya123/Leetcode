
class Solution(object):
    def getConcatenation(self, nums):
        res = []
        for elem in nums:
            res.append(elem)
            
        for elem in nums:
            res.append(elem)
        return res
    
solution = Solution()
result = solution.getConcatenation([1,2,3,4])

      