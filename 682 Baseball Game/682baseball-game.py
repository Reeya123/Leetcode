class Solution(object):
    def calPoints(self, ops):
        stack = []
        for elem in ops:
            
            if elem == '+':
                if len(stack) >= 2:
                    res = stack[-1] + stack[-2]
                    stack.append(res)
                    print("Added the top 2 elems", stack)
                else:
                    print("couldnt Add the top 2 elems", stack)
                    return 0
            elif elem == 'C' and stack:
                print("Popping the top elem", stack)
                stack.pop()
            elif elem == 'D'and stack:
                
                res = stack[-1] * 2
                print("Added the double of top elem", stack)
                stack.append(res)
            else:
                print("Added the int elems", stack)
                stack.append(int(elem))
        print(stack)
        return sum(stack)