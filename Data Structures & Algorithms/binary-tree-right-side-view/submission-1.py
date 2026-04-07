# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # first approach: level-order traversal, but only return the last node on each level
        # seems like this is the most basic and clear solution, don't suppose we can get better
        # than linear time here
        res = []
        this_level = []
        next_level = [root] if root else []

        while next_level:
            this_level = next_level
            next_level = []
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(this_level[-1].val)

        # for node in res: print(node.val)
        return res