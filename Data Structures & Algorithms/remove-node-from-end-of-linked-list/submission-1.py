# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_1 = head 
        current = head
        counter = 0
        length = 0
        while current_1:
            current_1 = current_1.next
            length+=1
        if n == length:
            return head.next
        while current:
            if counter == (length-n-1):
                current.next = current.next.next
                break
            current = current.next 
            counter += 1

        return head
    





        