class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k:
            newstring = ''
            for index in range(len(word)):
                
                newword = chr(ord(word[index])+ 1)
                newstring += newword
            word += newstring
        return word[k - 1]
 