# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inOrder_traverse(root, arr):
            if not root: return
            inOrder_traverse(root.left, arr)
            arr.append(root.val)
            inOrder_traverse(root.right, arr)

        arr = []
        inOrder_traverse(root, arr)
        return arr == sorted(list(set(arr)))