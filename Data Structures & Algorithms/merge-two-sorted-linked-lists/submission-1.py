# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = ListNode()
        cur = res
        while list1 or list2:
            if not list1:
                # list2 is something
                cur.val = list2.val
                list2 = list2.next
                
            elif not list2:
                cur.val = list1.val
                list1 = list1.next

            elif list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next

            else:
                cur.val = list2.val
                list2 = list2.next
                
            if list1 or list2:
                cur.next = ListNode()
                cur = cur.next
            
        return res