# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:

            ## set hte next thing to a temporary value
            temp = curr.next

            curr.next = prev 
            ## change the 
            prev = curr
            
            curr = temp 
        
        return prev
            


