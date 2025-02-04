class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap ={} ## number: frequency
        
        for number in nums:
            if number in hashmap:
                hashmap[number] += 1
                
            else:
                hashmap[number] = 1
            
        
        # Sort the hashmap based on frequency in descending order
        sorted_hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        
        # Get the top k frequent elements
        top_k = [item[0] for item in sorted_hashmap[:k]]
        
        return top_k