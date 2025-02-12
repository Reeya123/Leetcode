class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        maxheap = [-stone for stone in nums]
        heapq.heapify(maxheap)

        #Keepdoing it until we have 1 or no stones left 
        while len(maxheap) > 1:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            
            if x != y:
                heapq.heappush(maxheap, -(y - x))
                
        
        return -maxheap[0] if maxheap else 0