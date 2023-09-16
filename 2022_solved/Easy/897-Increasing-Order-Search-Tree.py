# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def traverse_leftright(root, arr):
            if root.left:
                traverse_leftright(root.left, arr)
            arr.append(root.val)
            if root.right:
                traverse_leftright(root.right, arr)
        
        # get list of node from left -> right
        node_lst = []
        traverse_leftright(root, node_lst)
        
        # convert list of node into tree
        root = TreeNode(node_lst[0])
        curr = root
        node_lst = node_lst[1:]
        while node_lst:
            curr.right = TreeNode(node_lst[0])
            curr = curr.right
            node_lst = node_lst[1:]
            
        return root