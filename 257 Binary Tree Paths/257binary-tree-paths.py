# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        def dfs(node, path, result):
            if not node:
                return
            
            # Append the current node's value to the path
            path += str(node.val)
            
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                result.append(path)
            else:
                # Continue the path with '->' and explore left and right children
                path += '->'
                dfs(node.left, path, result)
                dfs(node.right, path, result)
        
        result = []
        dfs(root, "", result)
        return result
        