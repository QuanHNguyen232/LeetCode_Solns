# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def postOrder_traverse(root, arr):
            if not root: return (0, 0)
            
            left_sum, left_node = postOrder_traverse(root.left, arr)
            right_sum, right_node = postOrder_traverse(root.right, arr)
            
            total_sum = left_sum + right_sum + root.val
            total_node = left_node + right_node + 1
            
            if total_sum//total_node == root.val: arr.append(root)
            
            return (total_sum, total_node)
        
        arr = []
        postOrder_traverse(root, arr)
        return len(arr)