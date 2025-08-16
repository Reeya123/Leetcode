# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Cues in Q:
- “The cloned tree is a copy of the original”	They have exact same structure , vals , placements 
Both can be traveresed in parallel

- Return a reference to the same node in the cloned tree - ans is the same position in cloned tree as the taget in original tree. 

- VVIMP - KNOW THAT TARGET IS AN OBJECT AND NOT JUST A NUMBER. HENCE "IS " IS USED INSTEAD OF "=="


'''
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #say - if the OBJECT original IS SAME AS OBJECT None.
        if original is None:
            return None
        #say - if the OBJECT original IS SAME AS OBJECT Target - YES TARGET IS AN OBJECT HERE NOT ONLY A VAL THAT NEEDS TO BE CHECKED
        if original is target:
            return cloned

#search and recurse over left subtree
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left

#search and recurse over right subtree
        return self.getTargetCopy(original.right, cloned.right, target)

