# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        lowerValues, higherValues = [], []
        while(head):
            if head.val < x: lowerValues.append(head.val)
            else: higherValues.append(head.val)
            head = head.next
        
        result = pointer = ListNode(-1)
        
        for value in lowerValues:
            result.next = ListNode(value)
            result = result.next
        
        for value in higherValues:
            result.next = ListNode(value)
            result = result.next
        
        return pointer.next