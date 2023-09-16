class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = []
        
        for i in range(1, n+1):
            num.append(str(bin(i))[2:]) # bin() results in 0bxxx -> get from xxx
        
        bin_num = ''.join(num)
        
        return int(bin_num, 2)%(10**9+7)
        