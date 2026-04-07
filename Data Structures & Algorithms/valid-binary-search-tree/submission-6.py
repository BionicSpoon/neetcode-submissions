# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, float('inf'), float('-inf'))

            left = dfs(node.left)
            right = dfs(node.right)

            if not left or not right:
                return False
            
            max_left = left[2]
            min_right = right[1]

            if max_left >= node.val or min_right <= node.val:
                return False
            return (True, min(left[1], node.val), max(right[2], node.val))

        return dfs(root) != False
