"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        tree_dict = defaultdict(list)
        
        def PreOrder_traverse(node: 'Node', level: int):
            if not node: return
            
            tree_dict[level].append(node.val)
            for child in node.children:
                PreOrder_traverse(child, level+1)
        
        
        PreOrder_traverse(root, 0)
        ret = []
        for i in range(len(tree_dict)):
            ret.append(tree_dict[i])
        
        
        return ret