# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def check_BST(node, minimum , maximum):
            if node is None: # the tree is empty; a leaf node 
                return True # An empty tree/ empty subtreeis valid bst by default
            
            if not minimum < node.val < maximum:
                return False
            
            return check_BST(node.left , minimum , node.val) and check_BST(node.right , node.val , maximum)
            
            
            
            
        return check_BST(root, float("-inf"), float("inf"))
        