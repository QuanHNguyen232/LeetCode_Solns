# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Way 1: in-order traversal
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        
        def botUp_traverse(root, depth):
            if not root:
                return
            
            d[depth].append(root.val)
            
            botUp_traverse(root.left, depth+1)
            botUp_traverse(root.right, depth+1)
            
        botUp_traverse(root, 0)
        max_depth = max(d.keys())        
        ret = [d[i] for i in range(max_depth+1)]

        return ret[::-1]


# Way 2: queue (BFS)
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # BFS
        queue = collections.deque()
        queue.append(root)
        
        ret = []
        while queue:
            
            level = []
            
            # loop through nodes in same level -> after this, queue only has nodes in next level
            for _ in range(len(queue)):
                
                curr = queue.popleft()
                
                # add to the level list
                level.append(curr.val)
                
                # push children to queue -> use in while loop
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            # push each level list to main output  
            ret.append(level)
                
        return ret[::-1]


