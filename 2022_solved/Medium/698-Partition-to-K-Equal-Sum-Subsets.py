class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # approach
        # if k=1: True (always)
        # if k=2: for [1, 2]: False, sum(nums) must divisible by k
        # [1, 2, 3]; k=2 --> try all subsets: [1, 2, 3], [(1, 2), 3], [1, (2, 3), etc]
        
        # Framework
        # procedure solve(data):
        #     procedure search(candidate):
        #         if reject(candidate): return
        #         if accept(candidate): output(candidate)
        #         for new-candidate in possible-extensions(candidate):
        #             search(new-candidate)
        #     search(root(data))
        
        
        
        def search(i: int) -> bool:
            if i == len(nums):
                print(set_sums)
                return all(j==target for j in set_sums)
        
            for j in range(k):
                if set_sums[j] + nums[i] > target: continue
                set_sums[j] += nums[i]
                if search(i+1): return True
                set_sums[j] -= nums[i]
                if set_sums[j] == 0: return False
                    
            return False
        
        
        
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0: return False
        
        target = total // k
        set_sums = [0]*k
        
        return search(0)

# CodePath Week10 Session2 Lecture sln