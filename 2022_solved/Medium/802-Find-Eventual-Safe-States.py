class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node, visited):
            # terminal node
            if len(graph[node])==0: return True
            if node in visited: return False
            
            visited.add(node)
            
            answer = True
            for n in graph[node]:
                answer = answer and dfs(n, visited)
            
            if answer:
                graph[node]=[]
            
            return answer
        
        num_nodes = len(graph)
        ret_list=[]
        visited = set([])
        for i in range(num_nodes):
            if dfs(i,visited):
                ret_list.append(i)
        
        return ret_list
