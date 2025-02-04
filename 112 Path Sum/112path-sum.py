# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def pathsum(node, target):
            if node is None:
                return False

            if not node.left and not node.right:
                return node.val == target

            
            target -= node.val

            return pathsum(node.left , target) or pathsum(node.right, target)

        return pathsum(root, targetSum)
        