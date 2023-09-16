# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val=val)
        
        
        def find_insert_loc(target: int, root) -> TreeNode:
            curr_node = root
            ret_node = None
            
            while curr_node:
                ret_node = curr_node
                if target < curr_node.val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            
            return ret_node
        
        # no root: return tnew_node as head
        if not root:
            return new_node
        
        # find which node to add
        node_to_add = find_insert_loc(val, root)
        # determine add left/right
        if val < node_to_add.val:
            node_to_add.left = new_node
        else:
            node_to_add.right = new_node
        
        return root