class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        #initialize the minheap 
        minheap = [] # tuple(distance , [x, y])
        result = []
        #distance = x**2 + y**2
        
        #cqalc the distance and push to heap
        for x,y in points:
            distance = x**2 + y**2
            #The heap will automatically keep the smallest distances at the top.
            heapq.heappush(minheap , (distance , [x, y]))
            
        for distance in range(k):
            distance, point = heapq.heappop(minheap)
            result.append(point)
            
        return result
            