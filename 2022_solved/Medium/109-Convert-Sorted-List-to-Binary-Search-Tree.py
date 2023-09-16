# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        def createTree(nums):
            if not nums or len(nums) == 0:
                return 
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = createTree(nums[:mid])
            root.right = createTree(nums[mid+1:])
            return root

        # convert to array
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        # add vals from arr to tree
        tree_root = createTree(nums)
        return tree_root
                