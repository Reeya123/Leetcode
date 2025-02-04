# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        def dfs(node, currval):
            if node is None:
                return 0

            currval = currval * 2 + node.val
            if not node.left and not node.right:
                return currval

            leftsum = dfs(node.left , currval)
            rightsum = dfs(node.right, currval)

            return leftsum + rightsum

        return dfs(root, 0)
        