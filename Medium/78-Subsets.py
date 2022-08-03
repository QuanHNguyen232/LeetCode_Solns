class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(result, nums, tmp):
            result.append(tmp)
            
            for i in range(len(nums)):
                helper(result, nums[i+1:], tmp+[nums[i]])
        
        
        result = []
        helper(result, nums, [])
        return result

# CodePath Week10 Session1 Portal sln



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        candidate = []
        
        def search(index):
            if index >= len(nums):
                result.append(candidate.copy())
                return
            
            # take element nums[i]
            candidate.append(nums[index])
            search(index+1)
            
            # don't take element nums[i] --> backtrack
            candidate.pop()
            search(index+1)
            
        search(0)
        return result

# CodePath Week10 Session1 Lecture sln
# backtracking