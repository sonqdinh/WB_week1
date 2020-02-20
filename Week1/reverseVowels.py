class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        
        sList = list(s)
        
        vowels = {'a','e','o','u','i', 'A', 'E','O','U','I'}
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right:
                if sList[left] in vowels:
                    break
                left += 1
            
            while right > left:
                if sList[right] in vowels:
                    break
                right -= 1
            
            if left != right:
                sList[left], sList[right] = sList[right], sList[left]
                left, right = left + 1, right - 1
        
        return ''.join(sList)
                