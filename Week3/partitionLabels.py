from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        last_index = defaultdict(int)
        
        for i, ch in enumerate(S):
            last_index[ch] = i
            
        ans = []
        first = 0
        last = last_index[S[0]]
        
        for i in range(0, len(S)):
            if i > last:
                ans.append(last - first + 1)
                first = i
            
            last = max(last_index[S[i]], last)
        
        ans.append(len(S) - first)
        return ans
            