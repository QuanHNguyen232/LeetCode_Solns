class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 1
        
        arr = sorted(nums_dict.keys())
        
        count = 0
        ret = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]+1:
                count += 1
            else:
                count = 0
            ret = max(ret, count)
        
        return ret+1

# O(nlogn)
# How to solve w/ O(n)