# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        total_depth = 0 
        while stack:
            node , depth = stack.pop()
            '''
            the reason why this is needed is because stack might append None nodes too
            The stack initially starts with (root, 1), which means it contains a valid node.
However, as the algorithm progresses, it pushes node.left and node.right into the stack.
If a node doesn’t have a left or right child, it still pushes (None, depth + 1).
Later, when stack.pop() retrieves (None, depth), None does not have children, causing an error when accessing node.right or node.left.
            '''
            if node:
                #process each node and add the depth 
                total_depth = max(total_depth, depth)

                if node.right:
                    stack.append((node.right, depth + 1))
                if node.left :
                    stack.append((node.left, depth + 1))
        return total_depth