class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        sList = []
        i = 0
        
        while i < len(strs[0]) and i < len(strs[1]):
            if strs[0][i] == strs[1][i]:
                sList.append(strs[0][i])
            else:
                break
            i += 1
    
        for i in range(2, len(strs)):
            for j in range(len(sList)):
                if j >= len(strs[i]) or strs[i][j] != sList[j]:
                    sList = sList[:j]
                    break
            if len(sList) == 0:
                break
        
        return ''.join(sList)