class Solution(object):
    def romanToInt(self, s):
        hashmap = {"I" : 1 , "V" : 5 ,"X" : 10 ,"L" : 50 ,"C" : 100 ,"D" : 500 ,"M" : 1000 }
        totalcount = 0
            #s = "LVIII"
            
            
        for char_index in range(len(s) - 1):
            if hashmap[s[char_index]] > hashmap[s[char_index + 1]]:
                totalcount += hashmap[s[char_index]]
                
                    
            elif hashmap[s[char_index]] < hashmap[s[char_index + 1]]:
                totalcount -= hashmap[s[char_index]]
            else:
                totalcount += hashmap[s[char_index]]

        return totalcount + hashmap[s[-1]]
                                                              