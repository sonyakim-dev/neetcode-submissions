# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        curr, prev, temp = head, None, head.next
        while curr:
            curr.next = prev
            prev = curr
            if not temp: break
            curr = temp
            temp = curr.next
        
        return curr