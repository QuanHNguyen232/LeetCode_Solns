class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_map = defaultdict(list)
        
        for city, neighs in enumerate(isConnected):
            for neigh, val in enumerate(neighs):
                if val == 1:
                    city_map[city].append(neigh)
        
        
        def dfs(city, isVisited: set):
            
            isVisited.add(city)
            
            for neigh in city_map[city]:
                if neigh not in isVisited and neigh!=city:
                    dfs(neigh, isVisited)
        
        count = 0
        isVisited = set([])
        for i in range(len(isConnected)):
            if i not in isVisited:
                count+=1
                dfs(i, isVisited)
        
        return count