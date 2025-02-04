class Solution(object):
    def isPalindrome(self, x):
        inputnum = x
        newnumber = 0
        while x > 0:
        
            newnumber = newnumber * 10 + (x % 10)
            x = x // 10

        return newnumber == inputnum



        