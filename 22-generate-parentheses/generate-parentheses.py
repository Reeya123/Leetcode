class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #2 choices - 1. Add an opening bracket 2.Add a closing bracket
        #take one decision -> backract on it(includes reccursion), explore the entire branch -> backtrack to prev call, explore it all -> so on. 
        
        #ddefine 2 g lobal lists 
        res = [] #includes all valid subsets 
        stack = [] #helps build a valid subset one by one
        
        def backtrack(NumOB, NumCB):
            #base case
            if NumOB == NumCB == n : #Reched limit, cqant add anymore brackets to the stqack 
                res.append("".join(stack))
                return 
            
            #adding open brackets 
            if NumOB < n:
                stack.append('(')
                backtrack(NumOB + 1 , NumCB)
                stack.pop()
            if NumCB < NumOB:
                stack.append(')')
                backtrack(NumOB , NumCB + 1)
                stack.pop()
                
                
        

        backtrack(0,0)
        return res