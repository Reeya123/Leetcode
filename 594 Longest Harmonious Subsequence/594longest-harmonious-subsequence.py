class Solution(object):
    def findLHS(self, nums):
        count = {} #key: num and value:number of occurences 
        maxlength = 0 

        for elem in nums:
            if elem in count:
                count[elem] += 1

            else:
                count[elem] = 1

        
        for num in count:
            if num + 1 in count:
                maxlength = max(maxlength , count[num] + count[num + 1])

        return maxlength