# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree_root = root
        self.val_lst = set([])
        self.recover(self.tree_root, 0)
        
        
    def recover(self, root, val):
        if not root:
            return
        
        # assign value & add to list of value
        root.val = val
        self.val_lst.add(val)
        
        # continue assign values to children
        self.recover(root.left, 2*val + 1)
        self.recover(root.right, 2*val + 2)
        
        
        
    def find(self, target: int) -> bool:
        return target in self.val_lst


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)