
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