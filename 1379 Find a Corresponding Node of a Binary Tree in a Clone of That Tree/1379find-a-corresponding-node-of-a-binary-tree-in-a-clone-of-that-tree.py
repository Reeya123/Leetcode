# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if original is None:
            return None
        
        if original == target:
            return cloned
        
        lefttree = self.getTargetCopy(original.left , cloned.left , target)
        righttree = self.getTargetCopy(original.right , cloned.right , target)
        
        return lefttree or righttree
        