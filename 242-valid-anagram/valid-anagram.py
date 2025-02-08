class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Valid anagram 

        Time: O(n)
        Space: O(n) - theoretical worst case scenario
        O(k)- theoretical Avg space complexity - k is number of unique elems 
        O(1)Since there are at most 26 unique characters, the space required for the hashmaps is constant and does not grow with 
        the size of the input strings.
        '''
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
        '''unerthe hood, hashmap s checks for each key in t and then its values. essentially making it O(n) but looking up in 
            hashmap is O(1) so its a total of O(n) complexity
        '''