class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0:
            return []
        
        rows, cols = len(A), len(A[0])
        
        for r in range(rows):
            left, right = 0, cols - 1
            while left < right:
                A[r][left] ^= 1
                A[r][right] ^= 1
                A[r][left], A[r][right] = A[r][right], A[r][left]
                left, right = left + 1, right - 1
            
            if left == right:
                A[r][left] ^= 1
        
        return A
            
            