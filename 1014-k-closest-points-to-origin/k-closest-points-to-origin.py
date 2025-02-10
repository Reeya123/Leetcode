class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
   
    
        minheap = []
        res = []
        for x,y in points:
        
            distance = x**2 + y**2
        
            heapq.heappush(minheap, (distance, [x,y]))
            
        for i in range(k):
            distance, point = heapq.heappop(minheap)
            res.append(point)
        return res