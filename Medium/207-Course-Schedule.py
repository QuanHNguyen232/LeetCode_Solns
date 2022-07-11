class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [set() for _ in range(numCourses) ]
        outdegrees = [set() for _ in range(numCourses) ]
        
        for (a, pre) in prerequisites:
            indegrees[a].add(pre)
            outdegrees[pre].add(a)
            
        q =[ i for i,e in enumerate(indegrees) if len(e) == 0]
        taken = set(q)

        while q:
            curr = q.pop()
            for i in outdegrees[curr]:
                indegrees[i].remove(curr)
                if len(indegrees[i]) == 0:
                    taken.add(i)
                    q.append(i)

      
        return len(taken) == numCourses

# https://leetcode.com/problems/course-schedule/discuss/2263692/simple-python-solution-faster-than-91.80