# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid node and the tail - slow becomes the mid node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half - prev becomes the head of the second half
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        #                s    c         p
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        while second:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp
