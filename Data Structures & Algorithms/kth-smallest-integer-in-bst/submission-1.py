# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur_index = 0
        res = root.val
        
            # simple in order traversal (in order traversal gives bst in order min->max)
        def dfs(node):
            nonlocal cur_index, res
            if not node:
                return None
            dfs(node.left)
            
            cur_index += 1
            if cur_index == k:
                res = node.val
            
            dfs(node.right)
            return 1

        dfs(root)
        return res