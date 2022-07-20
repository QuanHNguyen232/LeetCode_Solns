# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return 0 
            
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            
            node_sum = node.val + left_sum + right_sum
            node_diff = abs(left_sum - right_sum)
            node.val = node_diff
            
            return node_sum
        
        def traverse_inOrder(node, arr):
            if not node: return
            
            arr.append(traverse_inOrder(node.left, arr))
            arr.append(node.val)
            arr.append(traverse_inOrder(node.right, arr))
            
        helper(root)
        arr = []
        traverse_inOrder(root, arr)
        
        return sum(x for x in arr if x != None)