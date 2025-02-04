class Solution(object):
    def areAlmostEqual(self, s1, s2):
        diff = []
        if s1 == s2:
            return True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                
        if len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]:
            return True
                
        return False
        