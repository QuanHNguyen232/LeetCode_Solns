# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        def traverse(root, arr):
            if root.left:
                # if root.left is leaf
                if (not root.left.left) and (not root.left.right):
                    arr.append(root.left.val)
                else:
                    traverse(root.left, arr)
            if root.right:
                traverse(root.right, arr)
        
        arr = []
        traverse(root, arr)
        
        return sum(arr)