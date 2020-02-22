class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        for ch in t:
            idx = ord(ch) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return False if sum(count) else True