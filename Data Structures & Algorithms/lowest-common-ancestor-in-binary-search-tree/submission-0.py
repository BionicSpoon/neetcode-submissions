# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we know root is a binary search tree where all values are unique,
        # so we have to find the lowest node that splits nodes p and q ?
        # or else the node that is p or q if the other node is the node's descendant

        # basic try: just search the bst until min(p, q) <= cur and max(p, q) >= cur

        left_target = min(p.val, q.val)
        right_target = max(p.val, q.val)
        cur = root
        while not (left_target <= cur.val and right_target >= cur.val):
            if cur.val < left_target:
                # cur is too small
                cur = cur.right
            else:
                cur = cur.left

        return cur