class Solution(object):
    def plusOne(self, nums):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = "".join(map(str, nums))
        incrnumber = int(number) + 1 #integer - 1357
        return [int(digit) for digit in str(incrnumber)]