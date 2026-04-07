# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = None
        for l in lists:
            res = self.mergeTwo(res, l)
        return res

        
    def mergeTwo(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = ListNode()
        cur = res
        while list1 or list2:
            if not list1:
                # list2 is something
                cur.next = list2
                list2 = list2.next
                
            elif not list2:
                cur.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
                
            if list1 or list2:
                cur = cur.next
        
        return res.next