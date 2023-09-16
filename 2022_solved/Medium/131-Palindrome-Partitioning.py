class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def search(s: str, i: int, candidate: list, results: list):
            if i == len(s):
                results.append(candidate.copy())
                return
            
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                
                if sub == sub[::-1]:    # check palindrome
                    candidate.append(sub)
                    search(s, j, candidate, results)
                    candidate.pop()
            
        results = []
        search(s, 0, [], results)
        return results
    
# backtracking with framework
# Framework
# procedure solve(data):
#     procedure search(candidate):
#         if reject(candidate): return
#         if accept(candidate): output(candidate)
#         for new-candidate in possible-extensions(candidate):
#             search(new-candidate)
#     search(root(data))



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        
        def search(s, curr_state):
            if len(s) == 0:
                result.append(curr_state)
            
            for i in range(len(s)):
                sub_s = s[:i+1]
                if sub_s == sub_s[::-1]:
                    search(s[i+1:], curr_state + [sub_s])
        
        search(s, [])
        return result
    
# backtracking