# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)
        
        while True:
            if min_val <= root.val <= max_val:
                return root
            elif max_val < root.val:
                root = root.left
            else:
                root = root.right
