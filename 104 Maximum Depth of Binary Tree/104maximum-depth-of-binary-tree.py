# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def depth(node):
            if not node:  # Base case: if node is None, depth is 0
                return 0
            
            # Recursively compute the depth of the left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # The depth of the current node is the max depth of the subtrees plus 1
            return max(left_depth, right_depth) + 1

        # Call the helper function and return the result
        return depth(root)