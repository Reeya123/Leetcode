# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue: #continue until queue is empty 
            p, q = queue.popleft()
            
            '''
            3 cases:
            - are p and q nodes? are their vaalues equal?
            - p = None , q = None; return True 
            - (p =None and q != None) or (p !=None and q = None); return False 
            
            '''
            
            # Case 1: If both nodes are None, continue to next iteration
            if not p and not q:
                continue 
            
            # Case 2: If only one of them is None, trees are not same
            if not p or not q:
                return False 
            
            # Case 3: If values are different, trees are not same
            if p.val != q.val:
                return False 
            
            # Push left and right children to stack for further comparison
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
            
        # If the loop completes without returning False, the trees are same    
        return True