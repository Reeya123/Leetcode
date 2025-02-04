# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0 

        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right) 

            diameter = left_depth + right_depth 
            self.max_diameter = max(self.max_diameter, diameter)
        
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return self.max_diameter
        
        