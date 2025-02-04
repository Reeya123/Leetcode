class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        if len(arr) < k: # Not enough elements in the arr
            return 0
        
        window = sum(arr[:k])
        count = 0 
        reqsum = k * threshold  # sum of window / k >= threshold -> sum of window >= threshold * k
        
        if window >= reqsum:
            count += 1
            
        #slide the window
        for elem in range(k,len(arr)):
            window += arr[elem] - arr[elem - k]
            if window >= reqsum:
                count += 1
            
            
        return count