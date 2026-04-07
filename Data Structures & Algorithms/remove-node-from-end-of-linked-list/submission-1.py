# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        if length == 1:
            return None
        if length == n:
            return head.next
        print(f'{length=}')
        length -= n
        cur = head
        for _ in range(length-1):
            cur = cur.next
        print(cur.val)
        # cur.val = cur.next.val/
        cur.next = cur.next.next
        return head
