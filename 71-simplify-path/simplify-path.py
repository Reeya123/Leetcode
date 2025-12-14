class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splitlist = path.split("/")

        for elem in splitlist:
            if elem == '.' or elem =='':
                continue

            elif elem == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(elem)

        return '/' + '/'.join(stack)