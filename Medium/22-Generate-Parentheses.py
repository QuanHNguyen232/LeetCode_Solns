class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def search(result, state, _open, _close, n):
            # base case
            if _open == n and _close == n:
                result.append(state)
                return
            
            if _open < n:
                search(result, state+'(', _open+1, _close, n)
            if _close < _open:
                search(result, state+')', _open, _close+1, n)
        
        
        
        result = []
        search(result, '', 0, 0, n)
        return result

# backtracking