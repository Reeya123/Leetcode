class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        res = []
        for word in words:
            lower_word = word.lower() #converts every letter to lowercase 

            #determine which row first letter belongs to 
            if lower_word[0] in row1:
                #logic to check if all the letters in the word belong to same row 
                for letter in lower_word:
                    if letter not in row1:
                        break
                else:
                    res.append(word)
                
            elif lower_word[0] in row2:
                for letter in lower_word:
                    if letter not in row2:
                        break
                else:
                    res.append(word)
                        

            elif lower_word[0] in row3:
                for letter in lower_word:
                    if letter not in row3:
                        break
                else:
                    res.append(word)
                        
            else:
                #invalid char
                continue
        
        return res