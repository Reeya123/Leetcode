class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {} #key: unique characters in s value:Num of occurences 
        hashmap_t = {} 
        if len(s) != len(t):
            return False #Not an anagram 
        for elem in s:
            if elem in hashmap_s:
                hashmap_s[elem] += 1
            else:
                hashmap_s[elem] = 1
                
        for elem in t:
            if elem in hashmap_t:
                hashmap_t[elem] += 1
            else:
                hashmap_t[elem] = 1  
                
        return hashmap_s == hashmap_t