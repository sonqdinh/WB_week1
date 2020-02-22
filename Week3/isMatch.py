class Solution:
    def isMatch(self, s: str, p: str) -> bool:
#         def check(i, j):
#             if j == len(p):
#                 return i == len(s)
            
#             match = (i < len(s)) and (s[i] == p[j] or p[j] == '.')
            
#             if j + 1 < len(p) and p[j + 1] == '*':
#                 return check(i, j + 2) or (match and check(i + 1, j))
#             else:
#                 return match and check(i + 1, j + 1)
        
#         return check(0, 0)
        
        dp = [[False]*(len(s) + 1) for _ in range(len(p) + 1)]
        dp[-1][-1] = True
        
        for i in reversed(range(len(p))):
            for j in reversed(range(len(s) + 1)):
                first_match = (j < len(s)) and (s[j] == p[i] or p[i] == '.')

                if i + 1 < len(p) and p[i + 1] == '*':
                    dp[i][j] = dp[i + 2][j] or (first_match and dp[i][j + 1])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        
        return dp[0][0]