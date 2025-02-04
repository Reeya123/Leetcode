class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1 
        while l < r:
            #alphanumeric - 0-9; A-Z; a-z
            #skip non alphanumeric- spaces, colons etc 
            while l < r and not s[l].isalnum():
                l +=  1
            while l < r and not s[r].isalnum():
                r -=  1
            #if the loop reaches here means both are alphanumeric ; so compare 
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True 