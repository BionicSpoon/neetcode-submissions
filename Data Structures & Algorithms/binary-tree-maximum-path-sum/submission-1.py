# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # not the same as max path length but summing vals?
        # for each node, add its val to the sum of its childrens'
        # maxPathSums.
        # Return the max path through this node
        # NOTE: if maxPathSum of a child is negative, ignore it
        # OTHER NOTE: we should store the max path sum found 
        # in a nonlocal var

        # MISTAKE: did not account for each node can only be in path once
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_path_sum = max(left, 0) + max(right, 0) + node.val
            res = max(res, max_path_sum)
            return max(max(left, 0), max(right, 0)) + node.val


        dfs(root)
        return res