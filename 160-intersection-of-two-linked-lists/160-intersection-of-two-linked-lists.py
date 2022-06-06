# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp_set = set()
        current = headA
        
        while current:
            temp_set.add(current)
            current=current.next
        
        current = headB
        while current:
            if current in temp_set:
                return current
            current = current.next

        return None