class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            ret.append(curr_sum)
        return ret