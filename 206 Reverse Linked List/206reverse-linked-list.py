# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev= None 
        curr = head
        
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            
        return prev