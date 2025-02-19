class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()
        n = len(nums)
        def backtrack(index):
            
            #Collect all subsets at every recursion level- not only after reaching the end of the tree (like subset 1 - in which we append only the leaf nodes)
            res.append(sol[:])
                
            
            for i in range(index, n):
                #Skip duplicate elements at the same recursive level
                if i > index and nums[i] == nums[i-1]:
                    continue #dont pick 
                
                #Pick the current number
                sol.append(nums[i])
                #explore further
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res

