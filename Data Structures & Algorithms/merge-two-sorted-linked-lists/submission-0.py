# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        new = None
        head = None
        while l1 and l2:
            if l1.val > l2.val:
                if new:
                    new.next = l2
                    new = new.next
                    l2 = l2.next
                else:
                    new = l2
                    head = new
                    l2 = l2.next
            else:
                if new:
                    new.next = l1
                    new = new.next
                    l1 = l1.next
                else:
                    new = l1
                    head = new
                    l1 = l1.next
        if l2 and not l1 and new:
            new.next = l2
        elif l1 and not l2 and new:
            new.next = l1
        elif l2 and not l1:
            head = l2
        elif l1 and not l2:
            head = l1
        
        return head
