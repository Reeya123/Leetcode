# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        def booleantree(node):
            if node is None:
                #Empty tree - No node
                return False
            if node.val == 0:
                return False
                # The leaft node is False- Return False
            if node.val == 1:
                return True
                # The leaf node is true, return True

            if node.val == 2: #OR operation
                leftsubtree = booleantree(node.left) if node.left else False #Boolean value
                rightsubtree = booleantree(node.right) if node.right else False

                return leftsubtree or rightsubtree

            if node.val == 3:
                leftsubtree = booleantree(node.left) if node.left else False
                rightsubtree = booleantree(node.right) if node.right else False

                return leftsubtree and rightsubtree

        return booleantree(root)