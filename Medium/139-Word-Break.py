class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s=='': return True
        
        memo = {"": True}
        
        def helper(string):
            if string in memo: return memo[string]
            ans = False
            
            # iterate through all elements
            for word in wordDict:
                if string.startswith(word):
                    ans = helper(string[len(word):])   # string startswith(next word) -> ans = True
                    if ans: break
            
            memo[string] = ans
            
            return ans
        
        return helper(s)

# Understand Problem: https://docs.google.com/presentation/d/1esAxrnlYRPl6rD54l0Py3azScIJwpuQpeb8B5RO0hOk/edit#slide=id.g13f85d191d9_0_677
    