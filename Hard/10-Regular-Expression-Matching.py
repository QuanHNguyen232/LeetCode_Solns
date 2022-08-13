class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for col in range(1, len(p)+1):
            if p[col-1] == '*':
                dp[0][col] = dp[0][col-2]
            
        for row in range(1, len(s)+1):
            for col in range(1, len(p)+1):
                if p[col-1] == s[row-1] or p[col-1] == '.':
                    dp[row][col] = dp[row-1][col-1]
                elif p[col-1] == '*':
                    dp[row][col] = dp[row][col-2]
                    if p[col-2] == s[row-1] or p[col-2] == '.':
                        dp[row][col] = dp[row][col] or dp[row-1][col]
        
        return dp[len(s)][len(p)]
        