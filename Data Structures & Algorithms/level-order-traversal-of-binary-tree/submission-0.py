# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ezzz classic BFS in disguise? level order traversal
        # just need to keep a queue of nodes and add the children of each node to a next-level list
        # before moving those to the main queue and clearing the next level list

        res = []
        cur_level = [root] if root else []
        next_level = []

        while cur_level:
            # add all the nodes in cur_level to cur_res, and add their children to next_level
            res.append([cur.val for cur in cur_level])
            for cur_node in cur_level:
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)

            cur_level = next_level
            next_level = []

        return res