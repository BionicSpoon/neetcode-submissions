# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
                # the procedure for solving this (as derived mainly from the 2nd hint, I could not figure out)
        # is to:
        # 1. split the list in half (less on left side if uneven)
        # 2. reverse the second half
        # 3. merge the lists one element at a time
        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1

        half = length // 2 # number of nodes in the first half
        # print(half)

        # now to split the second half (rounded up) from the list
        first = head
        cur = first
        i = 1
        while i < half:
            cur = cur.next
            i += 1
        second = cur.next
        cur.next = None

        # print(first.val, cur.val, cur.next, second.val)

        # now to reverse the second half
        cur = second
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        second = prev
            
        # print(first, second)

        # Now we just have to merge the two lists one by one, starting from the first list
        # Do this by inserting nodes from the second list into the first
        cur = first
        while cur.next:
            temp = cur.next
            cur.next = second
            second = second.next
            cur = cur.next
            cur.next = temp
            cur = cur.next
    
        cur.next = second