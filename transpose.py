class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0:
            return []
        
        rows, cols = len(A), len(A[0])
        B = [[0]*rows for _ in range(cols)] 
        
        for r in range(rows):
            for c in range(cols):
                B[c][r] = A[r][c]
        
        return B