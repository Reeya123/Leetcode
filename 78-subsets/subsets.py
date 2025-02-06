class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        #define 2 global lists 
        res = []
        stack = []
        
        #defne function backtrack thqat takes in the index. iterqate over the nums array 
        def backtrack(i):
            #if we reach leaf node,copt the stack(has the individial combinations) to the res array.
            if i == n: #we want the index to go out of bounds. hence not n - 1
                res.append(stack[:])
                return
        # if i!= n; 2 paths - Dont append nums[i]; Append Number 
            backtrack(i+1) #we dont want to append nums, we say just move on and backtrack to next number 
            
            
            #pick the num
            stack.append(nums[i])   
            backtrack(i+1)
            #undo the step. Pop the number appended 
            stack.pop()
        
        
        
        backtrack(0)
        return res