class Solution(object):
    def balancedStringSplit(self, s):
        countR = 0 #keeps a track of R strings
        countL = 0 #keeps a track of L strings 
        countBS = 0 
        for index in range(len(s)):
            if s[index] == 'R':
                countR += 1
            else:
                countL += 1
            if countR == countL:
                countBS += 1
                #Reset the counters
                countL = 0 
                countR = 0
                
        return countBS  
            