# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left , p, q)
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        #If one node is in the left and the other in the right, or if root is equal to p or q, then root is the LCA.
        else:
            return root


'''
LCA - closest common parent to the nodes p and q 
        6
       / \
      2   8
     / \  / \
    0   4 7  9
       / \
      3   5

if p and q are either sides of the subtree:p = 3, q = 5, lca - 4
if either of them is the subroot: p = 2,q =4, lca -2 

can you speak exactly ike this??
Intuition
Since it is a BST, we know:

The left subtree contains smaller values than the root.
The right subtree contains larger values than the root.
So, given a current node (root), we can determine where p and q lie:

If both p and q are smaller than root, move left.
If both p and q are larger than root, move right.
If root is between p and q (or equal to one of them), root is the LCA.

'''