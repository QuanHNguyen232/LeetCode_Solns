class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]
        minPrice = prices[0]
        
        for idx in range(1, len(prices) + 1):
            minPrice = min(minPrice, prices[idx - 1])
            dp.append(max(dp[idx - 1], prices[idx - 1] - minPrice))
            
        return dp[-1]