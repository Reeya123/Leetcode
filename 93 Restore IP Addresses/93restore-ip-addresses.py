class Solution(object):
    def restoreIpAddresses(self, s):
        res = [] # stores the final valid ip addresses -  
        if len(s)> 12:
            return []
        
        def backtrack(start , parts): #parts = ["255" , "255" , "111" , "35"]
            if len(parts)== 4  and start == len(s):
                res.append(".".join(parts))
                return []
            
            if len(parts) == 4: #if len of parts is 4 and we havent used all the strings ; its invalid 
                return []
            
            #sploit the string into 1 , 2 or 3 digits then, backtract on theose to check for valid paths 
            for length in range(1,4): #check 3 times ; this is where we are making a decision tree 
                if start + length > len(s): #out of bounds
                    break 
                    
                currpart = s[start: start+ length]
                
                if ValidPart(currpart):
                    parts.append(currpart)
                    backtrack(start + length , parts)
                    parts.pop()
                
                

        def ValidPart(part):
            # Part is invalid if it starts with '0' but has more than one digit
            if len(part) > 1 and part[0] == '0':
                return False
            # Part must be in range 0-255
            return 0 <= int(part) <= 255
        # Start backtracking from index 0 with an empty list of parts
        backtrack(0, [])
        return res
        