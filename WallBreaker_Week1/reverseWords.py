class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        list_s = list(s)
        
        def reverse(start, end):
            while start < end:
                list_s[start], list_s[end] = list_s[end], list_s[start]
                start, end = start + 1, end - 1
            
        left = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                reverse(left, i - 1)
                left = i + 1
        
        reverse(left, len(s) - 1)
        return ''.join(list_s)