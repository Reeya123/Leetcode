class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        largest = 0
        for num in hashset:
            if (num - 1) not in hashset: #this element starts the sequence 
                nextnum = num + 1
                length = 1
                while nextnum in hashset:
                    length += 1
                    nextnum += 1
                largest = max(largest, length)
        return largest