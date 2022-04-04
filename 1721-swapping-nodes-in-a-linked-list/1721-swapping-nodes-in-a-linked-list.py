# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        a, b = head, head
		
        for i in range(k - 1):
            b = b.next
        first = b

        while b.next:
            a, b = a.next, b.next
		
        first.val, a.val = a.val, first.val

        return head
        