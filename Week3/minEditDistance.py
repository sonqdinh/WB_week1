class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        nOps = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0:
                    nOps[i][j] = j
                elif j == 0:
                    nOps[i][j] = i
                else:
                    if word2[i - 1] != word1[j - 1]:
                        nOps[i][j] = 1 + min(nOps[i - 1][j - 1], 
                                             nOps[i - 1][j],
                                             nOps[i][j - 1])
                    else:
                        nOps[i][j] = nOps[i - 1][j - 1]
        
        return nOps[-1][-1]