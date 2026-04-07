# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to check for the subroot at every node in the main tree? O(n*m)
        # guess that's fine based on the constraints
        # so the approach is: call isSame(node, subRoot) for every node stemming from root
        # isSame() will check the entirety of each tree and return true iff they are exactly the same

        self.res = False
        def isSame(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            if node1.val == node2.val and isSame(node1.left, node2.left) and isSame(node1.right, node2.right):
                return True

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if isSame(node, subRoot):
                return True

        return False