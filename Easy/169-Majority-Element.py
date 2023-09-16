class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        
        thres = len(nums)/2
        for key, val in d.items():
            if val> thres:
                return key
        return -1