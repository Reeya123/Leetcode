class Solution(object):
    def compress(self, chars):
        r = 0 # iterate the array and count the no of occurence
        l = 0 #to rewrite the array with compressed values
        
        while r < len(chars):
            count = 0 
            curroccur = chars[r] 
            
            
            while r < len(chars) and chars[r] == curroccur:
                count += 1
                r += 1
            
            # either the next elem is diff or we have reached the end of the array 
            chars[l] = curroccur #currchar = a
            l += 1 # l = 1
            
            if count > 1: #count = 1 , we dont havr to do anbything count = 12 
                for c in str(count):
                    chars[l] = c
                    l += 1
                    
        return l 
        