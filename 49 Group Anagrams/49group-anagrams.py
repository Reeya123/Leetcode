class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {} #key: the refernece word ; value : all the matched anagrams 
    
        for string in strs:
            print(string)
            sortedword = "".join(sorted(string))
            
            print(sortedword)
            if sortedword in hashmap:
                #yes
                hashmap[sortedword].append(string)
                
            else:
                hashmap[sortedword] = [string]
                
        return list(hashmap.values())