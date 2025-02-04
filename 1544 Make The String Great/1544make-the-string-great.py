class Solution(object):
    def makeGood(self, s):
        stack = []
    
        for elem in s:
            if elem == elem.upper():
                if stack and stack[-1] == elem.lower():
                    stack.pop()
                    #remove the upper and lower alphabet
                    #print("Popping the top elem coz it was small and to be added elem was cap", stack)
                else:
                    stack.append(elem)
                    #print("elem appended- cap", stack)
            elif elem == elem.lower():
                if stack and stack[-1] == elem.upper():
                    stack.pop()
                    #remove the upper and lower alphabet
                    #print("Popping the top elem coz it was cap and to be added elem was small", stack)
                else:
                    stack.append(elem)
                    #print("elem appended- small", stack)
            res = "".join(stack)
        return res
            