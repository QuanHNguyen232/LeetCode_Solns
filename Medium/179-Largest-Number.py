from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_strs = [str(num) for num in nums]
        
        nums_strs.sort(key = cmp_to_key(self.cmp_func), reverse = True) # sort by custom compare
        
        return ''.join(nums_strs).lstrip('0') or '0' # strip off all leading zeroes or return 0 if empty
        
    def cmp_func(self, x, y):
        if int(x + y) > int(y + x): # sorted value by concatenated string increasingly
            return 1
        elif int(x) == int(y):
            return 0
        return -1