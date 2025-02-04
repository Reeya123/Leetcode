# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #l1, l2 are referneces to the first nodes of respective lists
        #dummy node act as the head of result linked list. This helps simplify edge cases and will eventually point to the start of our answer.
        dummy = ListNode(0)
        curr = dummy 
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            
            #divmod - quotient , remainder = divmod(a, b)
            carry , out = divmod( val1 +val2 + carry , 10) #divmod( 1+ 2 + 1, 10) carry = 4//10 ; out = 4 % 10 
            
            curr.next = ListNode(out)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
        