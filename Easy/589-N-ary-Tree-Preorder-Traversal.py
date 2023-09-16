"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        def helper(root: Node, arr: List) -> None:
            arr.append(root.val)
            
            children = root.children
            for child in children:
                if child:
                    helper(child, arr)
        
        arr = []
        helper(root, arr)
        return arr
