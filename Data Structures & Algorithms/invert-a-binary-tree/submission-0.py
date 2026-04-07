# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # I've heard all binary tree problems are just one of the four traversals:
        # in, post, pre, and level-order traversal
        # clearly, this is pre order because we need to access the parent first and invert
        # its children before moving down the tree
        # should be easy to do with recursion or a queue and bfs type algorithm

        # let's do recursion for now
        if not root:
            return None
        temp = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp
        return root