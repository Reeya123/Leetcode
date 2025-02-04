class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)< 2:
            return ""
        charset = set(s)
            
            
        for index, elem in enumerate(s):
            if elem.swapcase() not in charset:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index + 1:])
                
                return left if len(left) >= len(right) else right
            
        return s
            