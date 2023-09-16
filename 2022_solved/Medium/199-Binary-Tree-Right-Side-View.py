# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = defaultdict(list)
        
        def level_traverse(root, depth, col):
            if not root:
                return
            
            d[depth].append((root.val, col))
            
            level_traverse(root.left, depth+1, col-1)
            level_traverse(root.right, depth+1, col+1)
            
        level_traverse(root, 0, 0)
        max_depth = max(d.keys())
        
        ret = []
        # loop through each depth
        for depth in range(max_depth+1):
            curr_val, rightmost_idx = 0, -(sys.maxsize-1)
            # find the rightmost node each depth
            for val, col in d[depth]:
                if col > rightmost_idx:
                    curr_val = val
                    rightmost_idx = col
            ret.append(val)
        
        return ret

# Explain, go to rightmost node of each level