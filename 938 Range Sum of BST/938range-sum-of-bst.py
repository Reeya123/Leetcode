# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        def dfs(node):
        
            if node is None:
                return 0
            sumofnode = 0
            if low <= node.val <= high:
                sumofnode = sumofnode + node.val
                
            
            if node.val > low:
                sumofnode += dfs(node.left)
            if node.val < high:  
                sumofnode += dfs(node.right)
                    
            return sumofnode
        
        return dfs(root)
            