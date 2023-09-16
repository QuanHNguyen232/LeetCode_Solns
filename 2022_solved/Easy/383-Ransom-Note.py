class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = collections.Counter(magazine)
        ransomNote_dict = collections.Counter(ransomNote)
        
        char_set = set(magazine_dict.keys())
        
        for char in ransomNote_dict.keys():
            if char not in char_set: return False
            if ransomNote_dict[char] > magazine_dict[char]: return False
        
        return True