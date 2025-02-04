# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        # If the tree is empty, it is symmetric
        if root is None:
            return True
        
        # Call the helper function to compare left and right subtrees
        return self.isMirror(root.left, root.right)  # 'self.isMirror' is calling a method inside the Solution class, 'root.left' and 'root.right' are attributes of the TreeNode instance
    
    def isMirror(self, left, right):
        # If both subtrees are empty, they are symmetric
        if left is None and right is None:
            return True
        # If one of the subtrees is empty and the other is not, they are not symmetric
        if left is None or right is None:
            return False
        # Check if the current nodes are equal and their subtrees are symmetric
        return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)