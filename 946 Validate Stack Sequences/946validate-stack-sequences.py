class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        popindex = 0
        
        for elem in pushed:
            
            stack.append(elem)
            while stack and popped[popindex] == stack[-1]:
                stack.pop()
                popindex +=1
        return not stack
            