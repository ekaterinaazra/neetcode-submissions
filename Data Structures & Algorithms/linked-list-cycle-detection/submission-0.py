# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        short = head 
        long = head 
        while long and long.next:
            short = short.next
            long = long.next.next
            if short == long:
                return True

        return False
