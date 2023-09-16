class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.edges = defaultdict(set)
        
        # DFS
        def dfs(src, goal):
            self.visited = set()
            def helper(node, product):
                if node == goal and node in self.edges:
                    return product
                if node in self.visited:
                    return -1.0
                self.visited.add(node)
                for edge in self.edges[node]:
                    (dest, weight) = edge
                    result = helper(dest, product * weight)
                    if result != -1:
                        return result
                return -1
            
            return helper(src, 1)
            
            
        # init directed graph
        for equa, val in zip(equations, values):
            (num, den) = equa # numerator/denominator
            self.edges[num].add((den, val))
            self.edges[den].add((num, 1/val))
        
        return [dfs(src, dest) for (src, dest) in queries]
        
# Solution from CodePath Summer22 Week7 Session2 lecture
