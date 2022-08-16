class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = defaultdict(int)
        
        for c in s:
            char_dict[c] += 1
        
        
        for idx, c in enumerate(s):
            if char_dict[c] == 1: return idx
        
        return -1