# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def checkbalance(node):
            if node is None:
                return 0, True  #height and isbalanced

            leftheight , leftbalanced = checkbalance(node.left)
            rightheight , rightbalanced = checkbalance(node.right)

            currentbalance = leftbalanced and rightbalanced and abs(leftheight - rightheight) <= 1

            checkheight = max(leftheight , rightheight) + 1

            return checkheight, currentbalance

        _, isbalance = checkbalance(root)
        return isbalance
            