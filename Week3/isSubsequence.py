class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = 0
        i = 0
        
        while check < len(s) and i < len(t):
            while i < len(t) and t[i] != s[check]:
                i += 1
            
            if i < len(t) and t[i] == s[check]:
                check += 1
                i += 1
        
        return True if check == len(s) else False