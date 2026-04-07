# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # should be easy enough with a post-order traversal recursive solution

        # just check if the children are valid (l < this and this < r)
        # then call recursively on the children

        # alright that won't quite work because there can be a deep node that breaks the BST only
        # when compared to the root node

        # instead, let's get keep track of the max node to the left and min node to the right,
        # then for each node, we can just check these two values to see if the BST is valid.
        # But how should we find these min and max values?
        # let's do a post order traversal, and replace every node.val with (subtree_min, subtree_max)
        # from there, it will be easier to check for valid BST
        
        # it would've been much better to do the DFS solution from the video, where you traverse the 
        # tree in pre order and keep track of left and right bounds for each node to be valid, then
        # return False as you go if there is an invalid node

        def isValid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root, -math.inf, math.inf)




        def setNode(node):
            if not node:
                return True
            
            if not setNode(node.left): return False
            if not setNode(node.right): return False

            cur_val = node.val
            if not node.left and not node.right:
                node.val = (node.val, node.val)
                return True

            elif not node.left:
                node.val = (min(node.right.val[0], node.val), max(node.right.val[1], node.val))
                return cur_val < node.right.val[0]

            elif not node.right:
                node.val = (min(node.left.val[0], node.val), max(node.left.val[1], node.val))

                print(cur_val)
                print(f'returning {cur_val > node.left.val[1]}')
                return cur_val > node.left.val[1]

            else:
                node.val = (min(node.left.val[0], node.val, node.right.val[0]), max(node.left.val[1], node.val, node.right.val[1]))
                return cur_val < node.right.val[0] and cur_val > node.left.val[1]

        return setNode(root)





