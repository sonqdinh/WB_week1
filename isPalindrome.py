class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        sList = []
        
        for ch in s.lower():
            if ch.isalnum():
                sList.append(ch)
                
        left, right = 0, len(sList) - 1
        while left < right:
            if sList[left] != sList[right]:
                return False
            left, right = left + 1, right - 1
        
        return True