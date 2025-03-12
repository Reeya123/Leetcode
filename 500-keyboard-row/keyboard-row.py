class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop") ##set uses hashing so lookup is O(1) while string lookup is O(m) - m is len of teh string 
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            lower_word = set(word.lower()) #converts every letter to lowercase 

            #determine which row first letter belongs to 
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                res.append(word)
        
        return res

        '''
to use issubset, both the words have to be a set - set(word).issubset(set(bigword))
It returns True if all elements of the first set are present in the second set, and False otherwise. 
It can be used with the <= operator as a shortcut.
'''