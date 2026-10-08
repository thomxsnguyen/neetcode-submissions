# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            curr = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next =list2
                    list2 = list2.next
                curr = curr.next
            curr.next = list1 if list1 else list2
            
            return dummy.next
                    

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged = mergeTwoLists(l1, l2)
                mergedLists.append(merged)
            lists = mergedLists
        
        return lists[0]