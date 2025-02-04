# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        def NumberofNodes(node):
            if node is None:
                return 0
            leftsubtree = NumberofNodes(node.left)
            rightsubtree = NumberofNodes(node.right)

            return leftsubtree + rightsubtree + 1
        return NumberofNodes(root)