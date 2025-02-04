class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1 = ''
        w2 = ''
        
        for elem in word1:
            w1 += elem
            
        

        for elem in word2:
            w2 += elem

        

        if w1 == w2:
            return True
        
        return False
