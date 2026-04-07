# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index = {val: idx for (idx, val) in enumerate(inorder)}
        
        # print(index)
        def recBuildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            # all this needs to do is pick the top node from preorder (first node), create a TreeNode with that val,
            # split inorder at that val, and call recursively twice for left and right children
            # But when are we supposed to consume from preorder? Only if inorder exists here. ?
            # base case: no children
            index = {val: idx for (idx, val) in enumerate(inorder)}
            if not inorder or not preorder:
                return None

            if len(inorder) == 1:
                if preorder[0] == inorder[0]:
                    preorder.pop(0)
                else:
                    print("I messed up")
                return TreeNode(inorder[0])

            # len(inorder) > 1
            val = preorder.pop(0)
            tmp = TreeNode(val)      

            tmp.left = self.buildTree(preorder, inorder[:index[val]]) 
            tmp.right = self.buildTree(preorder, inorder[index[val]+1:]) # safe because slicing is safe

            return tmp

            

        return recBuildTree(preorder, inorder)




































        # redo this all. This should be recursive; we need to split inorder on the first preorder node
        # then make a recursive call to assign the left and right child based on the left and right halves
        # of inorder.
        # Once we pop all vals from preorder, we will be done?
        # if not inorder:
        #     return None


        # val = preorder.pop(0)
        # node = TreeNode(val=val)
        # print(inorder, val)
        # val_idx = inorder.index(val)
        # inorder.remove(val)
        # left_inorder = inorder[:val_idx]
        # right_inorder = inorder[val_idx:] if val_idx < len(inorder) - 1 else []

        # node.left = self.buildTree(preorder, left_inorder)
        # node.right = self.buildTree(preorder, right_inorder)

        # return node


        # if a node is highest in preorder, it's left and right inorder ints are its children
        # provided we remove ints from inorder and replace with None after they become a node val/are consumed

        while preorder:
            val = preorder.pop(0)
            val_idx = inorder.index(val)
            new = ListNode(val)
            if val_idx > 0:
                left_val = inorder[val_idx - 1]
                if left_val:
                    new.left = ListNode(left_val)
                    inorder[val_idx - 1] = None
            if val_idx < len(inorder) - 1:
                right_val = inorder[val_idx + 1]
                if right_val:
                    new.left = ListNode(right_val)
                    inorder[val_idx + 1] = None






        # # pop nodes from preorder -> place them somewhere in the tree based on relative inorder position


        # root = TreeNode(val=preorder.pop(0)) # always at least one int
        # cur = root
        # parents = [root]
        
        # while preorder:
        #     val = preorder.pop(0)
        #     new_node = TreeNode(val)
        #     is_left_of_cur = True if inorder.index(val) < inorder.index(cur.val) else False
        #     print(is_left_of_cur)

        #     if is_left_of_cur and not cur.left:
        #         cur.left = new_node
        #         parents.append(cur)
        #         cur = cur.left
                
        #     elif is_left_of_cur and not cur.right:
        #         cur.right = new_node
        #         parents.append(cur)
        #         cur = cur.right
            
        #     elif not is_left_of_cur
            

        # return root