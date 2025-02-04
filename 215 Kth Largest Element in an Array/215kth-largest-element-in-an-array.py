import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      #convert a list into a max-heap inplace
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        for count in range(k):
            largest = -heapq.heappop(nums)
            
        return largest  