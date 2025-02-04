class Solution(object):
    def numIdenticalPairs(self, arr):
       
        count = 0
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i] == arr[j]:
                    
                    count +=1
                
  


        return count