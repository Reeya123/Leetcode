class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        greaterval = {} #value: greater than value
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                greaterval[stack.pop()] = num

            stack.append(num)

        for remaining in stack:
            greaterval[remaining] = -1

        result = [greaterval[num] for num in nums1]

        return result
