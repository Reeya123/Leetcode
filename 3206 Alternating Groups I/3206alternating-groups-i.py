class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        circlearr = [colors[-1]] + colors + [colors[0]]
        print(circlearr)
        L= 0 
        
        count = 0 
        for R in range(L+2,len(circlearr)):
            
            if circlearr[R] == circlearr[L] and circlearr[R - 1] != circlearr[R]:
                
                count += 1
                print(L,R,count)
            L += 1
            R += 1
                
        return count
        
            