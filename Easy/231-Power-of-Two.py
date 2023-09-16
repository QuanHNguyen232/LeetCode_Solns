class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        def helper(val):
            print(val)
            if val == n:
                return True
            if val > n:
                return False
            
            return helper(val*2)

        return helper(1)