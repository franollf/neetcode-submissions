# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()

        # loop while both lists are not empty
        while list1 and list2:
            # Check whos value is lesser
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next

            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        # If one of the lists are completely empty just put the append the rest of the list not empty
        node.next = list1 or list2

        return dummy.next
