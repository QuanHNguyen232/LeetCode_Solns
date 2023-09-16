# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        fixed_val = root.val
        is_uni = [True]
        
        def traverse(root, is_uni):
            if root.val != fixed_val:
                is_uni[0] =  False
            
            if root.left:
                traverse(root.left, is_uni)
            if root.right:
                traverse(root.right, is_uni)
        
        traverse(root, is_uni)
        
        return is_uni[0]