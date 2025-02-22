class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
    
        res = []
        sol = []
        hashmap = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "qprs",
                "8": "tuv",
                "9": "wxyz",
            }
        #since dfs is a nested function , the res, sol, hashmap and even digits are accessible to it without even passingitdirectly to the dfs 
        def dfs(d_index):
            if d_index == len(digits):
                res.append("".join(sol))
                return 
                
                
            for letter in hashmap[digits[d_index]]:
                sol.append(letter)
                dfs(d_index + 1)
                
                sol.pop()
        dfs(0)
        return res