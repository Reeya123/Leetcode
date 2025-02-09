'''
solution 1:
sort every string in the list 
hashmap - key: sorted string; value: the anagrams 
return the hashmap values as a list 
Time: n * m log m 

solution 2: without sorting 
count frequencies of chqaracters and save t hem as keys 
create an array of size 26 
add the frequency count of each element and make it a tuple 
add to hashmap as key 
check for each string and add as value if frequency count is same 

'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            frequency_array = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                frequency_array[index] += 1
            
            key = tuple(frequency_array)
            hashmap[key].append(string)
            
        return list(hashmap.values())