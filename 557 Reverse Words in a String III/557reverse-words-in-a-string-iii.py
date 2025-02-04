class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        res = []
        for word in words:
            reversed_word = word[::-1]
            res.append(reversed_word)
       
        return ' '.join(res)
        