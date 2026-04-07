# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let's iterate through the linked list and keep a var pointed at the prev node
        # then, whenever we move to a node, follow these steps:
        # 1. get the next node and store it in a next_node var
        # 2. set the current node's next pointer to the prev_node
        # 3. move prev_node to cur_node and cur_node to the next_node

        cur = head
        prev = None
        while cur:
            
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

        # prev_node: ListNode = None
        # cur_node: ListNode = head
        # next_node: ListNode = head

        # # was not necessary ez
        # # if not head or not head.next:
        # #     return head

        # while next_node is not None:
        #     # print(cur_node.val, cur_node.next)

        #     next_node = cur_node.next
        #     cur_node.next = prev_node
        #     prev_node = cur_node
        #     cur_node = next_node

            
        
        # return prev_node