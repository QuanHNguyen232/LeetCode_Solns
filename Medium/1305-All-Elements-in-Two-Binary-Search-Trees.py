# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return []
        
        def traverse(root, arr):
            if not root:
                return
            traverse(root.left, arr)
            arr.append(root.val)
            traverse(root.right, arr)
        
        arr1, arr2 = [], []
        traverse(root1, arr1)
        traverse(root2, arr2)
        
        # Merge sort
        ret = []
        ptr1 = ptr2 = 0
        while ptr1<len(arr1) and ptr2<len(arr2):
            if arr1[ptr1] <= arr2[ptr2]:
                ret.append(arr1[ptr1])
                ptr1 += 1
            else:
                ret.append(arr2[ptr2])
                ptr2 += 1
        
        arr = []
        if ptr1 < len(arr1):
            arr = arr1[ptr1:]
        else:
            arr = arr2[ptr2:]
        for val in arr:
            ret.append(val)
        
        return ret
        