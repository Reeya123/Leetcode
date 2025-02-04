# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''

Merge two sorted lists

use a dummy node(to keep a track of head)
and a curr pointer pointing at dummy.

- Define a node class. Each node will have the refernece to the next node - next 
- inialize dummy node 
- and also have a curr pointer pointing to dummy
- dummy will point to the head of the linked list
- list1 and list2 arent lists; they are pointers( refernces) to the head of the two linkedlists 

 if you are given inputs like list1 = [1, 2, 4] and list2 = [1, 3, 4], these are not linked lists yet. They are Python lists (arrays) by default. 
 For a function like merge() to work, you need to first convert these Python lists into linked lists using a helper function.
'''

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy 
        # list1 and list2 are variables pointing to the head of two linked lists
        while list1 and list2: #while the lists arent
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                
            else:
                curr.next = list2
                list2 = list2.next
                
            curr = curr.next
            
        if list1:
            curr.next = list1
            
        if list2:
            curr.next = list2
            
            
        return dummy.next


'''

# Helper function to convert a Python list to a linked list
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Create linked lists from Python lists
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Merge the linked lists
merged_list = merge(list1, list2)

# Print the merged linked list
print_linked_list(merged_list)
'''
                    
                    

            