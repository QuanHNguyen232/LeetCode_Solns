# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # Constrains: Every node has either 0 or 2 children
        def helper(root):
            # leaf node
            if not root.left and not root.right:
                return root.val
            
            # not leaf
            if root.val == 2:
                return helper(root.left) or helper(root.right)
            else:
                return helper(root.left) and helper(root.right)
        
        return helper(root)
