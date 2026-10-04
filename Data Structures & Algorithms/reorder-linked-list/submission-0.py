# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head 
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next # [ 4 - > 5n]
        prev = None

        
        while curr:
            temp = curr.next # [4 -> 5, temp = 5
            curr.next = prev # [4 -> 5, ] temp = 5,  [ None <- 4 -> 5 ]
            prev = curr #  [ 4 <- 4 -> 5 ]
            curr = temp #  [ 4 <- 5]
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = first
            first = temp1
            second = temp2
        
        return head

        

