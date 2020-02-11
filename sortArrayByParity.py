class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = -1
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                left += 1
                A[i], A[left] = A[left], A[i]
        
        return A