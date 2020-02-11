class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_xy = x ^ y
        nDiff = 0
        while xor_xy:
            nDiff += 1
            xor_xy &= (xor_xy - 1)
        
        return nDiff