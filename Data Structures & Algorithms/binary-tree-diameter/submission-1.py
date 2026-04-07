# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # very similar to the last problem (height of binary tree)
        # it looks like this can be easily done by returning the furthest node from the given node
        # in post order with a recursive DFS
        # this can be found easily by comparing the max length to the left and right and adding them
        # to get the max diameter of the subtree from this node
        # however, only the max between each of these components could be used for results above,
        # so this adds some complexity. If we return this max every time, though,
        # we can keep track of the max seperately and be fine
        self.res = 0
        def visit(node):
            """Return the height of the passed node and update the result with the sum of
            the heights of this node's children + 0"""
            if not node:
                return 0

            left_height = visit(node.left)
            right_height = visit(node.right)
            print(node.val, node.left, left_height, right_height)


            self.res = max(self.res, left_height + right_height)
            print(self.res)
            return 1 + max(left_height, right_height)
        
        visit(root)
        return self.res