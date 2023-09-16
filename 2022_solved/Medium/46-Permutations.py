class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            
        def helper(slns, state, nums):
            # have we reached this solution? --> add solution
            if not nums:
                slns.append(state.copy())
                return
            
            # have we reached an impossibility? --> abort rest of this search
            # recurse with next state and candidate of search
            for num in nums:
                state.append(num)
                helper(slns, state, nums - set([num]))
                state.pop()
        
        
        
        slns = []
        helper(slns, [], set(nums))
        return slns

# Solution: https://youtu.be/nqerP0SvzZI