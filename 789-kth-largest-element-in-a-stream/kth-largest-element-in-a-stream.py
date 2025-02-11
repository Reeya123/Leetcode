class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minheap = nums #minheap to store k large elements. smallest in this heap is the largest element
        heapq.heapify(self.minheap)
        
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, value: int) -> int:
        heapq.heappush(self.minheap, value)
        
        #if size of heap increases, renov e the smallest element
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)