class Solution:
    def uniquePaths(self, m: int, n: int, count={}) -> int:
        if m==0 or n==0:
            return 0
        if m==1 or n==1:
            return 1
        if (m, n) not in count:
            count[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return count[(m, n)]

# CodePath soln Week9 Session2
# Understand Problem: https://docs.google.com/presentation/d/15VyacGaw6fNwm3kBpZihYDBd-g4ii26u4VxkBbYFfTs/edit#slide=id.g142fd3e056a_0_4