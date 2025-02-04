class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num_str = str(num)
        count = 0
        
        for i in range(len(num_str) - k + 1):  # Slide the window of size k
            substring = num_str[i:i+k]
            divisor = int(substring)
            
            if divisor != 0 and num % divisor == 0:  # Check if it's a valid divisor
                count += 1
        
        return count

            