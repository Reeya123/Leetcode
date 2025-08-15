# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        '''
        Base cases usually are checking for empty trees but since it a full BT 
        there will be atleast one node. 
        So we check if theres just 1 node, simply return its bool val
        '''
        if not root.left and not root.right:
            return bool(root.val) #why bool? original tree has numeric vals lie 1,0

        #if its not a leaf node.  it will always have 2 childrens 
        #calculate left and right recursively

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right

        if root.val == 3:
            return left and right 

            
