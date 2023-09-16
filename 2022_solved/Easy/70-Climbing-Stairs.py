class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        if n <= 1:
            return arr[n]
        else:
            for i in range(2, n+1):
                arr.append(arr[i-2] + arr[i-1])
        
        return arr[n]
        