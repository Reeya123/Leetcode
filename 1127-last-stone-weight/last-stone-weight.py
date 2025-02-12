class Solution:
    '''
    solution:
    []
    #convert the aarray into a maxheap 
    get the x and y; caalculate new values and update the array accordingly 
    space ; O(n) for storing the heap 
    time: O(n log k)
    '''
    def lastStoneWeight(self, nums: List[int]) -> int:
        maxheap = [-stone for stone in nums] # O(n) space
        heapq.heapify(maxheap) #O(n) time

        #Keepdoing it until we have 1 or no stones left 
        while len(maxheap) > 1:
            y = -heapq.heappop(maxheap) #O(log k) time
            x = -heapq.heappop(maxheap) #O(log k) time

            if x != y:
                heapq.heappush(maxheap, -(y - x)) #O(log k) time


        return -maxheap[0] if maxheap else 0 