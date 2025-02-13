'''
    bin(n).count("1") is an elegant Python-specific solution but converts n to a string, which may have hidden overhead.
    Brian Kernighan’s approach works efficiently in any language.
    The naive O(1) method iterates over all 32 bits of n, even if n only has a few set bits.
    Brian Kernighan’s method (O(log n)) only iterates as many times as there are 1s in n.
    If n = 1000000, there are only ~17-20 set bits, so the loop runs 17-20 times instead of always running 32 times.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:

        ans = 0 #number of 1 bits
        while n != 0:
            '''
            n & (n - 1) removes the lowest set bit of n in each iteration until 0.
            Time Complexity: O(log n)
            Since the loop runs only as many times as there are set bits, it runs log n times in the worst case.
            '''
            n = n & (n - 1)
            ans += 1
        return ans       