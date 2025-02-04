class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0 
        maxlength = 0
        currstring = ""
        for r in range(len(s)):
            if s[r] in currstring:
                '''
                #if duplicate
                
                - move l pointer to r; we dont want to add anything until the repeated char
                - check the maxlength with currstring 
                - empty the currstring and add the s[l]
                '''
                l = r
                maxlength = max(maxlength, len(currstring))
                currstring = ""
                currstring += s[l]
        
            else: #no duplicate, add char r in currstr
                currstring += s[r]
            maxlength = max(maxlength, len(currstring))
        return maxlength
                    