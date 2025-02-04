class Solution(object):
    def isAnagram(self, s, t):
        hashmap_s = {} #key - char ; value : number of occurences
        hashmap_t = {} #key - char ; value : number of occurences
        
        #edge case:
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in hashmap_s:
                hashmap_s[char] = 1
            else:
                hashmap_s[char] += 1
                
        for char in t:
            if char not in hashmap_t:
                hashmap_t[char] = 1   
            else:
                hashmap_t[char] += 1
                
        #compare the hashmaps 
        if len(hashmap_s) == len(hashmap_t):
            
            for char in hashmap_s:
                if char not in hashmap_t or hashmap_s[char] != hashmap_t[char]:
                    return False 
            
            return True
        return False
    
        