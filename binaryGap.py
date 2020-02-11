class Solution:
    def binaryGap(self, N: int) -> int:
        first_one = True
        i = 0
        maxDistance = 0
        left = -1
        
        while N:
            # Check last bit:
            if N & 1:
                if not first_one:
                    maxDistance = max(maxDistance, i - left)
                else:
                    first_one = False
                left = i
            
            i += 1
            N >>= 1
        
        return maxDistance
                
        