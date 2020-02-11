class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        
        # First letter is capital:
        if ord('A') <= ord(word[0]) <= ord('Z'):
            capital = normal = False
            for ch in word[1:]:
                if ord('A') <= ord(ch) <= ord('Z'):
                    capital = True
                else:
                    normal = True
            
            if capital and normal:
                return False
        else:
            for ch in word:
                if ord('A') <= ord(ch) <= ord('Z'):
                    return False
        
        return True