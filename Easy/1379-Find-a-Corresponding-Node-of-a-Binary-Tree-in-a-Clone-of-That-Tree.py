# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # curr_original = original
        # curr_cloned = cloned
        
        def dfs(curr_original: TreeNode, curr_cloned: TreeNode, target: TreeNode, arr: list) -> TreeNode:
            if not curr_original or not curr_cloned: return
            
            if curr_original == target:
                arr.append(curr_cloned)
                return
            
            dfs(curr_original.left, curr_cloned.left, target, arr)
            dfs(curr_original.right, curr_cloned.right, target, arr)
        
        arr = []
        dfs(original, cloned, target, arr)
        
        return arr[0]