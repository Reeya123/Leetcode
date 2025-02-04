class Solution(object):
    def lengthOfLastWord(self, s):
        splittedString=s.split()
        return (len(splittedString[-1]))
        