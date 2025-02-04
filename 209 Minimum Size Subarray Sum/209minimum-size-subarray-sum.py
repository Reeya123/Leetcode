class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        minlength = float('inf')
        sum_window = 0

        for r in range(len(nums)):
            sum_window += nums[r]

            while sum_window >= target:
                minlength = min(minlength, r - l + 1)
                sum_window -= nums[l]
                l += 1

        return minlength if minlength != float('inf') else 0





        