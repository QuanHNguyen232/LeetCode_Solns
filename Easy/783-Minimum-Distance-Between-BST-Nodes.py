# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inOrder_traverse(root, arr):
            if not root: return
            
            inOrder_traverse(root.left, arr)
            arr.append(root.val)
            inOrder_traverse(root.right, arr)
        
        arr = []
        inOrder_traverse(root, arr)
        minVal = sys.maxsize
        for i in range(1, len(arr)):
            minVal = min(minVal, arr[i]-arr[i-1])
        
        return minVal

# Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/