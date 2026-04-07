# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if carry:
                s += 1
                carry = 0
            if s > 9:
                carry = 1
                s -= 10
            cur.next = ListNode(s)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        # cur.next = l1 or l2
        # if carry and (l1 or l2):
        #     cur.next.val += 1
        #     if cur.next.val > 9:
        #         while cur.
        # elif carry:
        #     cur.next = ListNode(1)
        # print(l1.val + l2.val)

        return dummy.next
