class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # All power of two has binary forms:
        # 10000000 so clear the MSB of power of two will return 0
        if n == 0:
            return False
        else:
            return n & (n - 1) == 0