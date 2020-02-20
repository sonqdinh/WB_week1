from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        
        for ch in sCount:
            if ch not in tCount or tCount[ch] != sCount[ch]:
                return False
            
        return True if len(tCount) == len(sCount) else False