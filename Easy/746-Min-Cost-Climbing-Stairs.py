class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curr_cost = 0
        ptr0, ptr1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            # calculate min total cost
            curr_cost = cost[i] + min(ptr0, ptr1)
            
            # update step
            ptr0, ptr1 = ptr1, curr_cost
        
        return min(ptr0, ptr1)
