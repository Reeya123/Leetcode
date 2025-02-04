class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue  #skip duplicate i values
            l = i + 1
            r = len(nums) - 1
            while  l < r:
                currsum = nums[i] + nums[l] + nums[r]
                if currsum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # Skip duplicates for `l` and `r`
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    l += 1
                    r -= 1
                elif currsum < 0:
                    l += 1
                
                else:
                    r -=1

        return res
            