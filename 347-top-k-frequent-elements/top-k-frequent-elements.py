from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int) #key:num; value: frequency
        heap = []
        res = []
        #first build the hashmap 
        for elem in nums:
            hashmap[elem] += 1
            
        #second, push the (- freq, value) tuple to maxheap. 
        #pop k elements based on the freq value 
        for key in hashmap:
            heapq.heappush(heap, (-hashmap[key], key))
            
            
        while k > 0 and heap:
            freq , value = heapq.heappop(heap)
            k -= 1
            res.append(value)
            
        return res