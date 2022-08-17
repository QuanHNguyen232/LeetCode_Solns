class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init dictionary
        my_dict = defaultdict(list)
        for idx, num in enumerate(nums):
            my_dict[num].append(idx)
        
        # loop through each element
        ele_set = set(my_dict.keys())
        for ele in ele_set:
            # get current element idx
            ele_idx = my_dict[ele].pop()

            # get the other element in pair (constrain: only 1 result)
            other_ele = target - ele
            # check if it is in dictionary and that element only exist in 1 position (edge case: [3, 3] - target=6)
            if other_ele in ele_set and len(my_dict[other_ele])>0:
                other_ele_idx = my_dict[other_ele].pop()
                return [ele_idx, other_ele_idx]