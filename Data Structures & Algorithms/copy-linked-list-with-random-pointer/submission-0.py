"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # holy tech let's make a dict that maps nodes from the original list to their new versions
        # holy not tech i didn't read that random was an index, nvm it is a Node pointer..
        new = Node(0) # dummy node
        v2 = {} # map Node in original to Node in copy
        
        cur = head
        copy_cur = new
        while cur:
            copy_cur.next = Node(cur.val)
            v2[cur] = copy_cur.next
            cur = cur.next
            copy_cur = copy_cur.next

        # print(v2)



        cur = head
        copy_cur = new.next
        # here, we need to set each copy_cur Node's random to the mapped Node in the dict: v2[cur.random]
        while cur:
            # print(cur.val, cur.random.val if cur.random else cur.random)
            copy_cur.random = v2[cur.random] if cur.random is not None else None
            # print(copy_cur.val, copy_cur.random.val if cur.random else cur.random)
            cur = cur.next
            copy_cur = copy_cur.next
            

        return new.next

