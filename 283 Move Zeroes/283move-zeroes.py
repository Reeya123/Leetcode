class Solution(object):
    def moveZeroes(self, nums):
        '''
        swap with zeros using 2 pointers until all zeros are at th ened of the array

        '''
        l = 0 
        r = 0
        for r in range(len(nums)):
            if nums[l] == 0: #we want to do a wap only if nums at l and r aarent same 
                if nums[l] == nums[r]:
                    r += 1
                else:
                    nums[l] , nums[r] = nums[r], nums[l]
                    l+= 1
                    r+=1

            else:
                l += 1
                r += 1
                
        return nums