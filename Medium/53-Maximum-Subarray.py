class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_run = nums[0]
        best_run = nums[0]
        for i in range(1, len(nums)):
            current_run = max(nums[i], current_run + nums[i])
            best_run = max(best_run, current_run)
        return best_run

# CodePath sln Week9 Session2