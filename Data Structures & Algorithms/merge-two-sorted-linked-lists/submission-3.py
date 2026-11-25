# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        # Create a dummy and a traversing node on an entirely new linked list
        dummy = node = ListNode()

        # Loop through while both lists are not None
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next
            
            # ?
            node = node.next

        node.next = list1 or list2


        return dummy.next

        # Check if value on either list is less, whichever is you have to append it onto the new linkedlist

        # when either is done just append the rest of the list onto it


        # return dummy.next