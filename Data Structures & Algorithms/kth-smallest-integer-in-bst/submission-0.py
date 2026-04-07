# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # this is just in-order traversal, but you stop and return after k iterations
        self.counter = 0
        self.res = root.val
        def getKth(node):
            # print(counter)
            if not node:
                return
            
            getKth(node.left)

            self.counter += 1
            if self.counter == k:
                self.res = node.val

            getKth(node.right)

        getKth(root)
        return self.res

            
            
