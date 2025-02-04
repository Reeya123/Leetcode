# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        def dfs(node):
            if node is None:
                return True
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            lefttree = dfs(node.left)
            righttree = dfs(node.right)
            return lefttree and righttree
        return dfs(root)
        