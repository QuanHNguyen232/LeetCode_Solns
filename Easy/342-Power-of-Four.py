class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        if n ==1: return True
        
        i=1
        while i < n:
            i *= 4
            if i==n: return True
        
        return False