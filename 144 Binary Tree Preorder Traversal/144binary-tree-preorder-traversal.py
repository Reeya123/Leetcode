# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        def preorder(node):
            if node is None:
                return []

            
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)
            return res

        return preorder(root)
            
        