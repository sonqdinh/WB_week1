class Solution:
    def titleToNumber(self, s: str) -> int:
        number = 0
        
        for ch in s:
            number = number * 26 + (ord(ch) - ord('A') + 1)
        
        return number