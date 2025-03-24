
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        hashmap = defaultdict(int) #key: elements ; value: frequency 
        res = []
        for subarray in nums:
            for element in subarray:
                hashmap[element] += 1
                
        for key in hashmap:
            if hashmap[key] == n:
                res.append(key)
                
        return sorted(res)