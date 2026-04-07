# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # should be easy, looks like you can just run a dfs and keep track of the max
        # value seen on this path for a simple O(n) time and space complexity solution
        # do this, and just increment res whenever the node.val > max_val
        # seems simplest to just do this with a recursive dfs implementation,
        # but you could also do dfs with a stack, it would just be more tricky to track
        # max_val, which could easily be passed in to the dfs recursive call
        self.good_nodes = 1
        def dfs(node: TreeNode, max_val: int) -> None:
            # check if the current node is a good node, and call itself on this node's children.
            # also, update max_val if node.val > max_val
            if not node:
                return
            
            if node.val >= max_val:
                self.good_nodes += 1
            max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root.left, root.val)
        dfs(root.right, root.val)
        return self.good_nodes